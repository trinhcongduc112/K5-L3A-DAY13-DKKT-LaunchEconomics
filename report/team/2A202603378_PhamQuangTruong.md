# Báo cáo cá nhân — HoVaTen-MSSV

Copy file này và đổi tên theo quy tắc `MSSV_HoTen.md`. Giữ nguyên file mẫu.

Ví dụ: `20241234_NguyenVanAn.md`.

## 1. Thông tin thành viên

- Họ tên: Phạm Quang Trường
- MSSV: 2A202603378
- Email: truongpham090325@gmail.com
- Vai trong nhóm: Người kiểm số.

## 2. Phần việc phụ trách

Phụ trách phần Kiểm số (Giai đoạn 1): tự tính lại số của Khánh để kiểm, tính các chỉ số đo lường/event, kiểm số trong hồ sơ, kiểm ngưỡng luật dừng, nội dung gửi Khánh và cả nhóm.

## 3. Đóng góp cụ thể

- Bước 7: tự tính độc lập 15 khoản (token, tool, lần chạy 2–3, xem lại, làm lại, tổng chi phí, việc thành công, CPS mỗi việc thành công, hoá đơn chia yêu cầu, CPS theo 4 loại) → so số với số của Khánh, lệch 0,0% (bảng ở mục 4).
- Bước 15+19: thêm E1 vào `lab13.py` (chính 82,83% / dùng 27,12% / an toàn 4,25%) và `chi_so.md` (3 chỉ số + 2 chỉ số tự đề xuất).
- Bước 23: 10 event có `trace_id`, kiểm chéo 5 chỉ số-event; Bước 25: kiểm ngưỡng luật dừng (an toàn 6% > 4,25%, chi phí ~3,5 đ < 6,700 đ, bỏ qua gợi ý 27,12% < 40%); Bước 29: truy nguồn mọi số trong `ho_so_launch_v0.md`.

## 4. Bằng chứng

### Kiểm số bước 11 — so số tự tính (bước 7) với số của Khánh (bước 6)

Tự tính độc lập bằng script `src/kiem_so_truong.py` (đọc thẳng hai CSV, không nhìn code của Khánh), rồi đối chiếu với `src/lab13.py` và `report/team/bang_chi_phi.md` của Khánh. Đã chạy `python lab13.py` của Khánh xác nhận code in ra đúng các số dưới đây.

| Khoản | Số mình tính | Số của Khánh | Độ lệch |
| --- | ---: | ---: | ---: |
| Token | 245.585 | 245.585 | 0,0% |
| Tool | 84.000 | 84.000 | 0,0% |
| Phần lần chạy thứ 2–3 | 93.804 | 93.804 | 0,0% |
| Xem lại (`simulated`) | 1.780.000 | 1.780.000 | 0,0% |
| Làm lại (`simulated`) | 2.264.000 | 2.264.000 | 0,0% |
| Tổng chi phí | 4.373.585 | 4.373.585 | 0,0% |
| Số việc thành công | 978 | 978 | 0,0% |
| Chi phí mỗi việc thành công (`simulated`) | 4.472 | 4.472 | 0,0% |
| Hoá đơn token + tool chia số yêu cầu | 274,7 | 274,7 | 0,0% |
| CPS loại `noi_dia` (`simulated`) | 2.696 | 2.696 | 0,0% |
| CPS loại `hang_nang` (`simulated`) | 8.221 | 8.221 | 0,0% |
| CPS loại `quoc_te` (`simulated`) | 22.515 | 22.515 | 0,0% |
| CPS loại `doi_tac` (`simulated`) | 10.215 | 10.215 | 0,0% |
| B1 · Giá token gấp đôi (`simulated`) | 4.723 (+5,6%) | 4.723 (+5,6%) | 0,0% |
| B3 · Cả hệ thống, giới hạn 2 lần chạy (`simulated`) | 6.901.220 | 6.901.220 | 0,0% |

Kết luận: mọi số khớp, độ lệch lớn nhất là **0,0%** (dưới ngưỡng 2%). Không cần báo Khánh sửa.

## 5. Công cụ AI đã dùng

Công cụ AI đã dùng: AI agent đang hỗ trợ bạn để đọc/phân tích bài thực hành; giúp dựng script tự tính `src/kiem_so_truong.py` (lấy số từ hai CSV); giúp dựng gợi ý cho Kiệt.
Cách tự kiểm: chạy script và so sánh với công thức tài liệu đối chiếu, cộng với chạy lại `lab13.py`; khớp 100% ở bước 11.

## 6. Tự đánh giá

Thực hiện đầy đủ 7 bước của phần Kiểm số (7, 11, 15, 19, 23, 25, 29). So số mình với Khánh/Đức đều khớp: lệch 0,0% ở bước 11, không cần báo sửa. Đề xuất cải thiện luật an toàn của Kiệt giải thích độ chênh thực (an toàn 3,97% cách trần ~2 điểm); cần đo thực tế dữ liệu pilot khi vào rollout.
