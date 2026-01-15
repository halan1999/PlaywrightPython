from pages.user_table import UserTable

def test_user_table(page):
    table = UserTable(page)
    table.open()
    print("-----------CELL---------")
    print(table.get_cell_text(1, 1))
    print("-----------ROW---------")
    print(table.get_row_values(2))
    print("-----------COL---------")
    print(table.get_column_values(0))
