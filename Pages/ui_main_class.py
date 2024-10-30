from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import allure
from time import sleep
from selenium.webdriver.common.keys import Keys


class MainUI:

    def __init__(self, driver: WebDriver) -> None:
        self.__url = "https://altaivita.ru/"
        self.__pr = "https://altaivita.ru/category/sweets/"
        self.__driver = driver

    @allure.step("UI. Авторизоваться на главной странице")
    def authorization(self, login='kojoxi7233@degcos.com', password='3iecnXhzsucD9'):
        """ Осуществляет авторизацию на главной странице сайта

            Принимает параметры: login и password

            Если не передавать параметры, то логин и пароль идут по умолчанию
        """
        self.__driver.get(self.__url)
        self.__driver.find_element(By.CSS_SELECTOR, '[href="/login/"]').click()
        self.__driver.implicitly_wait(10)
        self.__driver.find_element(
            By.CSS_SELECTOR, 'input[name="aj_login"].aj_login').send_keys(login)
        self.__driver.find_element(
            By.CSS_SELECTOR, 'button[class="main-btn green sign-in"]').click()
        self.__driver.find_element(
            By.CSS_SELECTOR, 'input.password').send_keys(password)
        self.__driver.find_element(
            By.XPATH, '(//button[text()="Войти"])[3]').click()
        self.__driver.implicitly_wait(10)

    @allure.step("UI. Перейти на страницу корзины")
    def to_cart(self):
        """ Осуществляет переход на страницу корзины"""
        self.__driver.get(self.__url)
        self.__driver.find_element(By.CSS_SELECTOR, 'a[href="/cart/"]').click()
        self.__driver.find_element(By.CSS_SELECTOR, 'a[href="/cart/"][contains(text(),"Перейти в корзину")]').click()
        sleep(5)

    @allure.step("UI. Добавить товар в корзину")
    def add_product(self):
        """ Добавляет товар в корзину"""
        self.__driver.get(self.__pr)
        sleep(5)
        self.__driver.find_element(
            By.XPATH, "//i[@class='fa fa-times-circle']").click()
        sleep(5)
        body = self.__driver.find_element(By.TAG_NAME, 'body')
        body.send_keys(Keys.PAGE_DOWN)
        # self.__driver.execute_script("window.scrollBy(0, 6000)")
        self.__driver.find_element(
            By.XPATH, "//span/text()[. ='в корзину'][1]").click()
# "//div[@class='product__add_2_0 js-product__add_2_0_cat_preview_3590']//button//span[contains(text(),'в корзину')]"

    @allure.step("UI. Увеличить количество товара в корзине")
    def add_another_product(self):
        """ Добавляет товар в корзину(увеличивает количество)"""
        self.__driver.get(self.__url)
        self.__driver.find_element(
            By.XPATH, "(//div[@class='product_add_2_0']//button[contains(text(), 'В корзину')])[1]")

    @allure.step("UI. Удалить товар из корзины")
    def delete_product(self):
        """ Удаляет товар из корзины"""
        self.__driver.get(self.__url)
        self.__driver.find_element(
            By.CSS_SELECTOR, '#products_595397::button[class="basket_delete js-item-delete"]')
