from playwright.sync_api import expect


def test_homepage_title(page):
    page.goto("https://www.demoblaze.com/")
    assert "STORE" in page.title()


def test_nav_links_exist(page):
    page.goto("https://www.demoblaze.com/")
    # Over základné navigačné prvky
    assert page.locator("a.nav-link", has_text="Home").first.is_visible()
    assert page.locator("a.nav-link", has_text="Contact").first.is_visible()
    assert page.locator("a.nav-link", has_text="About us").first.is_visible()
    # Over tlačidlá vpravo hore
    assert page.locator("#cartur").is_visible()     # Cart
    assert page.locator("#login2").is_visible()     # Log in
    assert page.locator("#signin2").is_visible()    # Sign up

def test_add_to_cart(page):
    page.goto("https://www.demoblaze.com/")

    # 1) otvor prvý produkt a vezmi jeho názov
    first_produkt = page.locator(".hrefch").first
    product_name =  first_produkt.text_content().strip()
    first_produkt.click()

    # 2) počkaj na tlačidlo a klikni
    page.get_by_text("Add to cart").click()

    # 3) potvrď alert "Product added"
    def on_dialog(d):
        assert "Product added" in d.message
        d.accept()
        page.once("dialog", on_dialog)

    # 4) choď do košíka a over, že je tam položka    
    page.locator("#cartur").click()
    page.wait_for_url("**/cart.html")
    rows = page.locator("tr.success") 
    expect(rows).to_have_count(1)
    # aspoň 1 položka
    # (voliteľné) over názov
    # expect(page.locator("#tbodyid tr.success td:nth-child(2)")).to_contain_text(product_name)  
     
from pages.home_page import HomePage
from pages.login_page import LoginPage

def test_login_invalid(page):
    home = HomePage(page)
    home.open()
    home.go_to_login()

    login = LoginPage(page)
    login.login("nespravne_meno", "zle_heslo")

    def on_dialog(dialog):
        assert "User does not exist" in dialog.message
        dialog.accept()

    page.once("dialog", on_dialog)
    page.wait_for:timeout(2000)
    
        
        