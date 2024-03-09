from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import BasketPageLocators

class ProductPage(BasePage):
    def add_item_to_basket(self):
        #нажимаем на кнопку "Добавить товар в корзину"
        add_button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        add_button.click()
    
    def there_are_basket_button(self):
        assert self.is_element_is_present( *ProductPageLocators.BUTTON_ADD_TO_BASKET), "Нет кнопки добавления товара"
    
    def there_are_product_name(self):
        assert self.is_element_present(*ProductPageLocators.CHECK_NAME), "Отсутствует название продукта"
    
    def there_are_product_price(self):
        assert self.is_element_present(*ProductPageLocators.CHECK_PRICE), "Нет цены продукта"
    
    def item_name_eql_basket_name(self):
        name_of_item = self.browser.find_element(*ProductPageLocators.CHECK_NAME).text
        name_of_item_after = self.browser.find_element(*ProductPageLocators.NAME_AFTER_ADD_ITEM).text
        assert name_of_item == name_of_item_after, "Название книги в корзине не совпадает с оригинальным"

    def item_price_eql_basket_price(self):
        price_of_item = self.browser.find_element(*ProductPageLocators.CHECK_PRICE).text
        price_of_item_after = self.browser.find_element(*ProductPageLocators.PRICE_AFTER_ADD_ITEM).text
        assert price_of_item_after ==  price_of_item, "Цена книги в корзине совпадает с оригинальной"

    def success_message_appeared(self):
        assert self.is_element_present(*ProductPageLocators.WHOLE_SUCCESS_MESSAGE)
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.WHOLE_SUCCESS_MESSAGE), \
           "Сообщение об успехе ошибочно появляется"
    
    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.WHOLE_SUCCESS_MESSAGE)
        "Сообщение об успехе не появляется, хотя должно"

    def add_to_basket_button(self):
         assert self.is_element_present(*BasketPageLocators. BASKET_PAGE_BUTTON)
    
        
    
