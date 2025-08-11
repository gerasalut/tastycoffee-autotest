from selenium import webdriver
from tastyCoffee.pages.ItemCard import ItemCard
from tastyCoffee.pages.ResultPage import ResultPage
from tastyCoffee.pages.MainPage import MainPage
import pytest

@pytest.fixture()
def driver():
    browser = webdriver.Chrome()
    browser.implicitly_wait(8)
    browser.maximize_window()
    yield browser
    browser.quit()

@pytest.fixture()
def main(driver):
    return MainPage(driver)

@pytest.fixture()
def result(driver):
    return ResultPage(driver)

@pytest.fixture()
def item(driver):
    return ItemCard(driver)