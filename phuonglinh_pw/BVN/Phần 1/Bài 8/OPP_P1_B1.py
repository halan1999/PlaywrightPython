#Lớp Product(Sản phẩm).Viết 1 class Product để quản lý thông tin sản phẩm
#_init_:Nhận vào name, price và quanity(SL)
#phương thức get_total_price():trả về tổng giá trị của sản phẩm đó(price*quanity)
#phương thức display_info(): In ra thông tin sản phẩm theo định dạng:
#Sản phẩm:[Tên], Đơn giá:[Giá], Số lượng :[Số lượng], Tổng giá trị: [Tổng giá trị]

class Product:
    def __init__(self, name, price, quanity):
        self.name = name
        self.price = price
        self.quanity = quanity

    def get_total_price(self):
        return self.price*self.quanity
    
    def display_info(self):
        total = self.get_total_price()
        print(f"Sản phẩm: {self.name}, Đơn giá: {self.price}, Số lượng: {self.quanity}, Tổng giá trị: {total}")

product1 = Product("book", 1000, 3)
product2 = Product("pencil", 500, 10)

product1.display_info()
product2.display_info()