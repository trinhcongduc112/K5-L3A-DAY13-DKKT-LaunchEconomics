# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51/1.200) |
| Dùng | Nhóm tự đề xuất: % yêu cầu của nhân viên nhóm can thiệp được xử lý bằng trợ lý | số yêu cầu có ít nhất một `agent_run_completed` ÷ tổng yêu cầu của nhóm can thiệp | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai tiền phát hiện qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm) | số đơn có `so_tien_da_hoan` ≠ `so_tien_dung` ÷ số đơn được kiểm tra mẫu | Không cần tính |

Chỉ số trong đợt chạy thử là **82,83%** (chính), **27,12%** (dùng), **4,25%** (an toàn). Không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- ...

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | Chi phí mỗi việc thành công tăng **+51,8%**, từ 4.472 đ lên **6.787 đ** (`simulated`) | Tỉ lệ ca làm lại theo tuần > **7%** (đợt chạy thử trong phạm vi `noi_dia` + `hang_nang` là 4,9% = 48/982) | Thu hẹp phạm vi về chỉ còn `noi_dia`, giữ giới hạn tối đa 2 lần chạy (B3: chi phí cả hệ thống thấp nhất **6.901.220 đ**, `simulated`) và rà soát 20 trace làm lại | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài sang các tuần sau | Chi phí mỗi việc thành công trong phạm vi `noi_dia` + `hang_nang` tăng lên **11.743 đ = 0,98×** của 12.000 đ (với 9 phút làm lại) hoặc **12.414 đ = 1,03×** (với 15,3 phút làm lại trung bình từ dữ liệu, `simulated`) | Tỉ lệ yêu cầu được xem lại vẫn > **50%** ở cuối bước rollout 0,25 hoặc thời gian xem lại đo thật > **4,8 phút/ca** | Giảm tỉ lệ xem lại theo bậc đối với nhóm đơn `noi_dia` khi tỉ lệ `sua` + `bo` < 15% và tối ưu giao diện để rút thời gian xem lại dưới 4,8 phút/ca | Trưởng nhóm CSKH |
| Khối lượng yêu cầu thực tế thấp hơn dự kiến | Chi phí cố định 40 triệu đ/tháng cộng **+1.185 đ/việc** ở 45.000 yêu cầu/tháng (tổng **4.599 đ = 0,38×**, `simulated`), tăng lên **+2.370 đ/việc** ở một nửa khối lượng (tổng **5.784 đ = 0,48×**, `simulated`) và vượt 12.000 đ nếu dưới 4.663 việc thành công/tháng | Số việc thành công mỗi tuần < **50%** kế hoạch phân bổ theo số nhân viên | Không mở rộng sang bước rollout tiếp theo và đàm phán lại cấu trúc chi phí vận hành cố định theo bậc khối lượng | Giám đốc vận hành LogiX-VN |
