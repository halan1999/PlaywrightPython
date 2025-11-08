#Tạo slug URL: 'Slug' là phiên bản rút gọn của tiêu đề, dùng cho URL. 
#Ví dụ, tiêu đề 'Top 5 học sinh giỏi' sẽ có slug là 'top-5-hoc-sinh-gioi'.
#Hãy viết code để chuyển đổi tiêu đề bất kì thành slug theo quy tắc.
#Chuyển hết về chữ thường 
#Thay thế tất cả các khoảng trắng bằng dấu gạch ngang (-)

URL = 'Top 5 HỌC sinh giỏi'
URLlower = URL.lower()
print(URLlower.replace(' ','-'))