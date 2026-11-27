# CLAUDE.md — Tool tin bóng đá cho YouTube

## Mục tiêu
Tool tự động tổng hợp tin bóng đá mỗi sáng: drama cầu thủ, thông tin trận đấu, họp báo, chuyển nhượng.
Tool **chỉ tổng hợp tin**. Không viết kịch bản, không tạo video.

## Người dùng
Chủ dự án tự dùng, đọc tin để tham khảo làm nội dung YouTube.

## Sản phẩm đầu ra (mỗi ngày)
- **Một file Excel duy nhất**, đặt tên theo ngày (`YYYY-MM-DD`).
- Mỗi dòng là một tin: ngày, chủ đề, tiêu đề, tóm tắt tiếng Việt, nguồn, link, trạng thái (xác thực / tin đồn).

## Nguồn tin
- Tìm bằng công cụ WebSearch của Claude, miễn phí.
- Tin X/Facebook của nhà báo top tier (vd: Fabrizio Romano, David Ornstein) lấy qua bài báo có trích lại. Không dùng API trả phí.
- Danh sách nhà báo, giải, cầu thủ: `contexte/decisions.md`.

## Chủ đề ưu tiên
- Drama cầu thủ: Ronaldo, Messi, Yamal, ...
- Trận đấu, họp báo, chuyển nhượng.
- Giải đấu ưu tiên: xem `contexte/decisions.md`.

## Cách làm việc
- **Chỉ chạy khi chủ dự án yêu cầu** (gõ `/tin-bong-da`). Claude không tự mở phiên, không hẹn giờ.
- Quy trình: skill `.claude/skills/tin-bong-da/SKILL.md` → script `outils/xuat_excel.py` → file trong `livrables/` → đẩy lên GitHub.

## Quy tắc nội dung
- Chỉ đưa tin đã xác thực là tin thật. Tin đồn phải ghi rõ **[TIN ĐỒN]** + nguồn.
- Mỗi tin phải có link nguồn. Không link = không đưa.
- Không đạo văn. Viết lại bằng lời mình, không chép nguyên văn.

## Quy tắc làm việc cho Claude
1. **Đọc `MAP.md` trước** khi tìm hoặc tạo file. MAP.md là bản đồ chính thức của dự án.
2. **Cập nhật `MAP.md` ngay** mỗi khi thêm, xóa, đổi tên, di chuyển file hoặc thư mục.
3. **Lưu quyết định quan trọng** vào `contexte/decisions.md` (ngày, quyết định, lý do).
4. **Không tạo file thừa.** Chỉ tạo file khi thật cần.
5. **Không ghi đè dữ liệu có sẵn.** Đọc trước khi sửa. File trong `livrables/` cũ thì giữ nguyên.
