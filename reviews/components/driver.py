
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException

from webdriver_manager.chrome import ChromeDriverManager

from .interfaces.IDriver import IDriverAdapter


class SeleniumClient(IDriverAdapter):
    def __init__(self, _sel_instance = None) -> None:
        if _sel_instance == None:
            self._sel = Chrome(service=Service(ChromeDriverManager().install()))
        else:
            self._sel = _sel_instance

    def get_element(
        self, 
        by_what: tuple, time_for_wait: int = 10) -> WebElement | None:
        
        try:
            element = WebDriverWait(self._sel, time_for_wait).until(
                EC.presence_of_element_located(by_what)
            )
        except TimeoutException:
            return None
        else:
            return element

    def get_all_elements(
        self, 
        by_what: tuple, time_for_wait: int = 10) -> list[WebElement] | None:
        
        try:
            element = WebDriverWait(self._sel, time_for_wait).until(
                EC.presence_of_all_elements_located(by_what)
            )
        except TimeoutException:
            return None
        else:
            return element

    def click_on_element(self, element: WebElement) -> None:
        try:
            element.click()
        except WebDriverException:
            pass
        finally:
            return None

    def go_to_page(self, url: str) -> None:
        try:
            self._sel.get(url)
        except WebDriverException:
            pass
        finally:
            return None

    def reload_page(self) -> None:
        try:
            self._sel.navigate().refresh()
        except WebDriverException:
            pass
        finally:
            return None

    def close(self) -> None:
        try:
            self._sel.close()
        except:
            pass

        try:
            self._sel.quit()
        except:
            pass
        