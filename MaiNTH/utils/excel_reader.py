import openpyxl


def read_login_data(file_path: str, sheet_name: str):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook[sheet_name]
    
    data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        case_id, username, password, expected, *_ = row

        # Convert None -> "" và ép về string
        case_id = "" if case_id is None else str(case_id)
        username = "" if username is None else str(username)
        password = "" if password is None else str(password)
        expected = "" if expected is None else str(expected)
        errormessage = "" if len(row) < 5 or row[4] is None else str(row[4])    

        data.append((case_id, username, password, expected, errormessage))
    
    return data

