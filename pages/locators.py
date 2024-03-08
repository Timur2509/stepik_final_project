from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#registration-email")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#registration-password1")
    PASSWORD_CHECK = (By.CSS_SELECTOR, "#registration-password2")
    SUBMIT_BUTTON = (By.NAME,"registration_submit")

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    CHECK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    CHECK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    NAME_AFTER_ADD_ITEM = (By.CSS_SELECTOR,".alert-success:first-child .alertinner strong")
    PRICE_AFTER_ADD_ITEM = (By.CSS_SELECTOR,".alert-info .alertinner strong")
    WHOLE_SUCCESS_MESSAGE = (By.CSS_SELECTOR,".alert-safe.alert-noicon")


