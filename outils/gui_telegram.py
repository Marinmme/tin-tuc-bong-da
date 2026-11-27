"""Gửi file Excel tin bóng đá vào Telegram qua bot.

Cần 2 biến môi trường (chủ dự án tự nhập trong cài đặt môi trường cloud):
    TELEGRAM_BOT_TOKEN  token bot từ @BotFather (bí mật)
    TELEGRAM_CHAT_ID    id người/nhóm nhận file

Cách dùng:
    python3 outils/gui_telegram.py livrables/2026-11-27_tin-bong-da.xlsx
    python3 outils/gui_telegram.py --lay-chat-id   # in chat id của người vừa nhắn bot
"""
import json
import os
import sys
import uuid
import urllib.request
from pathlib import Path

API = "https://api.telegram.org/bot{token}/{method}"
GIOI_HAN = 50 * 1024 * 1024  # bot gửi tối đa 50 MB


def token() -> str:
    t = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
    if not t:
        sys.exit("Lỗi: chưa có biến TELEGRAM_BOT_TOKEN trong môi trường.")
    return t


def goi(method: str, data: bytes | None = None, headers: dict | None = None) -> dict:
    req = urllib.request.Request(API.format(token=token(), method=method),
                                 data=data, headers=headers or {})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            kq = json.load(r)
    except urllib.error.HTTPError as e:
        kq = json.load(e)
    if not kq.get("ok"):
        sys.exit(f"Lỗi Telegram: {kq.get('description', kq)}")
    return kq["result"]


def lay_chat_id() -> None:
    ds = goi("getUpdates")
    if not ds:
        sys.exit("Chưa thấy tin nhắn nào. Hãy nhắn /start cho bot rồi chạy lại.")
    thay = {}
    for u in ds:
        m = u.get("message") or u.get("channel_post") or {}
        c = m.get("chat", {})
        if c:
            thay[c["id"]] = c.get("title") or c.get("first_name") or c.get("username")
    for cid, ten in thay.items():
        print(f"{cid}\t{ten}")


def gui(duong_dan: str) -> None:
    token()
    p = Path(duong_dan)
    if not p.is_file():
        sys.exit(f"Lỗi: không thấy file {p}")
    if p.stat().st_size > GIOI_HAN:
        sys.exit("Lỗi: file quá 50 MB, bot không gửi được.")
    chat = os.environ.get("TELEGRAM_CHAT_ID", "").strip()
    if not chat:
        sys.exit("Lỗi: chưa có biến TELEGRAM_CHAT_ID. Chạy --lay-chat-id để lấy.")

    ranh_gioi = uuid.uuid4().hex
    phan = []
    for ten, gt in (("chat_id", chat), ("caption", f"Tin bóng đá {p.stem[:10]}")):
        phan.append(f'--{ranh_gioi}\r\nContent-Disposition: form-data; name="{ten}"\r\n\r\n{gt}\r\n'.encode())
    phan.append(
        f'--{ranh_gioi}\r\nContent-Disposition: form-data; name="document"; filename="{p.name}"\r\n'
        "Content-Type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet\r\n\r\n".encode()
        + p.read_bytes() + b"\r\n")
    phan.append(f"--{ranh_gioi}--\r\n".encode())
    goi("sendDocument", b"".join(phan),
        {"Content-Type": f"multipart/form-data; boundary={ranh_gioi}"})
    print(f"Đã gửi {p.name} vào Telegram.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    lay_chat_id() if sys.argv[1] == "--lay-chat-id" else gui(sys.argv[1])
