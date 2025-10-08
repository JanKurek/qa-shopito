class LoginPage:
    def __init__(self, page):
        self.page = page

    def login(self, username, password):
        self.page.wait_for_selector("#logInModal")
        self.page.locator("#loginusername").fill(username)
        self.page.locator("#loginpassword").fill(password)
        self.page.locator("//button[text()='Log in']").click()
            