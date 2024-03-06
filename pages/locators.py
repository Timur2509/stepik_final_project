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