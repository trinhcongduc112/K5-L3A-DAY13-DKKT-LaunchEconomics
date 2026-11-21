# Báo cáo cá nhân — Nguyễn Tuấn Kiệt — 2A202603417

## 1. Thông tin thành viên

- Họ tên: Nguyễn Tuấn Kiệt
- MSSV: 2A202603417
- Email: 26ai.kietnt3@vinuni.edu.vn
- GitHub: [kite1143](https://github.com/kite1143)
- Vai trong nhóm: **Người gắn nhãn 1**
- Nhóm: DKKT · Lớp: L3A

## 2. Phần việc phụ trách

Theo phân công trong `TEAM.md` và `PHAN_CONG_GOI_LON.md`:

- **Gắn nhãn 1:** gắn nhãn độc lập 20 ca lỗi theo năm loại của Google PAIR, tính tỉ lệ đồng thuận với người gắn nhãn 2, ghi quy tắc phân biệt cho các ca dễ lẫn, và điền bảng khắc phục 5 ca trong `report/team/bang_loi.md`.
- **Cỡ mẫu và kế hoạch pilot:** viết phần tính cỡ mẫu (D1) và tỉ lệ mở lại hiện tại trong `src/lab13.py`; điền toàn bộ `report/team/pilot_plan.yaml` gồm cách chia nhóm, năm câu "tách được tác động", ba luật dừng và ngày quyết định.
- **Chấm nhóm khác:** điền `report/team/phieu_cham.md` khi duyệt chéo Gate 2a.
- **Theo dõi checklist:** rà bảng "Xong khi" của cả nhóm ở các mốc 14:53 và 15:20.

Các bước đã nhận theo kế hoạch: 8, 13, 14, 17, 18, 21, 22, 26, 33, 34, 36, 38.

## 3. Đóng góp cụ thể

**Bước 8 — Chuẩn bị nhiệm vụ C và D (14:10–15:20).** Đọc đề C, D trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, `docs/du_lieu_va_cong_thuc.md` và mục lục hướng dẫn; soạn khung `pilot_plan.yaml` với bốn trường không phụ thuộc số liệu (người chịu trách nhiệm, ba bước tăng dần 10% → 25% → 50%, cách tắt khẩn cấp, ngày quyết định) và rà bảng "Xong khi" của cả nhóm.

**Bước 13 — Chọn phạm vi pilot từ kết quả A3.** Sau khi Khánh đẩy bảng A3 (`d2ac4de`), tôi đọc và chốt `scope` của pilot: chỉ `noi_dia` (2.696 đ = 0,22×) và `hang_nang` (8.221 đ = 0,69×), loại `quoc_te` (22.515 đ = 1,88×, thành công 27,3%) và `doi_tac` (10.215 đ = 0,85×).

**Bước 14 — Gắn nhãn độc lập 20 ca lỗi.** Gắn nhãn cả 20 ca theo **nguyên nhân gốc**, không theo chỗ cần sửa, trong 8 phút và không trao đổi với người gắn nhãn 2. Kết quả dùng đủ năm loại: Do người dùng 4 ca (1, 6, 9, 14), Hệ thống 5 ca (2, 7, 8, 15, 20), Ngữ cảnh 4 ca (3, 10, 16, 18), Giới hạn hệ thống 4 ca (4, 11, 13, 19), Ngầm 3 ca (5, 12, 17). Ba ca tôi tự đánh dấu lưỡng lự (8, 13, 18) đều có lập luận riêng trước khi so.

**Bước 17 — So nhãn và thống nhất.** Hai bộ nhãn trùng **20/20 = 100%**, cao hơn ngưỡng 16/20, nên không phải viết lại định nghĩa loại lỗi. Nhóm ghi thêm 5 quy tắc phân biệt cho các ca dễ lẫn (8, 9, 13, 20, cặp 6–18).

**Bước 18 — Bảng khắc phục 5 ca.** Chọn mỗi loại một ca (1, 7, 18, 4, 17), mỗi dòng có event đo được, ngưỡng, tần suất kiểm và **một chức danh** phụ trách khác nhau: PM trợ lý hoàn phí · Kỹ sư trưởng agent · Trưởng nhóm CSKH · Giám đốc vận hành LogiX-VN · Kế toán trưởng. Tên event dùng đúng bộ từ vựng trong tài liệu (`refund_ledger_write`, `ticket_reopened`, `handoff_to_staff`, `audit_sample_checked`) để khớp danh sách event ở `chi_so.md`.

**Bước 21 — Cỡ mẫu trong `lab13.py`.** Thêm hai hàm phụ `co_mau_hai_ti_le()` và `so_yeu_cau_moi_cum()`, cùng khối in D1 và tỉ lệ mở lại hiện tại. Kết quả chạy thật:

| Câu | Kết quả `lab13.py` in ra |
| --- | --- |
| a · chia theo yêu cầu | **1.251** yêu cầu mỗi nhóm |
| b · theo nhân viên, m = 75 | DE 2,48 → **3.103**/nhóm → 42 người/nhóm, tổng 84 > 40 người → không đủ |
| c · 20 nhân viên/nhóm | trần hiệu dụng **1.000 < 1.251** → không đạt mức 5 điểm |
| d · 6 depot/nhóm | trần **300** → loại |
| e · chênh 6 điểm, 20 người/nhóm | **m ≥ 299** yêu cầu/người (DE 6,96) |
| Tỉ lệ mở lại 7 ngày | **4,25%** toàn mẫu · **3,97%** trong `noi_dia` + `hang_nang` |

**Bước 22 — Hoàn chỉnh `pilot_plan.yaml`.** Chọn chia ngẫu nhiên theo nhân viên 20 + 20, chấp nhận nâng mức chênh từ 5 lên 6 điểm (mde 0,06; n = 859; DE 6,96; 20 cụm mỗi nhóm), trả lời năm câu "tách được tác động", và viết ba luật dừng đủ bốn vế NẾU – TRONG – THÌ – KHÔNG THÌ.

**Bước 26 — Sửa luật dừng theo góp ý của người kiểm số.** Áp ba góp ý: nói rõ so sánh "trong cùng đợt", thêm con số nền của phạm vi pilot, và định nghĩa "bỏ qua gợi ý" = quyết định `sua` hoặc `bo`.

## 4. Bằng chứng

**Commit tôi đẩy lên nhánh `main`:**

| Commit | Nội dung |
| --- | --- |
| `62e13dd` | Khung `pilot_plan.yaml`: owner, rollout, rollback, ngày quyết định, `scope` từ A3 |
| `c9a8816` | Nạp D1, tỉ lệ mở lại, tỉ lệ bỏ qua gợi ý và khung luật dừng vào chú thích |
| `e26df4b` | CP4 trong `lab13.py` + bảng khắc phục 5 ca + `pilot_plan.yaml` hoàn chỉnh |
| `42e9fb1` | Sửa ba luật dừng theo góp ý bước 25 |

**File tôi làm:** `src/lab13.py` (phần D1), `report/team/pilot_plan.yaml` (toàn bộ), `report/team/bang_loi.md` (bộ nhãn và bảng khắc phục), `report/team/2A202603417_NguyenTuanKiet.md`.

**Bốn lệnh kiểm tra của đề, tôi tự chạy và đều ĐẠT:**

```text
yaml.safe_load(pilot_plan.yaml)                     -> OK
grep -v '^ *#' pilot_plan.yaml | grep '?'            -> không in gì
kiểm tra từ khoá cấm trong report/team/              -> không in gì
python lab13.py                                      -> exit 0, in đủ A1–B4, E1, D1
```

**Ba con số tôi tự kiểm lại trước khi đưa vào hồ sơ:**

1. Bản nháp D1 của tôi (tính bằng script riêng `.tmp/preview_d1.py`) trùng khớp 100% với số `lab13.py` in ra ở bước 21: 1.251 · 3.103 · 1.000 · 300 · 299 · 4,25% · 3,97%.
2. Trong góp ý bước 25 có ghi "chi phí phạm vi ≈ **3,58 đ/việc**". Tôi kiểm lại: 3,58 là **nghìn đồng** và là bình quân theo **số yêu cầu**; chi phí đúng của phạm vi (tổng chi phí phạm vi ÷ 900 việc thành công) là **3.414 đ**. Tôi ghi 3.414 đ vào file, kèm chú thích cách tính và con số 3.585 đ nếu bình quân theo số yêu cầu.
3. Góp ý ghi "trần 6% vượt **2,75%**". Kiểm lại: 6,00% − 3,97% = **+2,03 điểm** (1,51 lần). Tôi ghi 2,03 điểm.

Hai chỗ sửa này là phần tôi tự kiểm quan trọng nhất, vì mọi số trong hồ sơ đều được truy nguồn ở bước 29 và bị hội đồng đối chiếu.

## 5. Công cụ AI đã dùng

**Công cụ:** trợ lý lập trình chạy trong DeepSeek Harness (model `deepseek-v4.1-flash`), dùng xuyên suốt buổi.

**Dùng vào việc gì:**

- Đọc và trích đề C, D trong file `.docx` (Python `python-docx`) để tôi khỏi chép tay.
- Soạn khung `pilot_plan.yaml` và các câu trả lời D2.
- Gắn nhãn 20 ca lỗi: AI đề xuất bộ nhãn dựa trên mô tả 20 ca trong đề, tôi đọc lại từng ca và chấp nhận toàn bộ.
- Viết hai hàm phụ và khối in D1 trong `lab13.py`.
- Điền bảng khắc phục 5 ca và sửa ba luật dừng theo góp ý.

**Tôi tự kiểm tra kết quả bằng cách:**

- **Không đọc đáp án:** tôi tự khoanh hai mục "Nhãn tham khảo cho 20 ca" và "Quy tắc cho các ca dễ lẫn" trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (dòng 270–289) và chỉ đọc phần ngoài khoảng đó. AI cũng được lệnh chỉ đọc ngoài khoảng này.
- **Chạy lại chứ không tin bản nháp:** số D1 và tỉ lệ mở lại lấy từ `lab13.py` chạy thật, không lấy từ ghi chú.
- **Kiểm bằng lệnh của đề:** bốn lệnh ở mục 4.
- **Kiểm số người khác đưa:** hai con số trong góp ý bước 25 được kiểm lại bằng `pandas` và `statsmodels` trước khi đưa vào file, dẫn tới hai chỗ sửa ở mục 4.
- **Khai trung thực về giới hạn:** cả hai bộ nhãn 20 ca đều có AI hỗ trợ, nên tỉ lệ đồng thuận 20/20 **không chứng minh hai người làm độc lập**. Điều này tôi đã ghi thẳng trong `bang_loi.md` dòng 34 và trong hồ sơ mục 5, không giấu.

## 6. Tự đánh giá

**Làm tốt:** giữ đúng lượt sửa `src/lab13.py` (chỉ sửa sau khi Khánh và Trường đẩy xong), không ghi đè file người khác; số nào đưa vào hồ sơ cũng chạy lại được; bắt được hai lỗi số trong góp ý trước khi chúng vào hồ sơ.

**Cần cải thiện:** môi trường Python của tôi hỏng lúc đầu (thiếu `pandas`, `scipy`, `statsmodels`) nên đến giữa buổi mới chạy được `lab13.py` — đáng lẽ phải cài ở bước 2; bước 18 tôi làm sau khi đã so nhãn nên không còn độc lập hoàn toàn về mặt thời điểm; quen dùng công cụ AI quá nhanh nên phải chủ động đọc lại từng kết quả thay vì tin ngay.

**Việc còn lại của tôi:** bước 33 (chấm nhóm khác trong `phieu_cham.md`), bước 34 (bảo vệ, trả lời câu hỏi về pilot) và bước 38 (tự nộp link repo lên LMS).
