base_url = "https://hrm.anhtester.com/erp"
username = "admin_example"
password = "123456"
#câu lệnh kích hoạt venv: venv\Scripts\activate
#câu lệnh run test: pytest -s tests\Multi_Tabs\test_orange_hrm.py
pytest -s tests\ui\Core_HR\Designation\test_designation.py
#debug: set PWDEBUG=1 & pytest -s tests\test_class_buoi4.py
#huy debug: set PWDEBUG=1