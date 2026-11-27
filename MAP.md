# MAP.md — Bản đồ dự án

> Đọc file này trước khi làm việc. Cập nhật ngay khi cấu trúc thay đổi.

```
/
├── CLAUDE.md          Hướng dẫn + quy tắc dự án cho Claude
├── MAP.md             Bản đồ này
├── .gitignore         Bỏ qua __pycache__
├── .claude/skills/tin-bong-da/
│   └── SKILL.md       Quy trình /tin-bong-da: tìm → lọc → tóm tắt → Excel → GitHub → Telegram
├── outils/
│   ├── xuat_excel.py  JSON (stdin) → Excel trong livrables/, không ghi đè
│   └── gui_telegram.py Gửi file Excel vào Telegram qua bot
├── contexte/          Bối cảnh + quyết định quan trọng
│   └── decisions.md   Nhật ký quyết định (ngày, nội dung, lý do)
└── livrables/         File Excel tin tức mỗi ngày
```

## Quy ước đặt tên trong `livrables/`
- `YYYY-MM-DD_tin-bong-da.xlsx` — bảng tin trong ngày

## Lịch sử thay đổi cấu trúc
- 2026-11-27: Thêm `outils/gui_telegram.py` (gửi Telegram).
- 2026-11-27: Thêm skill `tin-bong-da` và `outils/xuat_excel.py`.
- 2026-11-27: Khởi tạo dự án (CLAUDE.md, MAP.md, contexte/, livrables/).
