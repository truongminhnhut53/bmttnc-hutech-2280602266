def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]
# Sử dụng hàm và in kết quả
input_string = input("Nhập và chuỗi cần đảo ngược: ")
print("Chuỗi cần đảo ngược là: ", dao_nguoc_chuoi(input_string))
