# Nhật ký quyết định

Mỗi quyết định: ngày, nội dung, lý do. Mới nhất ở trên cùng.

---

## 2026-11-27 — Cách chạy tool

**Quyết định:**
- Chạy trên Claude, **chỉ khi chủ dự án yêu cầu**. Không lịch hẹn, không tự mở phiên. (Thay mặc định "6:00 sáng tự chạy".)
- Nguồn miễn phí: WebSearch của Claude. Tin X/FB lấy qua bài báo trích lại. Không mua X API.
- Kết quả đẩy lên một repo GitHub.
**Lý do:** chủ dự án chọn; tránh phí API (~200 USD/tháng). Máy cloud chặn RSS (Google News, BBC) nên không dùng RSS.

---

## 2026-11-27 — Thu hẹp phạm vi: chỉ xuất Excel

**Quyết định:** tool chỉ tổng hợp tin, xuất một file Excel mỗi ngày. Bỏ kịch bản video, bỏ file Markdown.
**Lý do:** chủ dự án xác nhận tool không dùng để tạo video.
**Hệ quả:** bỏ các mặc định về giọng văn và độ dài video ở mục dưới.

---

## 2026-11-27 — Khởi tạo dự án

**Đã chốt (từ chủ dự án):**
- Mục tiêu: tool tìm tin bóng đá (drama, trận đấu, họp báo, ...).
- Người dùng: chủ dự án tự dùng, để làm video YouTube.
- Đầu ra: list tin + link, tóm tắt tiếng Việt, kịch bản video, file Markdown/Excel mỗi ngày.
- Nguồn: X, Facebook, nhà báo top tier.
- Lịch chạy: tự động mỗi buổi sáng.
- Luật: chỉ tin xác thực, tin đồn ghi rõ; không đạo văn; ưu tiên drama cầu thủ (Ronaldo, Messi, Yamal, ...).

**Mặc định tạm — CHỜ XÁC NHẬN** (chủ dự án chưa chọn cụ thể):
- Giọng kịch bản: sôi nổi, cuốn hút, nhưng không bịa, không giật tít sai sự thật.
- Độ dài video: 8–10 phút (~1.200–1.500 chữ kịch bản).
- Giải ưu tiên: Premier League, La Liga, Champions League, Serie A, Bundesliga, V-League, Saudi Pro League (vì Ronaldo), MLS (vì Messi).
- Nhà báo top tier: Fabrizio Romano, David Ornstein, Gianluca Di Marzio, Matteo Moretti, Florian Plettenberg, Sami Mokbel.
- Giờ chạy: 6:00 sáng giờ Việt Nam.

**Lý do:** cần mặc định để bắt đầu; sửa khi chủ dự án xác nhận.
