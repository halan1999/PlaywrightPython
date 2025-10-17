# NOTE: Khu vực 4 progressbar đầu trang - Chỉ lấy thẻ chưa progress bar phục vụ cho kịch bản verify value hiện tại của progress bar

# PROGRESS BAR 1: Invoices Awaiting Payment
# //div[contains(@class,'quick-stats-invoices')]//div[@role='progressbar']

# PROGRESS BAR 2: Converted Leads
# //div[contains(@class,'quick-stats-leads')]//div[@role='progressbar']

# PROGRESS BAR 3: Projects In Progress
# //div[contains(@class,'quick-stats-projects')]//div[@role='progressbar']

# PROGRESS BAR 4: Tasks Not Finished
# //div[contains(@class,'quick-stats-tasks')]//div[@role='progressbar']


##########################################################################################################
# NOTE: Khu vực Calendar - phục vụ chọn ô ngày hôm nay

# LABEL THÁNG - NĂM: Chỉ lấy thẻ để get text phục vụ verify tháng năm hiện tại
# //div[@id='widget-calendar']//h2

# NÚT LÙI THÁNG: Nếu tháng hiển thị đang là tương lai của tháng hiện tại
# //div[@id='calendar']//button[@aria-label='prev']

# NÚT TIẾN THÁNG: Nếu tháng hiển thị đang là quá khứ của tháng hiện tại
# //div[contains(@class,'quick-stats-projects')]//div[@role='progressbar']

# Ô ngày hiện tại
# //div[@id='calendar']//td[contains(@class,'today')]

##########################################################################################################
# NOTE: Khu vực My Tasks - Lấy các giá trị Export LƯU Ý: Các đối tượng hiển thị sau khi click nút Export

# NÚT EXCEL
# //span[normalize-space()='Export']/parent::button/following-sibling::div//li[contains(@class,'excel')]

# NÚT CSV
# //span[normalize-space()='Export']/parent::button/following-sibling::div//li[contains(@class,'csv')]

# NÚT PDF
# //span[normalize-space()='Export']/parent::button/following-sibling::div//li[contains(@class,'pdf')]

# NÚT PRINT
# //span[normalize-space()='Export']/parent::button/following-sibling::div//li[contains(@class,'print')]