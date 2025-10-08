from playwright.sync_api import expect

class CartPage:
    def __init__(self,page):
        self.page = page

    def verify_loaded(self):
        self.page.wait_for_url("**/cart.html")
        expect(self.page.locator("tr.success")).to_be_visible() 
           