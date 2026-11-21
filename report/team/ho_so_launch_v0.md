# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: DKKT · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | **4.472 đ** mỗi việc thành công [simulated], gấp **16,3×** hoá đơn token + tool chia số yêu cầu (274,7 đ, đo từ trace). Làm lại chiếm 51,8% và xem lại 40,7% tổng chi phí [simulated]. Trong phạm vi `noi_dia` + `hang_nang`, cộng chi phí cố định ở 45.000 yêu cầu/tháng: 4.599 đ [simulated]. Nguồn: `bang_chi_phi.md` (A2, A4) | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1) Số ca làm lại: +51,8% / −25,9% · 2) Tỉ lệ xem lại: +40,7% / −20,3% · 3) Lương nhân viên: +23,1% (giá token chỉ +5,6%) [simulated]. Nguồn: `bang_chi_phi.md` (B1, B2) | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Cả hệ thống **5.865 đ/yêu cầu = 0,49×** của 12.000 đ [simulated], đã cộng 222 ca chuyển nhân viên. Theo loại: `noi_dia` 0,22× · `hang_nang` 0,69× · `doi_tac` 0,85× · `quoc_te` 1,88× [simulated]. **Con số bất lợi:** xem lại 100% là 11.743–12.414 đ = 0,98–1,03× [simulated], tức gần như không tiết kiệm (B4) | Giả lập | Giám đốc vận hành LogiX-VN |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chỉ số trong đợt chạy thử (chưa có nhóm đối chứng): **chính 82,83%** (994/1.200) đóng trong 24 giờ và không mở lại 7 ngày · **dùng 27,12%** (48/177) bỏ qua gợi ý · **an toàn 4,25%** (51/1.200) mở lại trong 7 ngày; trong phạm vi `noi_dia` + `hang_nang` là 3,97% (39/982). Đủ 10 event có `trace_id`, cả 5 chỉ số tính được từ event. Nguồn: `chi_so.md` (E1) | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | 20 ca gắn nhãn năm loại, đồng thuận **20/20 = 100%** (cả hai bộ nhãn có dùng AI, đã khai trong `bang_loi.md`). Bảng khắc phục đủ 5 loại, mỗi dòng có event, ngưỡng và một vai phụ trách. Ví dụ: đối soát mỗi giờ sổ cái và tin nhắn "đã hoàn", ngưỡng 0 ca lệch (ca 7); kiểm mẫu 100 đơn/tuần, ngưỡng ≥ 1% lệch (ca 17) | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia theo **nhân viên: 20 dùng trợ lý + 20 đối chứng** (đủ 20 cụm mỗi nhóm), chỉ `noi_dia` + `hang_nang`. Cần 859 yêu cầu hiệu dụng mỗi nhóm, mỗi nhân viên ≥ 299 yêu cầu (hệ số thiết kế 6,96). Phát hiện được mức chênh **6 điểm**, không đủ mẫu cho 5 điểm (trần 1.000 < 1.251 yêu cầu). Ba luật dừng: mở lại ≥ +2 điểm so với đối chứng hoặc > 6%; chi phí > 6.700 đ [simulated]; bỏ qua gợi ý > 40%. Quyết định ngày 2027-01-05. Nguồn: `pilot_plan.yaml`, `lab13.py` (D1) | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Số ca làm lại gấp đôi: +51,8%, lên 6.787 đ · xem lại 100% kéo dài: 0,98–1,03× · khối lượng còn một nửa: 5.784 đ = 0,48× [simulated]. Ba dòng rủi ro có dấu hiệu theo dõi và hành động ở `chi_so.md` (E2) | Giả lập | PM trợ lý hoàn phí |

**Đề xuất: Go có điều kiện** cho pilot chỉ trong phạm vi `noi_dia` + `hang_nang`. Chưa xin duyệt cho `quoc_te` (1,88×, thành công 27,3%) và `doi_tac` (0,85×) [simulated]. Lý do: chi phí rẻ hơn nhân viên tự làm (0,22× và 0,69×) [simulated], an toàn hiện tại 3,97% có chỗ cho trần 6%, và pilot có đối chứng cùng đợt. Điều kiện (mỗi điều kiện một người phụ trách và một ngày kiểm tra):

1. Sửa khoá chống trùng và đối soát sổ cái trước khi bắt đầu, vì ca 7 (báo "đã hoàn" khi sổ cái trả 503) và ca 20 (hoàn hai lần) là lỗi hệ thống đã lộ ra. **Kỹ sư trưởng agent · kiểm 2026-12-04.**
2. Ký chấp nhận mức chênh 6 điểm. Nếu tác động thật chỉ 5 điểm thì power chỉ còn **0,64** (statsmodels `NormalIndPower`, n = 859 mỗi nhóm), pilot khó kết luận. **Giám đốc vận hành LogiX-VN · kiểm 2026-12-04.**
3. Bật đủ event có `trace_id` và đo thật phút xem lại, phút làm lại; thay số phút giả lập trong mô hình chi phí sau tuần 1. **Kỹ sư trưởng agent · kiểm 2026-12-14.**
4. Có kế hoạch giảm xem lại theo bậc, vì xem lại 100% chỉ còn 0,98–1,03× (B4) [simulated]; mốc theo dõi là tỉ lệ xem lại > 50% hoặc thời gian xem lại đo thật > 4,8 phút/ca. **Trưởng nhóm CSKH · kiểm 2026-12-21.**

**Con số bất lợi và cách xử lý:** (a) xem lại 100% gần như không tiết kiệm, xử lý bằng điều kiện 4; (b) tỉ lệ mở lại hiện tại 3,97% chỉ cách trần 6% khoảng 2 điểm, nên luật dừng đặt so với nhóm đối chứng cùng đợt; (c) mọi số tiền dựa trên phút giả lập [simulated], xử lý bằng điều kiện 3; (d) số ca làm lại là yếu tố nhạy nhất (+51,8% nếu gấp đôi), theo dõi hằng tuần với dấu hiệu > 7%.
