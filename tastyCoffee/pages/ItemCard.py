from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ItemCard:
    def __init__(self, driver :WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_cart(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".tc-btn-pay")))
        self.driver.find_element(By.CSS_SELECTOR, ".tc-btn-pay").click()

    def add_favorite(self):
        self.driver.find_element(By.CSS_SELECTOR, "[title='Добавить в избранное']").click()


