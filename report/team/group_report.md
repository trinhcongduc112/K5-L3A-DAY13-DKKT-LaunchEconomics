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
- **Nhiệm vụ E (Chỉ số, event, rủi ro kinh tế và hồ sơ launch v0):** Tính thử 3 chỉ số trên 1.200 yêu cầu, đề xuất thêm 1 chỉ số dùng và 1 chỉ số an toàn, đặc tả 10 event có `trace_id` kèm kiểm tra chéo, lập 3 dòng rủi ro kinh tế lấy số từ bảng độ nhạy tại [chi_so.md](chi_so.md) và tổng hợp vào hồ sơ một trang [ho_so_launch_v0.md](ho_so_launch_v0.md).

## 4. Kết quả

Con số chính (ghi nhãn `simulated` khi cần) và đề xuất cuối của `ho_so_launch_v0.md`. Kết quả duyệt chéo nhóm nhận được từ hội đồng.

- **Chi phí mỗi việc thành công (A2–A4):** Toàn mẫu là **4.472 đ/việc** (`simulated`), gấp **16,3 lần** hoá đơn token + tool chia số yêu cầu (`274,7 đ`); làm lại (`51,8%`) và xem lại (`40,7%`) chiếm **92,5%** tổng chi phí (`simulated`). Tính cả hệ thống (thêm 222 ca nhân viên làm thay × 12.000 đ) là **5.865 đ/yêu cầu = 0,49×** (`simulated`). Thu hẹp phạm vi pilot về `noi_dia` (`2.696 đ = 0,22×`, `simulated`) và `hang_nang` (`8.221 đ = 0,69×`, `simulated`), loại `quoc_te` (`22.515 đ = 1,88×`, thành công `27,3%`, `simulated`) và `doi_tac` (`10.215 đ = 0,85×`, `simulated`); cộng chi phí cố định 40 triệu đ/tháng ra **4.599 đ = 0,38×** ở 45.000 yêu cầu/tháng và **5.784 đ = 0,48×** ở nửa khối lượng (`simulated`).
- **Độ nhạy & Giới hạn chạy lại (B1–B4):** Ba yếu tố nhạy nhất là **Số ca làm lại** (`+51,8% / -25,9%`, `simulated`), **Tỉ lệ xem lại** (`+40,7% / -20,3%`, `simulated`) và **Lương nhân viên** (`+23,1%`, `simulated`). Giới hạn **2 lần chạy** rẻ nhất cho cả hệ thống (**6.901.220 đ**, `simulated`). Kịch bản xem lại 100% làm chi phí vọt lên **11.743 đ = 0,98×** (9 phút làm lại) đến **12.414 đ = 1,03×** (15,3 phút làm lại trung bình dữ liệu, `simulated`).
- **Chỉ số & Cỡ mẫu (D1, E1):** Chỉ số trong đợt chạy thử (chưa có đối chứng): Chính **82,83%** (`994/1.200`), Dùng - bỏ qua gợi ý **27,12%** (`48/177`), An toàn - mở lại trong 7 ngày **4,25%** (`51/1.200`; trong phạm vi là `3,97%`). Cỡ mẫu theo nhân viên `20 + 20` có trần hiệu dụng `1.000 < 1.251` nên chọn `MDE = 0,06` (`n_per_arm = 859`, `m >= 299`, `DE = 6,96`, power còn `0,64` nếu hiệu ứng thật là +5 điểm).
- **Đề xuất cuối của `ho_so_launch_v0.md`:** **Go có điều kiện** cho pilot trong phạm vi `noi_dia` + `hang_nang`, kèm 4 điều kiện có người phụ trách và ngày kiểm tra (sửa khoá chống trùng & đối soát sổ cái trước 2026-12-04; ký chấp nhận MDE 6 điểm trước 2026-12-04; bật đủ 10 event đo thật thay số `simulated` sau tuần 1 trước 2026-12-14; thực hiện giảm xem lại theo bậc trước 2026-12-21).
- **Kết quả duyệt chéo từ hội đồng (nhóm ChuTichHungYen · L3A chấm DKKT):** Đạt **25/30 điểm** sơ bộ (**10/10** Đề xuất khớp bằng chứng · **10/10** Số giả lập và phạm vi · **5/10** Pilot ra được quyết định) với quyết định **Go có điều kiện**. Hội đồng ghi nhận phạm vi pilot và nhãn `simulated` chặt chẽ, nhưng yêu cầu làm rõ lịch thu đủ 299 yêu cầu/nhân viên (11.960 yêu cầu đủ điều kiện, chừa đủ 7 ngày theo dõi mở lại trước 05/01/2027), người kích hoạt từng luật dừng trong `pilot_plan.yaml`. **Trả lời câu hỏi của hội đồng:** Với 1.500 yêu cầu/ngày (81,8% thuộc `noi_dia` + `hang_nang`, tức ~1.227 yêu cầu/ngày), mỗi nhân viên xử lý trung bình **~215 yêu cầu đủ điều kiện/tuần**, nên ở bước rollout 0,50 (20 + 20 nhân viên) sẽ đạt `m >= 299` sau **~1,4 tuần** (cộng thêm 7 ngày theo dõi mở lại là đủ kịp mốc nếu kéo dài đo hết 2 tuần ở bước 0,50). Nếu đến hạn chốt mẫu vẫn thiếu 859 yêu cầu hiệu dụng mỗi nhánh (và chưa vi phạm luật dừng), nhóm sẽ gia hạn thêm 1 tuần thu mẫu thay vì ép kết luận; nếu hết thời hạn gia hạn vẫn thiếu thì kết luận chưa đủ bằng chứng (không mở rộng).

## 5. Khó khăn và cách xử lý

- **Giới hạn cỡ mẫu cụm (40 nhân viên, ICC 0,02):** Không cách chia theo cụm nào đạt 1.251 yêu cầu hiệu dụng/nhóm cho MDE 5 điểm; nhóm giải tường minh bất phương trình cụm chọn MDE 6 điểm (`m >= 299`) và khai báo rõ rủi ro power giảm còn 0,64 trong hồ sơ.
- **Khai báo trung thực dùng AI ở nhiệm vụ C & phối hợp Git:** Hai bộ nhãn lỗi trùng 20/20 do đều có công cụ AI hỗ trợ nên nhóm khai báo trung thực trong `bang_loi.md` thay vì coi là độc lập thuần tuý; đồng thời phân quyền 1 file 1 người chủ và chạy kiểm tra `src/lab13.py` sau mỗi lần đồng đội đẩy code để tránh xung đột.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md` *(sẽ cập nhật tóm tắt 3 dòng của mỗi thành viên khi chốt bài lúc 17:50)*.

## 7. Hạn chế và hướng cải thiện

- **Hạn chế:** Hai cột thời gian xem lại và làm lại chiếm 92,5% chi phí hiện vẫn là số `simulated`; thiết kế 20 + 20 nhân viên có power 0,64 ở mức 5 điểm; và theo góp ý của hội đồng ChuTichHungYen, lịch thu đủ 299 yêu cầu/nhân viên cần tính đủ 7 ngày cửa sổ theo dõi mở lại trước ngày quyết định 2027-01-05.
- **Hướng cải thiện:** Thu thập thời gian đo thật từ event `staff_review_decision` và `staff_rework_completed` ngay tuần 1 để hiệu chỉnh mô hình chi phí; cập nhật rõ lịch tích luỹ mẫu theo tuần và phương án dự phòng gia hạn nếu chưa đủ 859 yêu cầu hiệu dụng/nhóm vào `pilot_plan.yaml`.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, [arxiv.org/abs/2504.13359](https://arxiv.org/abs/2504.13359).
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure", [pair.withgoogle.com](https://pair.withgoogle.com).
- Tài liệu `statsmodels`, lớp `NormalIndPower` (mục `stats.power`), và tài liệu hướng dẫn Lab 13 AI20K K5.
