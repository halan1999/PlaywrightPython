email = "abc@gmail.com" #biến global (dc dùng trong các class trong cùng file)
class User:
    def __init__(self, Fname, Lname, age):
        self.Fname = Fname #biến instance (dc dùng trong class này)
        self.Lname = Lname
        self.age = age
        isActive = True
    def Identify(self, age):
        number = "123" #biến local (chỉ dùng trong phương thức này)
        if (age >= 18):
            print("You are mature")
            print(email)
            print(self.Fname)
        else:
            print("You are a kid")

sv1 = User("Alex","Park", 18)
sv2 = User("Mira","Kim", 20)
sv2.Identify(20)

# print(sv2.age)

