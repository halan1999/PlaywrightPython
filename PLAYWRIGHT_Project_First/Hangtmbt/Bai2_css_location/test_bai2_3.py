https://crm.anhtester.com/admin
admin@example.com
123456
1. Dashboard
- Lấy theo role:
page.get_by_role("link",name="Dashboard")
- Lấy theo text:
page.get_by_text("Dashboard")
- Lấy theo CSS:
page.locator('#side-menu li.menu-item-dashboard > a')
2. Customers:
- Lấy theo role:
page.get_by_role("link", name="Custormers")
- Lấy theo href:
page.locator('a[href="/admin/customers"]')
page.locator('a[href*="/admin/customers"]') #có thể có tiền tố hoặc hậu tố
- Lấy theo CSS:
page.locator('#side-menu li.menu-item-customers>a')
3. sale
- Lấy theo role:
page.get_by_role("link", name="Sales")
- Lấy theo CSS:
page.locator("#side-menu li.menu-item-sales  >a")
