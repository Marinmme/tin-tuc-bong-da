---
name: tin-bong-da
description: Tổng hợp tin bóng đá trong ngày (drama cầu thủ, trận đấu, họp báo, chuyển nhượng) từ web, xuất một file Excel vào livrables/ rồi đẩy lên GitHub. Chỉ chạy khi chủ dự án yêu cầu (gõ /tin-bong-da hoặc "chạy tin bóng đá").
---

# Tổng hợp tin bóng đá → Excel

Chỉ chạy khi chủ dự án yêu cầu. Không tự hẹn giờ, không tự mở phiên.
Đọc `MAP.md` và `contexte/decisions.md` trước (danh sách giải, nhà báo, cầu thủ).

## Bước 1 — Tìm tin (24 giờ qua)

Dùng WebSearch, gửi nhiều truy vấn cùng lúc. Tối thiểu các nhóm:
- **Nhà báo top tier:** tin mới nhất của từng người trong `contexte/decisions.md` (vd "Fabrizio Romano here we go", "David Ornstein").
- **Drama cầu thủ:** Ronaldo, Messi, Yamal + cầu thủ khác trong `decisions.md`.
- **Trận đấu:** kết quả, lịch, diễn biến hôm qua/hôm nay của các giải ưu tiên.
- **Họp báo:** phát biểu HLV, cầu thủ trước/sau trận.
- **Chuyển nhượng:** tin chính thức và tin đồn.

Tin trên X/Facebook: lấy qua bài báo có trích lại bài đăng. Ghi nguồn gốc là người đăng (vd "Fabrizio Romano (X), qua Goal.com"), link là link bài báo.

## Bước 2 — Lọc và xác thực

- Chỉ giữ tin trong 24–48 giờ qua.
- **Xác thực** = CLB/giải/cầu thủ công bố chính thức, hoặc ít nhất 2 nguồn uy tín độc lập cùng đưa, hoặc nhà báo top tier xác nhận ("here we go", "done deal").
- Còn lại = **Tin đồn**.
- Không link = bỏ tin. Trùng tin = gộp, giữ nguồn tốt nhất.
- Không bịa. Không chắc thì ghi Tin đồn hoặc bỏ.
- Mục tiêu 15–30 tin.

## Bước 3 — Viết tóm tắt

- Tiếng Việt, 2–4 câu, tự viết lại, không chép nguyên văn.
- Nêu ai, chuyện gì, khi nào, nguồn nói gì.

## Bước 4 — Xuất Excel

Đưa JSON qua stdin (không tạo file tạm trong dự án):

```bash
python3 outils/xuat_excel.py <<'EOF'
[
  {"thoi_gian": "2026-11-27 08:00", "chu_de": "Chuyển nhượng",
   "tieu_de": "...", "tom_tat": "...", "nguon": "...",
   "link": "https://...", "trang_thai": "Xác thực"}
]
EOF
```

- `chu_de`: Drama | Trận đấu | Họp báo | Chuyển nhượng | Khác
- `trang_thai`: `Xác thực` hoặc `Tin đồn` (script tự thêm [TIN ĐỒN] và tô vàng)
- Script không ghi đè: file đã có thì tạo `_2`, `_3`.

## Bước 5 — Đẩy lên GitHub

```bash
git add livrables/
git commit -m "Tin bóng đá YYYY-MM-DD"
git push
```

Báo lại cho chủ dự án: số tin, số tin đồn, 3 tin nóng nhất, đường dẫn file.
