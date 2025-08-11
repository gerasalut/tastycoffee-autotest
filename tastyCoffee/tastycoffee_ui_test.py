from tastyCoffee.pages.ItemCard import ItemCard
from tastyCoffee.pages.MainPage import MainPage
from tastyCoffee.pages.ResultPage import ResultPage
import pytest

#Авторизация пользователя
@pytest.mark.parametrize("email,password", [
    ("email", "password")
])
def test_login_user(main: MainPage, email, password):
    main.open()
    main.login(email, password)
    logout_txt = main.logout_btn()
    assert logout_txt == "Выйти"

#Поиск товара и добавление его в корзину на странице результата
def test_result_page_add_cart(main: MainPage, result: ResultPage):
    main.open()
    main.search("Воронка")
    result.add_cart()
    counter = main.get_counter()
    assert counter == 1

#Поиск товара и добавление его в корзину в карточке товара
def test_add_to_cart_in_item_card(main: MainPage, result: ResultPage, item: ItemCard):
    main.open()
    main.search("Эфиопия")
    result.go_to_card()
    item.add_cart()
    counter = main.get_counter()
    assert counter == "1"

#Поиск товара, добавление его в избранное в карточке товара, переход в избранное и проверка товара
def test_result_page_add_favorite(main: MainPage, result: ResultPage, item: ItemCard):
    main.open()
    main.search("Кения")
    result.go_to_card()
    item.add_favorite()
    favorite = main.get_counter_favorite()
    assert favorite == "1"
    main.go_to_favorite()
    assert any("кения" in name for name in main.name_item_card())


#Проверка, что интерактивные баннеры ведут на корректную страницу категорий
def test_espresso_banner(main: MainPage, result: ResultPage):
    main.open()
    main.espresso_banner()
    assert result.category_title_card() == "для эспрессо"

def test_filter_banner(main: MainPage, result: ResultPage):
    main.open()
    main.filter_banner()
    assert result.category_title_card() == "для фильтра"

def test_accessory_banner(main: MainPage, result: ResultPage):
    main.open()
    main.accessory_banner()
    assert result.category_title_card() == "аксессуары для кофе"