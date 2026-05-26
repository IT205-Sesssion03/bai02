# Phân tích lỗi
# Trace code khi nhập số ngày công = 0:
# Vòng lặp bắt đầu xử lý nhân viên số 2
# working_days = 0 -> điều kiện if working_days == 0: đúng, chương trình in ra cảnh báo
# Tuy nhiên sau đó chương trình không dừng mà tiếp tục chạy xuống:
# Kết quả: vẫn tính thưởng (0 VND) và gửi email dù đã cảnh báo không xét duyệt

# Nguyên nhân:
# Vấn đề nằm ở cấu trúc điều kiện trong vòng lặp lập trình viên chỉ dùng if để in cảnh báo nhưng không có else hoặc continue để bỏ qua phần tính thưởng
# Đây là lỗi logic: không tách nhánh xử lý, dẫn đến việc khối lệnh sau vẫn chạy dù điều kiện cảnh báo đã đúng

# Sửa lỗi
# Giải pháp:
# Khi số ngày công = 0, in cảnh báo và dùng continue để chuyển ngay sang vòng lặp kế tiếp, bỏ qua phần tính thưởng và gửi email

print("--- HỆ THỐNG GỬI EMAIL THƯỞNG TẾT ---")
for employee_number in range(1, 4):
    print(f"--- Đang xử lý nhân viên số {employee_number} ---")
    working_days = int(input("Nhập số ngày công trong tháng: "))
    if working_days == 0:
        print("CẢNH BÁO: Nhân viên nghỉ cả tháng. Không xét duyệt thưởng.")
        continue 
    bonus_amount = working_days * 200000
    print(f" Đã tự động gửi Email: 'Chúc mừng nhận được {bonus_amount} VNĐ tiền thưởng!'")
print("Đã hoàn tất quá trình duyệt thưởng cho 3 nhân viên!")