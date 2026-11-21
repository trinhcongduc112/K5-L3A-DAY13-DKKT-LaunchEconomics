# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Nguyễn Tuấn Kiệt · Người gắn nhãn 2: Trịnh Công Đức (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 20 / 20 = 100%

**Nguồn nhãn (khai trung thực):** người 1 (Kiệt) gắn với sự trợ giúp của công cụ AI và không đọc mục đáp án trong file hướng dẫn (theo ghi chú của Kiệt). Người 2 (Đức): bản nháp do một agent AI gắn theo hướng dẫn của mentor, agent không đọc đáp án mẫu; Đức rà soát và không đổi nhãn nào. Hai bộ nhãn trùng hoàn toàn, có thể do cùng loại công cụ, nên con số này không chứng minh hai người làm độc lập.

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

Hai bộ nhãn trùng 20/20 nên không có ca không trùng, và đồng thuận trên 80% nên không phải viết lại định nghĩa. Dưới đây là quy tắc cho các ca khó, nơi ít nhất một người ghi "chưa chắc", để rõ ranh giới giữa các loại:

- **Ca 8, Hệ thống (không phải Ngầm):** căn cứ "Điều 7.2" sai nằm ngay trong tin nhắn của trợ lý, đọc lại là thấy; Ngầm chỉ dùng khi lỗi chỉ lộ ra qua kiểm tra mẫu hoặc đối soát.
- **Ca 9, Do người dùng (không phải Giới hạn hệ thống):** nguyên nhân gốc là khách nhập mã đơn của sàn thay vì mã vận đơn; việc trợ lý báo "mã không hợp lệ" mà không gợi ý là chỗ cần cải thiện, ghi ở cột khắc phục.
- **Ca 13, Giới hạn hệ thống (không phải Hệ thống):** yêu cầu về bảo hiểm hàng hoá nằm ngoài phạm vi trợ lý nên không thể trả lời; việc trợ lý không nói rõ là hệ quả, xử lý ở cột khắc phục.
- **Ca 20, Hệ thống (không phải Do người dùng, không phải Ngầm):** lệnh hoàn thứ hai thiếu khoá chống trùng là vi phạm thiết kế; khách gửi lại sau 10 phút là hành vi bình thường, không phải đầu vào sai; ca không mô tả việc lỗi bị che khuất tới khi kiểm tra mẫu.
- **Ca 6 và ca 18:** đều là khách hiểu khác hệ thống nhưng khác gốc. Ca 6 khách chọn sai mục (Do người dùng); ca 18 trợ lý tính đúng, chỉ thiếu cách tính trong tin nhắn nên giả định "khách hiểu cách tính" không khớp (Ngữ cảnh).

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| ... | Do người dùng | ... | ... | ... |
| ... | Hệ thống | ... | ... | ... |
| ... | Ngữ cảnh | ... | ... | ... |
| ... | Giới hạn hệ thống | ... | ... | ... |
| ... | Ngầm | ... | ... | ... |
