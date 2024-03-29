from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest
import time

#@pytest.mark.parametrize('promo_number', ["0", "1", "2", "3", "4", "5", "6",							
#								  pytest.param("7", marks=pytest.mark.xfail),
#								  "8", "9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
	link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	page = ProductPage(browser, link)
	page.open()
	page.add_to_basket()
	page.should_appear_message_about_added_product_with_correct_product_name()
	page.should_appear_message_about_basket_total_with_correct_value()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket (browser):
	link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
	page = ProductPage(browser, link)
	page.open()
	page.add_to_basket()
	page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
	link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
	page = ProductPage(browser, link)
	page.open()
	page.should_not_be_success_message()

@pytest.mark.xfail
def test_success_message_disappeared_after_adding_product_to_basket(browser):
	link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
	page = ProductPage(browser, link)
	page.open()
	page.add_to_basket()
	page.should_dissapear_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.should_be_login_link()	

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page (browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.go_to_login_page()
	login_page = LoginPage(browser, browser.current_url)
	login_page.should_be_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.go_to_basket()
	basket_page=BasketPage(browser, browser.current_url)
	basket_page.should_be_empty()
	basket_page.should_has_disclaimer_empty_basket()

class TestUserAddToBasketFromProductPage():
	@pytest.fixture(scope="function", autouse=True)
	def setup(self, browser):
		link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
		login_page = LoginPage(browser, link)
		login_page.open()
		email = str(time.time()) + "@fakemail.org"
		login_page.register_new_user(email, "rfhfrekb9")
		login_page.should_be_authorized_user()
		self.browser=browser

	def test_user_cant_see_success_message(self):
		link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
		page = ProductPage(self.browser, link) 
		page.open()
		page.should_not_be_success_message()

	@pytest.mark.need_review
	def test_user_can_add_product_to_basket(self):
		link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
		page = ProductPage(self.browser, link)
		page.open()
		page.add_to_basket()
		page.should_appear_message_about_added_product_with_correct_product_name()
		page.should_appear_message_about_basket_total_with_correct_value()
