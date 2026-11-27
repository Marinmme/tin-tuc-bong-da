"""Xuất danh sách tin bóng đá (JSON từ stdin) ra file Excel trong livrables/.

Cách dùng:
    python3 outils/xuat_excel.py < tin.json
    python3 outils/xuat_excel.py --ngay 2026-11-27 < tin.json

JSON đầu vào: danh sách object, mỗi object có các khóa
    chu_de, tieu_de, tom_tat, nguon, link, trang_thai, thoi_gian (tùy chọn)
trang_thai chỉ nhận: "Xác thực" hoặc "Tin đồn".

Không bao giờ ghi đè: nếu file của ngày đã có, tạo bản _2, _3, ...
"""
import argparse
import json
import sys
from datetime import date
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill

THU_MUC = Path(__file__).resolve().parent.parent / "livrables"
COT = [
    ("STT", 6),
    ("Thời gian", 18),
    ("Chủ đề", 16),
    ("Tiêu đề", 45),
    ("Tóm tắt tiếng Việt", 70),
    ("Nguồn", 22),
    ("Link", 50),
    ("Trạng thái", 12),
]
TRANG_THAI_HOP_LE = {"Xác thực", "Tin đồn"}
MAU_TIN_DON = PatternFill("solid", fgColor="FFF2CC")


def kiem_tra(tin: list) -> None:
    if not isinstance(tin, list) or not tin:
        sys.exit("Lỗi: JSON phải là danh sách tin, không rỗng.")
    for i, t in enumerate(tin, 1):
        for khoa in ("chu_de", "tieu_de", "tom_tat", "nguon", "link", "trang_thai"):
            if not str(t.get(khoa, "")).strip():
                sys.exit(f"Lỗi: tin {i} thiếu '{khoa}'.")
        if not t["link"].startswith(("http://", "https://")):
            sys.exit(f"Lỗi: tin {i} link không hợp lệ: {t['link']}")
        if t["trang_thai"] not in TRANG_THAI_HOP_LE:
            sys.exit(f"Lỗi: tin {i} trạng thái phải là {TRANG_THAI_HOP_LE}.")


def duong_dan_moi(ngay: str) -> Path:
    goc = THU_MUC / f"{ngay}_tin-bong-da.xlsx"
    if not goc.exists():
        return goc
    n = 2
    while (p := THU_MUC / f"{ngay}_tin-bong-da_{n}.xlsx").exists():
        n += 1
    return p


def xuat(tin: list, ngay: str) -> Path:
    wb = Workbook()
    ws = wb.active
    ws.title = ngay
    for c, (ten, rong) in enumerate(COT, 1):
        o = ws.cell(row=1, column=c, value=ten)
        o.font = Font(bold=True, color="FFFFFF")
        o.fill = PatternFill("solid", fgColor="1F4E78")
        ws.column_dimensions[o.column_letter].width = rong
    ws.freeze_panes = "A2"

    for r, t in enumerate(tin, 2):
        tieu_de = t["tieu_de"]
        if t["trang_thai"] == "Tin đồn" and not tieu_de.startswith("[TIN ĐỒN]"):
            tieu_de = f"[TIN ĐỒN] {tieu_de}"
        gia_tri = [r - 1, t.get("thoi_gian", ""), t["chu_de"], tieu_de,
                   t["tom_tat"], t["nguon"], t["link"], t["trang_thai"]]
        for c, v in enumerate(gia_tri, 1):
            o = ws.cell(row=r, column=c, value=v)
            o.alignment = Alignment(wrap_text=True, vertical="top")
            if t["trang_thai"] == "Tin đồn":
                o.fill = MAU_TIN_DON
        ws.cell(row=r, column=7).hyperlink = t["link"]
        ws.cell(row=r, column=7).font = Font(color="0563C1", underline="single")

    ws.auto_filter.ref = ws.dimensions
    THU_MUC.mkdir(exist_ok=True)
    p = duong_dan_moi(ngay)
    wb.save(p)
    return p


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ngay", default=date.today().isoformat())
    a = ap.parse_args()
    tin = json.load(sys.stdin)
    kiem_tra(tin)
    p = xuat(tin, a.ngay)
    print(f"Đã lưu {len(tin)} tin: {p}")


if __name__ == "__main__":
    main()
