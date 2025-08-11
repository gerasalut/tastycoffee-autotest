from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ResultPage:
    def __init__(self, driver :WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_cart(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".tc-btn-pay")))
        self.driver.find_elements(By.CSS_SELECTOR, ".tc-btn-pay")[2].click()

    def go_to_card(self):
        self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "picture.object-contain")))
        self.driver.find_elements(By.CSS_SELECTOR, "picture.object-contain")[2].click()

    def category_title_card(self):
        title_text = self.driver.find_element(By.CSS_SELECTOR, ".tc-tile__top div.mr-auto")
        print(title_text.text.strip())
        return title_text.text.strip()