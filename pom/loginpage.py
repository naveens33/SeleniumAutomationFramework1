from selenium.webdriver.common.by import By
from pom.basepage import BasePage


class LoginPage(BasePage):
    _username_field = By.ID, "user_login"
    _password_field = By.ID, "user_password"
    _sign_in_button = By.NAME, "submit"

    def do_login(self,username,password):
        self._enter_text(self._username_field,username)
        self._enter_text(self._password_field, password)
        self._click(self._sign_in_button)
        #just to pass the login
        self.driver.get('http://zero.webappsecurity.com/bank/account-summary.html')



