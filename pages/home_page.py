class HomePage:
    URL = "https://www.demoblaze.com/"

    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto(self.URL)

    def go_to_login(self):
        self.page.locator("#login2").click()

    def go_to_cart(self):
        self.page.locator("#cartur").click()
               