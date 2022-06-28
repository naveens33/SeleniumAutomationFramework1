from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    #def __init__(self, driver):
    #    self.driver = driver

    def _click(self, locator):
        element = self.driver.find_element(*locator)
        self._highlight(element)
        element.click()

    def _enter_text(self, locator, text):
        element = self.driver.find_element(*locator)
        self._highlight(element)
        element.send_keys(text)

    def _find_elements(self,locator):
        return self.driver.find_elements(*locator)

    def _highlight(self, element):
        self.driver.execute_script("arguments[0].setAttribute('style','border: 2px solid red;');", element)

    def _wait_for_element(self, locator, expected_condition, timeout=5):
        wait = WebDriverWait(self.driver, timeout)
        if expected_condition == "visibility":
            return wait.until(EC.visibility_of_element_located(locator))
        elif expected_condition == "invisibility":
            return wait.until(EC.invisibility_of_element_located(locator))
        else:
            pass
