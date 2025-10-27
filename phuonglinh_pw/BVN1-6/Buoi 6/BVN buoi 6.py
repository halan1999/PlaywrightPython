import openpyxl, json
workbook = openpyxl.load_workbook("../buoi 3/data/Student.xlsx")
sheet = workbook.active
students = []
for row in sheet.iter_rows(min_row=2, values_only=True):
    student_id, name, score, level = row
    try:
        score_ft = float(score)
    except Exception as e:
        print(e)
    students.append({
        "ID": student_id,
        "Họ và tên": name,
        "Điểm": score,
        "Xếp loại": level
    })
print(students)
#tạo file json
with open("Report1.json", "w", encoding="utf-8") as f:
    json.dump(students, f, ensure_ascii= False, indent= 4)
print('Tạo file thành công')
#Đọc file json
with open("../buoi 3/Report1.json", "r", encoding="utf-8") as f:
    readjson = json.load(f)