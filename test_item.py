from selenium.webdriver.common.by import By
import time

def test_product_page_have_add_to_basket_button(browser):

    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

    browser.get(link)

    add_basket_button = browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')

    assert add_basket_button.is_displayed(), 'Кнопка добавления товара в корзину отсутсвует'


