from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        """Конструктор ключевым словом super на самом деле только вызывает конструктор класса предка
        и передает ему все те аргументы, которые мы передали в конструктор MainPage"""
        super(MainPage, self).__init__(*args, **kwargs)
