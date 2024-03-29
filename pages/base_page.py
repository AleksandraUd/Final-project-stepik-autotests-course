from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators

class BasePage():
	def __init__(self, browser, url, timeout=10):
		self.browser = browser
		self.url = url
		self.browser.implicitly_wait(timeout)

	def go_to_login_page(self):
		assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
		link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
		link.click()

	def go_to_basket(self):
		assert self.is_element_present(*BasePageLocators.BASKET_LINK), "Basket link is not presented"
		link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
		link.click()

	def input_value(self, how, what, value):
		assert self.is_element_present(how, what), "Input field is not presented"
		input_field = self.browser.find_element(how, what)
		input_field.send_keys(value)

	def is_disappeared(self, how, what, timeout=4):
		try:
			WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
		except TimeoutException:
			return False
		return True	

	def is_element_present(self, how, what):
		try:
			self.browser.find_element(how, what)
		except (NoSuchElementException):
			return False
		return True		

	def is_not_element_present(self, how, what, timeout=4):
		try:
			WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
		except TimeoutException:
			return True
		return False

	def read_innerHTML (self, how, what):
		return self.browser.find_element(how, what).text		
	
	def open(self):
		self.browser.get(self.url)

	def should_be_authorized_user(self):
		assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented, probably unauthorised user"

	def should_be_login_link(self):
		assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

