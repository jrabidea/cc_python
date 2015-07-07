from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC



class BasePageObject(object):

	def __init__(self, driver):
		self.driver = driver


	def find_element(self, element):
		self.element = element
		return self.driver.find_element(*element)

	def find_elements(self, element):
		self.element = element
		return self.driver.find_elements(*element)

	def wait(self, element, timeout):

		try:
			WebDriverWait(self.driver, timeout).until(
				EC.visibility_of_element_located(element))
		except TimeoutException, e:
			message = "Time out!"
			raise TimeoutException(message)
