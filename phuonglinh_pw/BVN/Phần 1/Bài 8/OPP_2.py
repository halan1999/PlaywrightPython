class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
# Tạo 2 đối tượng xe hơi
car1 = Car("Toyota", "Vios")
car2 = Car("Honda", "Civic")

# In ra thông tin của chúng
print(car1.brand, car1.model)
print(car2.brand, car2.model)