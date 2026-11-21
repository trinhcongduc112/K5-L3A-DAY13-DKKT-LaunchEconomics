# Team

## Thông tin nhóm

- Tên nhóm: DKKT
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY13-DKKT-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/trinhcongduc112/K5-L3A-DAY13-DKKT-LaunchEconomics · nhánh `main` · commit chốt: (điền khi nộp)

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Trịnh Công Đức | 2A202603527 | 26ai.ductc2@vinuni.edu.vn | [trinhcongduc112](https://github.com/trinhcongduc112) | Trưởng nhóm · Người gắn nhãn 2, kiêm giữ hồ sơ |
|   2 | Nguyễn Vũ Khanh | 2A202603427 | 26ai.khanhnv@vinuni.edu.vn | [vukhanhkg2005-lang](https://github.com/vukhanhkg2005-lang) | Người viết code |
|   3 | Phạm Quang Trường | 2A202603378 | 26ai.truongpq@vinuni.edu.vn | [truongpham090325](https://github.com/truongpham090325) | Người kiểm số |
|   4 | Nguyễn Tuấn Kiệt | 2A202603417 | 26ai.kietnt3@vinuni.edu.vn | [kite1143](https://github.com/kite1143) | Người gắn nhãn 1 |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## TrinhCongDuc-2A202603527

### Phần việc phụ trách

- Trưởng nhóm: tạo repo nhóm, điều phối giờ giấc, chủ trì các lần gặp nhau, kiểm cả nhóm nộp đủ.
- Người gắn nhãn 2: gắn nhãn độc lập 20 ca lỗi, tính tỉ lệ đồng thuận, ghi quy tắc cho ca không trùng trong `report/team/bang_loi.md`.
- Giữ hồ sơ: `TEAM.md`, `report/team/ho_so_launch_v0.md`, trình bày và trả lời hội đồng khi duyệt chéo.

### Đóng góp cụ thể

- Điền `TEAM.md`: thông tin nhóm, bảng 4 thành viên, phần việc theo vai của từng người, và phần đóng góp của cả bốn người (tổng hợp từ báo cáo cá nhân).
- Điền `report/team/bang_loi.md`: bộ nhãn người 2 cho 20 ca, tỉ lệ đồng thuận **20/20 = 100%**, quy tắc phân biệt cho các ca khó (6, 8, 9, 13, 18, 20) và đoạn khai nguồn nhãn trung thực.
- Điền `report/team/ho_so_launch_v0.md` đủ **7 mục** và dòng đề xuất **Go có điều kiện** với 4 điều kiện, mỗi điều kiện có một chức danh phụ trách và một ngày kiểm tra.
- Nêu thẳng các con số bất lợi thay vì chỉ trình bày kết quả đẹp: xem lại 100% chỉ còn **0,98–1,03×** mức thủ công, **power 0,64** nếu tác động thật là 5 điểm, tỉ lệ mở lại **3,97%** chỉ cách trần 6% khoảng 2 điểm.
- Điều phối nhóm: mời thành viên vào repo, chủ trì các mốc gặp nhau, theo dõi "ai chờ ai", gửi hồ sơ cho nhóm hội đồng lúc 17:00.

### Bằng chứng

- Commit `4071c14` (`TEAM.md`, `bang_loi.md`, `ho_so_launch_v0.md` mục 1–3 và 7), `899b29b` (hồ sơ đủ 7 mục + đề xuất cuối), `051603e` (báo cáo cá nhân + phiếu chấm hội đồng).
- `report/team/bang_loi.md`: bảng so nhãn 20 ca với hai cột người 1 / người 2, dòng tổng kết 20/20 = 100%.
- `report/team/ho_so_launch_v0.md`: 7/7 mục có con số, trạng thái chỉ dùng ba giá trị cho phép, người phụ trách đều là chức danh.
- Kiểm số hồ sơ: đối chiếu **26/26 con số** trong hồ sơ với đầu ra `src/lab13.py`; tính `power` bằng `statsmodels` `NormalIndPower` (859 yêu cầu/nhóm) ra 0,64 cho mức chênh 5 điểm và 0,80 cho 6 điểm.
- `report/team/phieu_cham.md`: chấm nhóm ChuTichHungYen 3 tiêu chí có lý do bằng số, tổng 26/30, kèm một câu hỏi phản biện và câu trả lời của đội trình.

## NguyenVuKhanh-2A202603427

### Phần việc phụ trách

- Người viết code: viết `src/lab13.py` phần A và B, điền `report/team/bang_chi_phi.md`, viết phần rủi ro kinh tế trong `report/team/chi_so.md`, soạn `report/team/group_report.md`, kiểm tra cuối và push.

### Đóng góp cụ thể

- Viết phần **A** trong `src/lab13.py`: ba hàm A1 đạt ba phép thử (`1,20 · 1,25 · 1,25`), hàm `mo_hinh()` đọc hai file CSV với `keep_default_na=False`, tính A2 (**4.472 đ/việc thành công**, gấp **16,3 lần** hoá đơn `274,7 đ`, `simulated`), tách 4 loại yêu cầu ở A3 kèm tỉ lệ `ok` theo `attempt`, và cộng chi phí cố định 40 triệu đ/tháng ở A4 (`4.599 đ = 0,38×` ở 45.000 yêu cầu/tháng; `5.784 đ = 0,48×` ở nửa khối lượng, `simulated`).
- Viết phần **B**: 9 kịch bản độ nhạy B1, đổi cặp B2 (`6.543 đ`, `+46,3%`, `simulated`), xếp hạng ba yếu tố nhạy nhất (số ca làm lại · tỉ lệ xem lại · lương nhân viên), chi phí cả hệ thống B3 (giới hạn 2 lần chạy rẻ nhất `6.901.220 đ`, `simulated`) và kịch bản xem lại 100% B4 (`11.743 đ = 0,98×` và `12.414 đ = 1,03×`, `simulated`).
- Viết **E2** (3 dòng rủi ro kinh tế kèm dấu hiệu theo dõi, hành động, chức danh) trong `report/team/chi_so.md`.
- Giảng lại cách `mo_hinh` chạy cho cả nhóm trước khi bàn giao `src/lab13.py` cho Trường; soạn và hoàn thiện `report/team/group_report.md`, chạy các lệnh kiểm tra cuối và push.

### Bằng chứng

- Commit `d2ac4de` (phần A và B trong `src/lab13.py` + `report/team/bang_chi_phi.md`), `76225ce` (E2 trong `chi_so.md`), `3c57588` / `ccddeb9` / `86373ea` (`group_report.md` từ bản nháp đến bản chốt).
- `python lab13.py` trong `src/` in `Ba phép thử đáp án biết trước: ĐẠT`, `Tự kiểm tuyến tính B1: ĐẠT`, cùng toàn bộ bảng A1–A4, B1–B4, E1, D1; exit code 0.
- `report/team/bang_chi_phi.md`: A2 đủ **9 dòng**, A3 đủ **4 dòng**, B1 đủ **9 dòng**, mọi con số từ cột `_simulated` đều có nhãn `simulated`.

## PhamQuangTruong-2A202603378

### Phần việc phụ trách

- Người kiểm số: tự tính lại số của nhiệm vụ A, B để đối chiếu; viết phần chỉ số và danh sách event trong `report/team/chi_so.md` và phần tính chỉ số trong `src/lab13.py`; kiểm ngưỡng luật dừng và mọi con số trong hồ sơ.

### Đóng góp cụ thể

- **Bước 7 + 11 — tự tính để kiểm số:** viết script riêng đọc thẳng hai file CSV, **không nhìn code của Khánh**, tính độc lập 15 khoản chi phí (token, tool, lần chạy 2–3, xem lại, làm lại, tổng, việc thành công, CPS mỗi việc thành công, hoá đơn chia yêu cầu, CPS theo 4 loại) rồi so với số của Khánh.
- **Bước 15 + 19 — ba chỉ số:** thêm phần E1 vào `src/lab13.py` (chính **82,83%** · dùng **27,12%** · an toàn **4,25%**) và vào `report/team/chi_so.md` (3 chỉ số + 1 chỉ số dùng và 1 chỉ số an toàn tự đề xuất, mỗi chỉ số có công thức).
- **Bước 23 — danh sách event:** 10 event, mỗi event có `trace_id`, kèm bảng kiểm chéo 5 chỉ số ↔ event; xác nhận 4 event mà Kiệt dùng trong bảng khắc phục đều đã có nên không phải thêm.
- **Bước 25 + 29 — kiểm ngưỡng và kiểm số hồ sơ:** kiểm ba ngưỡng luật dừng so với mức thực của dữ liệu, góp ý cho Kiệt sửa lại luật dừng; truy nguồn từng con số trong `ho_so_launch_v0.md` về file gốc.

### Bằng chứng

- Commit `acc54d1` (E1 trong `lab13.py` + `chi_so.md`, kèm báo cáo cá nhân), `2baa8b5` (danh sách event + kiểm chéo chỉ số), `85e2b79`.
- Bảng so số 15 khoản trong báo cáo cá nhân: **độ lệch lớn nhất 0,0%** so với số của Khánh (ngưỡng cho phép là 2%), kết luận không cần báo Khánh sửa.
- `report/team/chi_so.md`: **10 event** có `trace_id` và bảng kiểm tra chéo cho thấy **cả 5 chỉ số đều đo được** từ danh sách event.
- Góp ý bước 25 gửi Kiệt: nói rõ so sánh "trong cùng đợt", bổ sung nền chi phí của phạm vi pilot, và định nghĩa "bỏ qua gợi ý"; Kiệt áp cả ba ở bước 26.

## NguyenTuanKiet-2A202603417

### Phần việc phụ trách

- Người gắn nhãn 1: gắn nhãn độc lập 20 ca lỗi, điền bảng khắc phục trong `report/team/bang_loi.md`; viết phần cỡ mẫu trong `src/lab13.py` và `report/team/pilot_plan.yaml`; chấm nhóm khác trong `report/team/phieu_cham.md`; theo dõi checklist "Xong khi".

### Đóng góp cụ thể

- **Bước 14 — bộ nhãn người 1:** gắn nhãn độc lập cả 20 ca lỗi trong 8 phút theo **nguyên nhân gốc**, không trao đổi với người gắn nhãn 2; dùng đủ năm loại (Do người dùng 4 · Hệ thống 5 · Ngữ cảnh 4 · Giới hạn hệ thống 4 · Ngầm 3).
- **Bước 18 — bảng khắc phục:** chọn mỗi loại một ca (1, 7, 18, 4, 17), mỗi dòng có event đo được, ngưỡng, tần suất kiểm và **một chức danh** phụ trách khác nhau; tên event khớp bộ từ vựng mà Trường dùng ở bước 23.
- **Bước 21 — cỡ mẫu trong `lab13.py`:** thêm hai hàm `co_mau_hai_ti_le()` và `so_yeu_cau_moi_cum()`, cùng khối in D1 và tỉ lệ mở lại hiện tại.
- **Bước 22 + 26 — `pilot_plan.yaml`:** chọn chia ngẫu nhiên theo nhân viên 20 + 20, nâng mức chênh từ 5 lên 6 điểm, viết 3 luật dừng đủ bốn vế; sau góp ý của Trường thì sửa lại cả ba luật và chỉnh hai con số bị sai đơn vị trong góp ý (3,58 → **3.414 đ**; 2,75 → **+2,03 điểm**).

### Bằng chứng

- Commit `62e13dd` (khung `pilot_plan.yaml` + `scope` từ A3), `c9a8816` (số nháp D1 và ngưỡng), `e26df4b` (CP4 trong `lab13.py` + bảng khắc phục 5 ca + `pilot_plan.yaml` hoàn chỉnh), `42e9fb1` (sửa ba luật dừng theo góp ý bước 25), `1cdff73` (báo cáo cá nhân).
- Kết quả D1 do `lab13.py` in ra: **1.251** yêu cầu/nhóm · DE **2,48** → **3.103**/nhóm → 42 người/nhóm (tổng 84 > 40 nên không đủ người) · trần 20 nhân viên **1.000 < 1.251** · trần 6 depot **300** · mức chênh 6 điểm cần **m ≥ 299** yêu cầu/người (DE 6,96) · tỉ lệ mở lại **4,25%** toàn mẫu và **3,97%** trong phạm vi.
- `report/team/bang_loi.md`: 20 ca có hai bộ nhãn, đồng thuận **20/20 = 100%**, bảng khắc phục đủ 5 loại.
- `report/team/pilot_plan.yaml`: `yaml.safe_load` đọc được, **không còn dấu `?`**, **3 luật dừng** đủ bốn vế NẾU – TRONG – THÌ – KHÔNG THÌ, mỗi luật có ngưỡng số, thời hạn và người có quyền dừng.
