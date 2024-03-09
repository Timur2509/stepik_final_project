from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def no_items_in_basket(self):
        assert self.is_not_element_present(
            *BasketPageLocators.ITEMS_IN_BASKET), "В корзине есть товары, хотя не должны быть!"    

    def basket_is_empty_message_check(self):
        assert self.is_element_present(
            *BasketPageLocators.BASKET_IS_EMPTY_MESSAGE), "Нет сообщения о пустой корзине"
    




