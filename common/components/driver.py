
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from webdriver_manager.chrome import ChromeDriverManager

from .interfaces.IDriver import IDriver


class SeleniumClient(IDriver):
    def __init__(self, _sel_instance = None) -> None:
        if _sel_instance == None:
            self._sel = Chrome(service=Service(ChromeDriverManager().install()))
        else:
            self._sel = _sel_instance

    def get_element(self, by_what: tuple, time_for_wait: int = 10) -> WebElement | None:
        try:
            element = WebDriverWait(self._sel, time_for_wait).until(
                EC.presence_of_element_located(by_what)
            )
        except TimeoutException:
            return None
        else:
            return element


    def get_all_elements(self, by_what: tuple, time_for_wait: int = 10) -> list[WebElement] | None:
        try:
            element = WebDriverWait(self._sel, time_for_wait).until(
                EC.presence_of_all_elements_located(by_what)
            )
        except TimeoutException:
            return None
        else:
            return element

    def click_on_element(self, element: WebElement) -> None:
        element.click()

    def go_to_page(self, url: str) -> None:
        self._sel.get(url)

    def reload_page(self) -> None:
        self._sel.navigate().refresh()