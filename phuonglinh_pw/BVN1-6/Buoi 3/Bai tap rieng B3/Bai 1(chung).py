#Bai 1
products = ["iPhone 13", "Samsung Galaxy", "MacBook Pro 16 inch", "Oppo Reno"]
found = False
for p in products:
    if p == "MacBook Pro 16 inch":
        found = True
        break
if found:
    print(f'Đã tìm thấy sản phẩm: {p}')
else:
    print('Không tìm thấy sản phẩm')
