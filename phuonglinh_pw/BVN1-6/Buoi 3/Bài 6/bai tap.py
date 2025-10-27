import openpyxl, json
workbook = openpyxl.load_workbook("../buoi 3/data/logindata.xlsx")
sheet = workbook.active
students = []
for row in sheet.iter_rows(min_row=2, values_only=True):
    stt, student_id, name, score = row
    try:
        score_ft = float(score)
        stt_ft = int(stt)
    except Exception as e:
        print(e)
    if score_ft >= 9:
        students.append({
            "ID": student_id,
            "Ho va ten": name,
            "Level": "Very good"
        })    
# print(students)
#Tạo file json
with open("Report.json", "w", encoding="utf-8") as f:
    json.dump(students, f, ensure_ascii=False, indent=4)
print("Tao file json thanh cong")
#Đọc file json
with open("../buoi 3/report.json", "r", encoding="utf-8")as f:
    loaddata = json.load(f)
# print(loaddata[0])
# print(loaddata[1])