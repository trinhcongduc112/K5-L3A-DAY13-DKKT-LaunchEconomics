# Báo cáo cá nhân — TrinhCongDuc-2A202603527

## 1. Thông tin thành viên

- Họ tên: Trịnh Công Đức
- MSSV: 2A202603527
- Email: 26ai.ductc2@vinuni.edu.vn
- Vai trong nhóm: Trưởng nhóm · Người gắn nhãn 2, kiêm giữ hồ sơ

## 2. Phần việc phụ trách

- **Trưởng nhóm:** mời các thành viên vào repo nhóm, điều phối giờ giấc và các lần gặp nhau, theo dõi ai đang chờ ai, gửi hồ sơ cho nhóm hội đồng lúc 17:00.
- **Người gắn nhãn 2:** bộ nhãn người 2 cho 20 ca lỗi, so với bộ nhãn của người gắn nhãn 1 (Kiệt), tính tỉ lệ đồng thuận và ghi quy tắc phân biệt trong `report/team/bang_loi.md`.
- **Giữ hồ sơ:** `TEAM.md` và `report/team/ho_so_launch_v0.md` (bảy mục và dòng đề xuất cuối); trình bày và trả lời hội đồng khi duyệt chéo.

## 3. Đóng góp cụ thể

- Điền `TEAM.md`: thông tin nhóm, bảng thành viên, phần việc từng người (commit `4071c14`).
- Điền `report/team/bang_loi.md`: hai bộ nhãn, tỉ lệ đồng thuận **20/20 = 100%**, quy tắc phân biệt cho các ca khó 6, 8, 9, 13, 18, 20, và đoạn khai nguồn nhãn (commit `4071c14`).
- Điền `report/team/ho_so_launch_v0.md`: mục 1–3 và 7 từ `bang_chi_phi.md`, mục 4–6 từ `chi_so.md`, `bang_loi.md`, `pilot_plan.yaml`; đề xuất **Go có điều kiện** với bốn điều kiện, mỗi điều kiện có người phụ trách và ngày kiểm tra (commit `4071c14`, `899b29b`).
- Đưa ra đề xuất cuối dựa trên các con số bất lợi: xem lại 100% chỉ còn 0,98–1,03×, power 0,64 nếu tác động thật là 5 điểm, tỉ lệ mở lại 3,97% cách trần 6% khoảng 2 điểm, mọi số tiền dựa trên phút giả lập.
- **Điều phối nhóm:** tạo repo nhóm và cho cả ba thành viên quyền ghi (cả ba đều đã push lên repo); chốt bảng phân công 38 bước theo giờ và theo vai cho 4 người, được cả nhóm dùng làm mốc (các commit của nhóm ghi theo số bước); rà soát tiến độ các bước 1–29 trước khi chuyển sang bước duyệt chung và gửi hồ sơ; chốt cùng nhóm đề xuất cuối Go có điều kiện.

## 4. Bằng chứng

- Commit `4071c14` (`TEAM.md`, `bang_loi.md`, `ho_so_launch_v0.md` mục 1–3, 7) và `899b29b` (hồ sơ hoàn chỉnh) trên nhánh `main`.
- `report/team/bang_loi.md`: 20 ca, đồng thuận 20/20, bảng so nhãn cột người 1 và người 2.
- `report/team/ho_so_launch_v0.md`: đủ 7 mục, trạng thái đúng ba giá trị cho phép, người phụ trách đều là chức danh, không dùng từ bị cấm ở quy tắc 5 của lab.
- Kiểm số hồ sơ: chạy lại `src/lab13.py` và đối chiếu 26 con số chính trong hồ sơ (chi phí mỗi việc thành công, độ nhạy, ba chỉ số, hệ số thiết kế 6,96, power 0,64); cả 26 khớp với code.
- Power 0,64 và 0,80 tính bằng `statsmodels` (`NormalIndPower`, 859 yêu cầu mỗi nhóm, mức chênh 5 và 6 điểm).

## 5. Công cụ AI đã dùng

- **Claude Code (Claude)** dùng cho: lập kế hoạch phân công theo checkpoint; chạy lại `src/lab13.py` để kiểm số của Khánh; điền hồ sơ từ số trong `bang_chi_phi.md`, `chi_so.md`, `pilot_plan.yaml`; so hai bộ nhãn bằng code; tính power; soạn câu chữ cho quy tắc phân biệt và đề xuất cuối.
- **Bộ nhãn người 2 do AI gắn nháp, theo hướng dẫn của mentor** (mentor cho phép dùng AI gắn nhãn, nhóm chỉnh sửa sau). Vì Claude đã đọc file hướng dẫn có đáp án mẫu lúc lập kế hoạch, nên không tự gắn nhãn mà dùng một agent AI mới, chỉ được đọc đề và định nghĩa năm loại, không đọc đáp án. Kiệt cũng dùng AI cho bộ nhãn của mình (theo ghi chú của Kiệt), nên hai bộ nhãn trùng hoàn toàn và 100% này **không chứng minh hai người làm độc lập**; điều này đã được khai trong `bang_loi.md`.
- **Hướng dẫn của mentor về việc dùng AI gắn nhãn:** theo trao đổi của nhóm với mentor, mentor cho phép dùng AI gắn nhãn làm bản nháp và nhóm chỉnh sửa sau, vì nhóm không phải chuyên gia về gắn nhãn lỗi và đây là dự án để học cách làm việc.
- **Báo cáo cá nhân này:** bản nháp mục 6 (Tự đánh giá) và phần câu chữ do Claude Code soạn từ những gì đã kiểm được trong buổi lab; tôi đọc lại và xác minh từng thông tin trước khi nộp.
- **Cách tự kiểm tra kết quả của AI:** chạy lại `lab13.py` trong môi trường của mình; đối chiếu số trong hồ sơ với đầu ra của code (26/26 khớp); so hai bộ nhãn bằng code thay vì chép tay; đọc `yaml.safe_load` cho `pilot_plan.yaml`; `grep` kiểm không còn từ bị cấm ở quy tắc 5 và không còn dấu `?` ngoài chú thích.

## 6. Tự đánh giá

**Làm tốt.** Nhóm giữ đúng thứ tự checkpoint và mỗi file có một chủ riêng, nên các lần kéo bản mới của tôi (`git pull --rebase`) đều không xung đột. Số liệu được kiểm chéo: Trường tự tính lại 15 con số và lệch 0,0%; tôi đối chiếu 26 con số trong hồ sơ với đầu ra của `lab13.py` và cả 26 khớp. Đề xuất cuối là Go có điều kiện và nêu rõ các con số bất lợi (xem lại 100% chỉ còn 0,98–1,03×, power 0,64 nếu tác động thật là 5 điểm), thay vì chỉ trình bày kết quả đẹp.


