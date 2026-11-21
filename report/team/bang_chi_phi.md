# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 | | có phần simulated |
| Số việc thành công | 978 | `ket_qua` | |
| Chi phí mỗi việc thành công | 4.472 | | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | | đo từ trace |

- Chi phí mỗi việc thành công gấp bao nhiêu lần "hoá đơn chia số yêu cầu"? Chi phí mỗi việc thành công là 4.472 đ (`simulated`), gấp **16,3 lần** hoá đơn chia số yêu cầu (274,7 đ). Tính cả hệ thống (thêm 222 ca không thành công × 12.000 đ) là 5.865 đ/yêu cầu = 0,49× của 12.000 đ (`simulated`).
- Khoản nào chiếm tỉ trọng lớn nhất trong tổng chi phí, bao nhiêu phần trăm? Khoản **làm lại** lớn nhất với 2.264.000 đ, chiếm **51,8%** tổng chi phí (`simulated`), tiếp theo là xem lại 40,7% (`simulated`); tổng giờ nhân viên chiếm 92,5%.

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ (`simulated`) | 0,22× (`simulated`) |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ (`simulated`) | 0,69× (`simulated`) |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ (`simulated`) | 1,88× (`simulated`) |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ (`simulated`) | 0,85× (`simulated`) |

- Loại nào không đáng để trợ lý xử lý? Với loại đó, cho chạy lại tới 3 lần có giúp không? Loại `quoc_te` không đáng để trợ lý xử lý (22.515 đ = 1,88×, thành công 27,3%, `simulated`). Chạy lại tới 3 lần không giúp (trung bình 2,32 lần/yêu cầu; tỉ lệ chạy `ok` giảm từ 30,0% ở lần 1 xuống 11,4% ở lần 2 và 2,2% ở lần 3); nên loại cả `doi_tac` (0,85×, `simulated`) khỏi pilot.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ (`simulated`) | 0,38× (`simulated`) |
| Một nửa khối lượng | 16.875 | 2.370 đ | 5.784 đ (`simulated`) | 0,48× (`simulated`) |

- Chi phí cố định có đổi kết luận không? Ở khối lượng nào? Không đổi kết luận ở quy mô đầy đủ 45.000 yêu cầu/tháng (4.599 đ = 0,38×, `simulated`) lẫn một nửa khối lượng (5.784 đ = 0,48×, `simulated`). Chi phí cố định chỉ làm tổng chi phí vượt 12.000 đ nếu khối lượng giảm xuống dưới 4.663 việc thành công/tháng.

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ (`simulated`) | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ (`simulated`) | -2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ (`simulated`) | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ (`simulated`) | -20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ (`simulated`) | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ (`simulated`) | -25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ (`simulated`) | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ (`simulated`) | -5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ (`simulated`) | -8,1% |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: 6.543 đ (`simulated`), tăng +46,3% so với gốc (bằng đúng tổng +5,6% + 40,7% vì mô hình cộng tuyến tính).
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. Số ca làm lại (+51,8% / -25,9%, `simulated`) · 2. Tỉ lệ xem lại (+40,7% / -20,3%, `simulated`) · 3. Lương nhân viên (+23,1%, `simulated`).

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ (`simulated`) | 319 | 7.449.781 đ (`simulated`) | 4.111 đ (`simulated`) |
| 2 lần | 4.093.220 đ (`simulated`) | 234 | 6.901.220 đ (`simulated`) | 4.237 đ (`simulated`) |
| 3 lần | 4.373.585 đ (`simulated`) | 222 | 7.037.585 đ (`simulated`) | 4.472 đ (`simulated`) |

- Giới hạn nào rẻ nhất cho công ty? Có trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất không? Giới hạn **2 lần chạy** rẻ nhất cho công ty (6.901.220 đ, `simulated`), **không trùng** với giới hạn có chi phí mỗi việc thành công thấp nhất (1 lần chạy: 4.111 đ, `simulated`) vì 1 lần đẩy thêm 85 việc sang nhân viên làm với giá 12.000 đ/việc.

## B4 · Nếu phải xem lại tất cả

- Chi phí mỗi việc thành công khi xem lại 100% (`noi_dia` + `hang_nang`), so với 12.000 đ: Với 9 phút làm lại/ca là **11.743 đ = 0,98×** của 12.000 đ (`simulated`, hoà vốn xem lại ≤ 5,1 phút/ca); với trung bình 15,3 phút làm lại/ca từ dữ liệu là **12.414 đ = 1,03×** (`simulated`, hoà vốn xem lại ≤ 4,8 phút/ca).
- Kết quả này nói gì về thứ pilot cần học được? Xem lại 100% gần như không tiết kiệm (0,98×–1,03×, `simulated`), nên pilot phải đo thời gian thực và kiểm chứng mức giảm tỉ lệ xem lại an toàn cũng như khả năng rút thời gian xem lại xuống dưới 4,8 phút/ca.
