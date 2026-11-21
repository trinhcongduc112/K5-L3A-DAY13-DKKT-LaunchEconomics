"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1.0 / p if k is None else (1.0 - (1.0 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1.0 - (1.0 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, chay_lai, xem_lai, lam_lai, tong, thanh_cong, cps, hoa_don_moi_yc.
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])].copy()
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000.0 * gia_vao + runs['tokens_out'] / 1000.0 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())

    return dict(
        token=float(tien_token.sum()),
        tool=float(tien_tool.sum()),
        chay_lai=float((tien_token + tien_tool)[runs['attempt'] > 1].sum()),
        xem_lai=float(xem_lai),
        lam_lai=float(lam_lai),
        tong=float(tong),
        thanh_cong=thanh_cong,
        cps=float(tong / thanh_cong),
        hoa_don_moi_yc=float((tien_token.sum() + tien_tool.sum()) / len(reqs)),
    )


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        if ten == 'hoa_don_moi_yc':
            print(f'{ten:14s} {gia_tri:>14,.1f}')
        else:
            print(f'{ten:14s} {gia_tri:>14,.0f}')

    # ---------- Nhiệm vụ A3 · Tách theo loại yêu cầu ----------
    print('\n=== A3 · TÁCH THEO LOẠI YÊU CẦU ===')
    print(f'{"Loại":10s} {"Số YC":>7s} {"Tỉ lệ TC":>10s} {"Lần chạy/YC":>13s} {"CPS [simulated]":>17s} {"So với 12.000đ":>15s}')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        sub_reqs = reqs[reqs['loai'] == loai]
        kq_loai = mo_hinh(runs, sub_reqs)
        so_yc = len(sub_reqs)
        tl_tc = kq_loai['thanh_cong'] / so_yc * 100
        lan_chay_tb = sub_reqs['so_lan_chay'].mean()
        so_voi_base = kq_loai['cps'] / BASELINE
        print(f'{loai:10s} {so_yc:7d} {tl_tc:9.1f}% {lan_chay_tb:13.2f} {kq_loai["cps"]:15,.0f} đ {so_voi_base:14.2f}x')

    print('\n--- Tỉ lệ lần chạy status == "ok" theo loại và lần thử (attempt) ---')
    merged_runs = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    merged_runs['is_ok'] = (merged_runs['status'] == 'ok').astype(float) * 100
    bang_attempt = merged_runs.pivot_table(index='loai', columns='attempt', values='is_ok', aggfunc='mean')
    print(bang_attempt.round(1).to_string())

    # ---------- Nhiệm vụ A4 · Chi phí cố định (phạm vi noi_dia + hang_nang) ----------
    print('\n=== A4 · CHI PHÍ CỐ ĐỊNH 40 TRIỆU Đ/THÁNG (PHẠM VI: noi_dia + hang_nang) ===')
    chi_phi_co_dinh = 40_000_000
    pham_vi_reqs = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq_pv = mo_hinh(runs, pham_vi_reqs)
    tc_mau = kq_pv['thanh_cong']
    cps_pv = kq_pv['cps']
    for nhan_kl, tong_yc_thang in [('45.000 yêu cầu/tháng', 45000), ('Một nửa khối lượng', 22500)]:
        viec_tc_thang = tong_yc_thang * tc_mau / len(reqs)
        co_dinh_moi_viec = chi_phi_co_dinh / viec_tc_thang
        tong_cps_co_dinh = cps_pv + co_dinh_moi_viec
        print(f'{nhan_kl:24s}: {viec_tc_thang:8,.0f} việc TC/tháng | Cố định: {co_dinh_moi_viec:6,.0f} đ/việc | CPS + cố định: {tong_cps_co_dinh:6,.0f} đ [simulated] ({tong_cps_co_dinh / BASELINE:.2f}x)')

    # ---------- Nhiệm vụ B1 · Đổi từng yếu tố ----------
    print('\n=== B1 · BẢNG ĐỘ NHẠY (ĐỔI TỪNG YẾU TỐ SO VỚI GỐC 4.472 Đ [simulated]) ===')
    kich_ban = {
        'Giá token gấp đôi':          dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa':     dict(gia_vao=13, gia_ra=65),
        'Tỉ lệ xem lại gấp đôi':      dict(he_so_xem_lai=2.0),
        'Tỉ lệ xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Số ca làm lại gấp đôi':      dict(he_so_lam_lai=2.0),
        'Số ca làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương nhân viên tăng 25%':   dict(luong_phut=2500),
        'Chỉ cho chạy tối đa 2 lần':  dict(max_lan_chay=2),
        'Chỉ cho chạy 1 lần':         dict(max_lan_chay=1),
    }
    goc_cps = ket_qua['cps']
    ket_qua_b1 = {}
    print(f'{"Kịch bản":28s} {"CPS [simulated]":>16s} {"Thay đổi":>10s}')
    print(f'{"Gốc (A2)":28s} {goc_cps:14,.0f} đ {"0.0%":>10s}')
    for ten_kb, tham_so in kich_ban.items():
        cps_kb = mo_hinh(runs, reqs, **tham_so)['cps']
        thay_doi = (cps_kb / goc_cps - 1.0) * 100.0
        ket_qua_b1[ten_kb] = thay_doi
        print(f'{ten_kb:28s} {cps_kb:14,.0f} đ {thay_doi:+9.1f}%')

    # Tự kiểm B1: mỗi kịch bản "giảm một nửa" bằng đúng nửa mức tăng của "gấp đôi"
    for yeu_to in ['Giá token', 'Tỉ lệ xem lại', 'Số ca làm lại']:
        tang = ket_qua_b1[f'{yeu_to} gấp đôi']
        giam = ket_qua_b1[f'{yeu_to} giảm một nửa']
        assert abs(giam + tang / 2.0) < 1e-9, f'Sai tuyến tính ở {yeu_to}'
    print('Tự kiểm tuyến tính B1 (giảm một nửa = -1/2 gấp đôi): ĐẠT')

    # ---------- Nhiệm vụ B2 · Đổi một cặp và xếp hạng ----------
    print('\n=== B2 · ĐỔI MỘT CẶP VÀ XẾP HẠNG ===')
    kq_cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2.0)
    td_cap = (kq_cap['cps'] / goc_cps - 1.0) * 100.0
    print(f'Giá token gấp đôi + Tỉ lệ xem lại gấp đôi: {kq_cap["cps"]:,.0f} đ [simulated] ({td_cap:+.1f}%)')
    print('Xếp hạng 3 yếu tố ảnh hưởng mạnh nhất: 1. Số ca làm lại (+51,8% / -25,9%) · 2. Tỉ lệ xem lại (+40,7% / -20,3%) · 3. Lương nhân viên (+23,1%)')

    # ---------- Nhiệm vụ B3 · Giới hạn chạy lại và chi phí cả hệ thống ----------
    print('\n=== B3 · GIỚI HẠN CHẠY LẠI VÀ CHI PHÍ CẢ HỆ THỐNG ===')
    print(f'{"Giới hạn":10s} {"Tổng trợ lý [sim]":>18s} {"Không TC":>10s} {"Cả hệ thống [sim]":>20s} {"CPS [sim]":>14s}')
    for k_lim in [1, 2, 3]:
        kq_k = mo_hinh(runs, reqs, max_lan_chay=k_lim)
        ko_tc = len(reqs) - kq_k['thanh_cong']
        ca_he_thong = kq_k['tong'] + ko_tc * BASELINE
        print(f'{k_lim} lần      {kq_k["tong"]:16,.0f} đ {ko_tc:10d} {ca_he_thong:18,.0f} đ {kq_k["cps"]:12,.0f} đ')

    # ---------- Nhiệm vụ B4 · Kịch bản xem lại 100% (noi_dia + hang_nang) ----------
    print('\n=== B4 · KỊCH BẢN XEM LẠI 100% (PHẠM VI noi_dia + hang_nang: 982 YÊU CẦU) ===')
    runs_pv = runs[runs['request_id'].isin(pham_vi_reqs['request_id'])]
    yc_co_ok = runs_pv[runs_pv['status'] == 'ok']['request_id'].nunique()
    so_ca_lam_lai_pv = int((pham_vi_reqs['ket_qua'] == 'lam_lai').sum())
    tien_token_tool_pv = kq_pv['token'] + kq_pv['tool']
    tien_xem_100 = yc_co_ok * 5 * LUONG_PHUT
    tien_lam_lai_9p = so_ca_lam_lai_pv * 9 * LUONG_PHUT
    tong_b4_9p = tien_token_tool_pv + tien_xem_100 + tien_lam_lai_9p
    cps_b4_9p = tong_b4_9p / tc_mau

    phut_lam_lai_tb = round(reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean(), 1)
    tien_lam_lai_15p = so_ca_lam_lai_pv * phut_lam_lai_tb * LUONG_PHUT
    tong_b4_15p = tien_token_tool_pv + tien_xem_100 + tien_lam_lai_15p
    cps_b4_15p = math.floor(tong_b4_15p / tc_mau)

    hoa_von_9p = (tc_mau * BASELINE - tien_token_tool_pv - tien_lam_lai_9p) / (yc_co_ok * LUONG_PHUT)
    hoa_von_15p = (tc_mau * BASELINE - tien_token_tool_pv - tien_lam_lai_15p) / (yc_co_ok * LUONG_PHUT)
    print(f'- Số yêu cầu phạm vi: {len(pham_vi_reqs)}, số YC có run ok: {yc_co_ok}, số ca làm lại: {so_ca_lam_lai_pv}, số việc thành công: {tc_mau}')
    print(f'- Với 9 phút/ca làm lại (đề bài): Tổng = {tong_b4_9p:,.0f} đ -> CPS = {cps_b4_9p:,.0f} đ = {cps_b4_9p / BASELINE:.2f}x của 12.000 đ [simulated] (hoà vốn xem lại <= {hoa_von_9p:.1f} phút).')
    print(f'- Với {phut_lam_lai_tb:.1f} phút/ca làm lại (trung bình cột simulated): Tổng = {tong_b4_15p:,.0f} đ -> CPS = {cps_b4_15p:,.0f} đ = {cps_b4_15p / BASELINE:.2f}x của 12.000 đ [simulated] (hoà vốn xem lại <= {hoa_von_15p:.1f} phút).')
    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
