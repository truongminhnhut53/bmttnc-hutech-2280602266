#nhập số từ người dùng
so =  int(input("Nhập một số nguyên: "))
# kiểm tra xem số đó chẵn hay lẽ
if so % 2 == 0:
    print(so, "là số chẵn.")
else:
    print(so, "ko phải là số chẵn.")