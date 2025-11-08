#Chuẩn hóa số điện thoại: Một số điện thoại được nhập vào có dạng messy_phone = ' 090-123 4567'.
# Hãy viết code để chuẩn hóa SĐT này về dạng loại bỏ hết khoảng trắng và gạch nối

messy_phone = '090-123 4567'
clean_phone = messy_phone.replace('-','').replace(' ','')
print(clean_phone)
