from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_CHECK = (By.CSS_SELECTOR, "#id_registration-password2")
    SUBMIT_BUTTON = (By.NAME,"registration_submit")

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    CHECK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    CHECK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    NAME_AFTER_ADD_ITEM = (By.CSS_SELECTOR,".alert-success:first-child .alertinner strong")
    PRICE_AFTER_ADD_ITEM = (By.CSS_SELECTOR,".alert-info .alertinner strong")
    WHOLE_SUCCESS_MESSAGE = (By.CSS_SELECTOR,".alert-safe.alert-noicon")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_PAGE_BUTTON = (By.CSS_SELECTOR, ".basket-mini a.btn-default")
    BASKET_IS_EMPTY_MESSAGE = (By.CSS_SELECTOR,"#content_inner")
    ITEMS_IN_BASKET = (By.CSS_SELECTOR,".basket-items")