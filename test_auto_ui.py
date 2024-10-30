from Pages.ui_main_class import MainUI
import pytest
import allure

@allure.epic("AltaivitaCard")
@allure.severity("blocker")
@allure.id("Card - 1")
@allure.story("Добавление товара в корзину")
@allure.feature("UPDATE")
@allure.title("Добавление товара в корзину")
@pytest.mark.ui_tests
def test_add_product_to_card(chrome_browser):
    ui_card = MainUI(chrome_browser)
    with allure.step("Авторизоваться на странице сайта"):
        ui_card.authorization()
    with allure.step("Добавить продукт в корзину"):
        ui_card.add_product()
    with allure.step("Перейти на страницу корзины"):
        ui_card.to_cart()
    with allure.step("Удалить продукт из корзины"):
        ui_card.delete_product()

@allure.epic("AltaivitaCard")
@allure.severity("blocker")
@allure.id("Card - 2")
@allure.story("Изменение количества товара в корзине(увеличить)")
@allure.feature("UPDATE")
@allure.title("Изменение количества товара в корзине")
@pytest.mark.ui_tests
def test_update_count_products(chrome_browser):
    ui_card = MainUI(chrome_browser)
    with allure.step("Авторизоваться на странице сайта"):
        ui_card.authorization()
    with allure.step("Добавить продукт в корзину"):
        ui_card.add_product()
    with allure.step("Перейти на страницу корзины"):
        ui_card.to_cart()
    with allure.step("Увеличить количество товара"):
        ui_card.add_another_product()
    with allure.step("Удалить продукт из корзины"):
        ui_card.delete_product()
