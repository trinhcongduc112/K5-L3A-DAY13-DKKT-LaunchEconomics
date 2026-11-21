# Báo cáo cá nhân — NguyenVuKhanh-2A202603427

Copy file này và đổi tên theo quy tắc `MSSV_HoTen.md`. Giữ nguyên file mẫu.

Ví dụ: `20241234_NguyenVanAn.md`.

## 1. Thông tin thành viên

- Họ tên: Nguyễn Vũ Khanh
- MSSV: 2A202603427
- Email: 26ai.khanhnv@vinuni.edu.vn
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người viết code

## 2. Phần việc phụ trách

- Dựng môi trường Python trong `src/`, viết phần A (A1–A4) và phần B (B1–B4) của `src/lab13.py`, điền `report/team/bang_chi_phi.md`.
- Trình bày cách hoạt động của hàm `mo_hinh` và giải thích quy tắc tử số/mẫu số cho cả nhóm trước khi bàn giao `src/lab13.py` cho Trường.
- Viết phần E2 (Rủi ro kinh tế) trong `report/team/chi_so.md`.
- Kéo code của đồng đội (Trường, Kiệt), chạy kiểm tra `src/lab13.py` từ đầu đến cuối trên máy mình; soạn và hoàn thiện `report/team/group_report.md`, chạy các lệnh kiểm tra cuối và push.

## 3. Đóng góp cụ thể

- **Nhiệm vụ A (A1–A4):** Cài đặt 3 hàm A1 (`so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`) đạt 3 phép thử (`1,20 · 1,25 · 1,25`). Viết hàm `mo_hinh()` đọc `logix_runs.csv` và `logix_requests.csv` (`keep_default_na=False`), tính A2 (`4.472 đ/việc`, `simulated`, gấp `16,3 lần` hoá đơn `274,7 đ`), tách 4 loại yêu cầu A3 kèm tỉ lệ `ok` theo `attempt`, và tính chi phí cố định 40 triệu đ/tháng A4 (`4.599 đ = 0,38×` ở 45.000 YC/tháng; `5.784 đ = 0,48×` ở nửa khối lượng, `simulated`).
- **Nhiệm vụ B (B1–B4):** Chạy 9 kịch bản độ nhạy B1, đổi cặp B2 (`6.543 đ`, `+46,3%`, `simulated`), xác định top 3 yếu tố nhạy nhất (Số ca làm lại · Tỉ lệ xem lại · Lương nhân viên), tính chi phí cả hệ thống B3 (giới hạn 2 lần chạy rẻ nhất: `6.901.220 đ`, `simulated`) và kịch bản xem lại 100% B4 (`11.743 đ = 0,98×` với 9 phút làm lại; `12.414 đ = 1,03×` với 15,3 phút làm lại, `simulated`). Điền đầy đủ bảng A1–A4 và B1–B4 vào `report/team/bang_chi_phi.md`.
- **Nhiệm vụ E2 & Báo cáo nhóm:** Viết 3 dòng rủi ro kinh tế (kèm dấu hiệu theo dõi, hành động và chức danh phụ trách) trong `report/team/chi_so.md`. Kiểm tra chạy lại toàn bộ `src/lab13.py` sau khi Trường (E1) và Kiệt (D1) đẩy code. Soạn và hoàn thiện `report/team/group_report.md` (bao gồm kết quả duyệt chéo `25/30` từ nhóm `ChuTichHungYen · L3A`, câu trả lời phản biện, khó khăn và hạn chế).

## 4. Bằng chứng

Commit, file, bảng hoặc con số do bạn làm.

- Commit `d2ac4de`: hoàn thành phần A và B trong `src/lab13.py` và `report/team/bang_chi_phi.md`.
- Commit `76225ce`: bổ sung bảng rủi ro kinh tế E2 trong `report/team/chi_so.md`.
- Commit `3c57588`: bản nháp `report/team/group_report.md` (và bản hoàn thiện sau duyệt chéo).
- Kết quả chạy `python lab13.py` trong `src/` in `Ba phép thử đáp án biết trước: ĐẠT`, `Tự kiểm tuyến tính B1: ĐẠT` cùng toàn bộ bảng A1–A4, B1–B4, E1, D1.

## 5. Công cụ AI đã dùng

Công cụ nào, dùng vào việc gì, bạn tự kiểm tra kết quả ra sao.

- Dùng trợ lý AI (Antigravity) để gợi ý cấu trúc code Python trong `src/lab13.py`, rà soát công thức và định dạng bảng Markdown trong `bang_chi_phi.md`, `chi_so.md`, `group_report.md`.
- Tự kiểm tra kết quả bằng cách chạy trực tiếp `python lab13.py` qua 3 phép thử A1 (`1,20 · 1,25 · 1,25`), kiểm tra tính chất tuyến tính B1/B2 (mỗi kịch bản giảm một nửa bằng đúng nửa mức tăng gấp đôi: `+5,6% / -2,8%`, `+40,7% / -20,3%`, `+51,8% / -25,9%`, đổi cặp `+46,3%`), đối chiếu số với đồng đội kiểm số (Trường), và chạy `yaml.safe_load` cùng kiểm tra từ cấm `"production"` trong `report/team/`.

## 6. Tự đánh giá

Hoàn thành đúng tiến độ và đầy đủ các đầu việc được phân công của vai Người viết code; toàn bộ con số đều xuất trực tiếp từ `src/lab13.py`, gắn nhãn `simulated` đầy đủ và khớp 100% với tiêu chí chấm điểm của rubric.
