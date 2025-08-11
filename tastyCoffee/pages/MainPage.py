from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class MainPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
#Открытие страницы
    def open(self):
        self.driver.get('https://shop.tastycoffee.ru')
        self.driver.add_cookie({
            "name": "receive-cookie-deprecation",
            "value": "1"
        })
        self.driver.add_cookie({
            "name": "cookies",
            "value": "true"
        })

    def login_window(self,):
        self.driver.find_element(By.CSS_SELECTOR, "div .normal-case.cursor-pointer").click()

    def logout_btn(self):
        logout = self.driver.find_elements(By.CSS_SELECTOR, ".order-1 span")[4].text
        return logout

    def login(self, email: str, password: str):
        self.login_window()
        self.driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys(email)
        self.driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    #Поиск страницы
    def search(self, text: str):
        self.driver.find_element(By.CSS_SELECTOR, "button.no-underline[type='button']").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "#search-v-0-0-0-0").send_keys(text, Keys.RETURN)
#Открытие корзины
    def go_to_cart(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".relative.flex.order-4")))
        self.driver.find_element(By.CSS_SELECTOR, ".relative.flex.order-4").click()
#Получение числа товаров в корзине
    def get_counter(self):
        time.sleep(1)
        num_text = self.driver.find_elements(By.CSS_SELECTOR, ".block.text-ellipsis.mr-1")[1].text
        num = int(''.join(filter(str.isdigit, num_text)))
        return num
#Переход в избранное
    def go_to_favorite(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/my-favorites'][type='button']")))
        self.driver.find_element(By.CSS_SELECTOR, "a[href='/my-favorites'][type='button']").click()
#Содержимое избранного
    def name_item_card(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".product a.font-din-black")))
        name_items = [
            el.text.strip().lower()
            for el in self.driver.find_elements(By.CSS_SELECTOR, ".product a.font-din-black")]
        print(name_items)
        return name_items
        # name_item = self.driver.find_element(By.CSS_SELECTOR, ".product a.font-din-black").text.strip().lower()
        # print(name_item)
        # return name_item
#Получение числа товаров в избранном
    def get_counter_favorite(self):
        num_text = self.driver.find_element(By.CSS_SELECTOR, ".tc-amount__text").text
        return num_text
#Баннеры
    def espresso_banner(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/coffee?methods=1b']")))
        self.driver.find_element(By.CSS_SELECTOR, "a[href='/coffee?methods=1b']").click()

    def filter_banner(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/coffee?methods=3b']")))
        self.driver.find_element(By.CSS_SELECTOR, "a[href='/coffee?methods=3b']").click()

    def accessory_banner(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/accessories']")))
        self.driver.find_element(By.CSS_SELECTOR, "a[href='/accessories']").click()



