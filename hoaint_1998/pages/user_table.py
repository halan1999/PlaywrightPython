from core.base_page import BasePage

class UserTable(BasePage):
    def __init__(self, page):
        super().__init__(page)

    URL = "https://book.anhtester.com/user-management"
    
    def open(self):
        self._goto(self.URL)

    def table(self):
        return self._get_locator("//table")
    
    def rows (self):
        return self._get_locator("//tbody//tr")

    def get_cell_text(self, row: int, col: int):
        return self._get_locator(f"//table//tbody//tr[{row}]/td[{col}]").inner_text().strip()
    
    def get_row_values(self, row: int):
        cells = self.rows().nth(row + 1).locator("td")
        return [cells.nth(i).inner_text().strip() for i in range(cells.count())]
    
    def get_column_values(self, col: int):
        rows = self.rows()
        values = []
        for i in range(rows.count()):
            values.append(rows.nth(i + 1).locator("td").nth(col).inner_text().strip())
        return values
    