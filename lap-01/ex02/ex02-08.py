# Hàm kiểm tra số nhị phân có chia hết cho 5 không
def chia_het_cho_5(so_nhi_phan):
    # Chuyển số nhị phân sang số thập phân
    so_thap_phan = int(so_nhi_phan, 2)
    # Kiểm tra xem số thập phân có chia hết cho 5 không
    if so_thap_phan % 5 == 0:
        return True
    else:
        return False

# Nhập chuỗi số nhị phân từ người dùng
chuoi_so_nhi_phan = input("Nhập chuỗi số nhị phân (phân tách bởi dấu phẩy): ")

# Xử lý chuỗi và in kết quả
danh_sach_so = chuoi_so_nhi_phan.split(',')
ket_qua = []

for s in danh_sach_so:
    if chia_het_cho_5(s.strip()):
        ket_qua.append(s.strip())

print(", ".join(ket_qua))