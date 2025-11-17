# #Máy tính đơn giản. Viết 1 class Calculator.
# Không cần __init__ phức tạp.
# Phương thức add(a, b): Trả về tổng của a và b.
# Phương thức subtract(a, b): Trả về hiệu của a và b.
# Phương thức multiply(a, b): Trả về tích của a và b.
# Phương thức divide(a, b): Trả về thương của a và b. Dùng try-except để xử lý trường hợp b bằng 0.

class Calculator:
    def add(self,a,b):
        return a+b
    def subtract(self,a,b):
        return a-b
    def multiply(self,a,b):
        return a*b
    def divide(self,a,b):
        try:
            return a/b
        except ZeroDivisionError:
            return "b phải khác 0"     

calc1 = Calculator()
print(calc1.add(2,3))
print(calc1.divide(2,0))
