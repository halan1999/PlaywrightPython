# Automation - LoginPage Object Tạo một class LoginPage hoàn chỉnh (không cần chạy Selenium thật, chỉ cần viết code).
# __init__(self, driver): Lưu lại driver.
# Thuộc tính: username_locator, password_locator, login_button_locator.
# Phương thức enter_username(self, username): Giả lập việc tìm element username và gõ username vào. Dùng print() để mô phỏng.
# Phương thức enter_password(self, password): Tương tự cho password.
# Phương thức click_login(self): Tương tự cho nút login.
# Phương thức login(self, username, password): Gọi 3 phương thức trên theo đúng thứ tự để thực hiện toàn bộ quy trình đăng nhập.

class LoginPage:
    def __init__(self, driver):
        self.username_locator = "input#username"
        self.password_locator = "input#password"
        self.login_button_locator = "button#login"
    def enter_username(self, username):
        print(f"Tìm elementt: {self.username_locator}")
        print(f"Nhập username: {username}")
    def enter_password(self, password):
        print(f"Tìm element: {self.password_locator}")
        print(f"Nhập password: {password}")
    def click_login(self):
        print(f"Tìm element: {self.login_button_locator}")    
        print(f"Click button {self.login_button_locator}")   
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        print("login hoàn tất")
