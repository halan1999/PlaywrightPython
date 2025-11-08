#Cho chuỗi số điện thoại:
# messy_phone = " 090-123 4567 "
# Dùng strip() để bỏ khoảng trắng.
# Dùng replace() để bỏ dấu - và khoảng trắng.
# In ra số điện thoại chuẩn hóa: 0901234567.

messy_phone = ' 090-123 4567 '
phone1 = messy_phone.strip()
phone2 = phone1.replace('-','').replace(' ','')
print(phone2)