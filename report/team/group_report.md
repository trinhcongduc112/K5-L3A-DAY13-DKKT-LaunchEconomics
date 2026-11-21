# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: DKKT
- Lớp: L3A
- Thành viên: xem `TEAM.md` (Trịnh Công Đức, Nguyễn Vũ Khanh, Phạm Quang Trường, Nguyễn Tuấn Kiệt)

## 2. Mục tiêu và cách tiếp cận

Dựng bộ hồ sơ launch v0 cho trợ lý hoàn phí của LogiX-VN từ dữ liệu giả lập đợt chạy thử (1.200 yêu cầu, 1.624 lần chạy) để bảo vệ kế hoạch pilot trước hội đồng Gate 2a. Nhóm chia bốn vai độc lập theo `TEAM.md`, mỗi file có đúng một người phụ trách: xây dựng mô hình chi phí thực trên mỗi việc thành công và bảng độ nhạy bằng `src/lab13.py` (có người kiểm số tính độc lập để đối chiếu), phân loại 20 ca lỗi theo khung Google PAIR kèm bảng khắc phục 5 ca, thiết kế kế hoạch pilot có đối chứng và luật dừng bằng `pilot_plan.yaml`, và đặc tả hệ thống chỉ số, event, rủi ro kinh tế để tổng hợp vào hồ sơ một trang `ho_so_launch_v0.md`.

## 3. Giải pháp

Tóm tắt cách nhóm làm từng nhiệm vụ A–E và link tới file hồ sơ tương ứng.

- **Nhiệm vụ A & B (Mô hình chi phí và bảng độ nhạy):** Viết `src/lab13.py` qua đủ 3 phép thử A1 (`1,20 · 1,25 · 1,25`), tính chi phí từ trace (A2), tách theo 4 loại yêu cầu và lần thử (A3), cộng chi phí cố định 40 triệu đ/tháng (A4), chạy 9 kịch bản đơn biến (B1), 1 kịch bản đổi cặp (B2), chi phí cả hệ thống theo giới hạn 1–3 lần chạy (B3) và kịch bản xem lại 100% (B4). Chi tiết: [bang_chi_phi.md](bang_chi_phi.md).
- **Nhiệm vụ C (Bảng lỗi và cách khắc phục):** Hai người gắn nhãn 20 ca lỗi trong 8 phút (đồng thuận 20/20 = 100%, có khai báo trung thực cách dùng công cụ AI hỗ trợ), viết quy tắc phân biệt các ca dễ lẫn và lập bảng khắc phục cho 5 ca đại diện đủ 5 loại (ca 1, 7, 18, 4, 17) với event, ngưỡng đo và chức danh phụ trách riêng. Chi tiết: [bang_loi.md](bang_loi.md).
- **Nhiệm vụ D (Kế hoạch pilot):** Tính 5 câu cỡ mẫu D1 và tỉ lệ `mo_lai_trong_7_ngay` hiện tại bằng `src/lab13.py`, trả lời 5 câu kiểm tra tách tác động D2, chọn chia ngẫu nhiên theo nhân viên (`20 + 20`), chấp nhận nâng MDE lên `0,06` (`m >= 299`, `DE = 6,96`) và viết 3 luật dừng đủ 4 vế `NẾU – TRONG – THÌ – KHÔNG THÌ`. Chi tiết: [pilot_plan.yaml](pilot_plan.yaml).
- **Nhiệm vụ E (Chỉ số, event, rủi ro kinh tế và hồ sơ launch v0):** Tính thử 3 chỉ số trên 1.200 yêu cầu, đề xuất thêm 1 chỉ số dùng và 1 chỉ số an toàn, lập 3 dòng rủi ro kinh tế lấy số từ bảng độ nhạy (đang hoàn thiện danh sách event ở bước 23) tại [chi_so.md](chi_so.md) và tổng hợp vào hồ sơ một trang [ho_so_launch_v0.md](ho_so_launch_v0.md).

## 4. Kết quả

Con số chính (ghi nhãn `simulated` khi cần) và đề xuất cuối của `ho_so_launch_v0.md`. Kết quả duyệt chéo nhóm nhận được từ hội đồng.

- **Chi phí mỗi việc thành công (A2–A4):** Toàn mẫu là **4.472 đ/việc** (`simulated`), gấp **16,3 lần** hoá đơn token + tool chia số yêu cầu (`274,7 đ`); làm lại (`51,8%`) và xem lại (`40,7%`) chiếm **92,5%** tổng chi phí (`simulated`). Tính cả hệ thống (thêm 222 ca nhân viên làm thay × 12.000 đ) là **5.865 đ/yêu cầu = 0,49×** (`simulated`). Thu hẹp phạm vi pilot về `noi_dia` (`2.696 đ = 0,22×`, `simulated`) và `hang_nang` (`8.221 đ = 0,69×`, `simulated`), loại `quoc_te` (`22.515 đ = 1,88×`, thành công `27,3%`, `simulated`) và `doi_tac` (`10.215 đ = 0,85×`, `simulated`); cộng chi phí cố định 40 triệu đ/tháng ra **4.599 đ = 0,38×** ở 45.000 yêu cầu/tháng và **5.784 đ = 0,48×** ở nửa khối lượng (`simulated`).
- **Độ nhạy & Giới hạn chạy lại (B1–B4):** Ba yếu tố nhạy nhất là **Số ca làm lại** (`+51,8% / -25,9%`, `simulated`), **Tỉ lệ xem lại** (`+40,7% / -20,3%`, `simulated`) và **Lương nhân viên** (`+23,1%`, `simulated`). Giới hạn **2 lần chạy** rẻ nhất cho cả hệ thống (**6.901.220 đ**, `simulated`). Kịch bản xem lại 100% làm chi phí vọt lên **11.743 đ = 0,98×** (9 phút làm lại) đến **12.414 đ = 1,03×** (15,3 phút làm lại trung bình dữ liệu, `simulated`).
- **Chỉ số & Cỡ mẫu (D1, E1):** Chỉ số trong đợt chạy thử (chưa có đối chứng): Chính **82,83%** (`994/1.200`), Dùng - bỏ qua gợi ý **27,12%** (`48/177`), An toàn - mở lại trong 7 ngày **4,25%** (`51/1.200`; trong phạm vi là `3,97%`). Cỡ mẫu theo nhân viên `20 + 20` có trần hiệu dụng `1.000 < 1.251` nên chọn `MDE = 0,06` (`n_per_arm = 859`, `m >= 299`, `DE = 6,96`).
- **Đề xuất cuối của `ho_so_launch_v0.md`:** *(Đang chờ chốt ở bước 28 lúc 16:45.)*
- **Kết quả duyệt chéo từ hội đồng:** *(Điền sau 17:40 ở bước 35.)*

## 5. Khó khăn và cách xử lý

- *(Bản nháp — hoàn thiện chi tiết ở bước 35 lúc 17:00–17:40: cập nhật thêm khó khăn về khai báo dùng AI hỗ trợ ở nhiệm vụ C, đánh đổi MDE 5 điểm → 6 điểm khi chỉ có 40 nhân viên, và phối hợp Git theo lượt sửa `src/lab13.py`.)*

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md` *(sẽ tổng hợp thêm 3 dòng đóng góp của từng thành viên ở bước 37 lúc 17:50)*.

## 7. Hạn chế và hướng cải thiện

- *(Bản nháp — hoàn thiện chi tiết ở bước 35 lúc 17:00–17:40: số phút xem lại/làm lại hiện vẫn là `simulated` chiếm 92,5% chi phí; power thực tế tụt dưới 0,80 nếu tác động thật chỉ là +5 điểm; cần thay bằng thời gian đo thực tế qua event ngay tuần đầu pilot.)*

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, [arxiv.org/abs/2504.13359](https://arxiv.org/abs/2504.13359).
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure", [pair.withgoogle.com](https://pair.withgoogle.com).
- Tài liệu `statsmodels`, lớp `NormalIndPower` (mục `stats.power`), và tài liệu hướng dẫn Lab 13 AI20K K5.
