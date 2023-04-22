
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException

from webdriver_manager.chrome import ChromeDriverManager

from reviews.components.interfaces.IDriverAdapter import IDriverAdapter

from logging import getLogger

log = getLogger(__name__)


class SeleniumAdapter(IDriverAdapter):
    def __init__(self, _sel_instance=None) -> None:        
        if _sel_instance is None:
            options = Options()
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')

            self._sel = Chrome(
                service=Service(
                    ChromeDriverManager().install()), options=options)
        else:
            self._sel = _sel_instance

    def get_element(
            self,
            by_what: tuple, time_for_wait: int = 3) -> WebElement | None:

        try:
            element = WebDriverWait(self._sel, time_for_wait).until(
                EC.presence_of_element_located(by_what)
            )
        except TimeoutException as E:
            log.warning(E)
        else:
            return element

    def get_all_elements(
            self,
            by_what: tuple, time_for_wait: int = 3) -> list[WebElement] | None:

        try:
            element = WebDriverWait(self._sel, time_for_wait).until(
                EC.presence_of_all_elements_located(by_what)
            )
        except TimeoutException as E:
            log.warning(E)
        else:
            return element

    def click_on_element(self, element: WebElement) -> None:
        try:
            element.click()
        except WebDriverException as E:
            log.warning(E)
        finally:
            return None

    def go_to_page(self, url: str, page_load_time_out: int = None) -> None:
        if page_load_time_out is not None:
            self._sel.set_page_load_timeout(page_load_time_out)

        try:
            if page_load_time_out is None:
                self._sel.implicitly_wait(5)
                self._sel.set_page_load_timeout(300)

            self._sel.get(url)
        except WebDriverException as E:

            self._sel.execute_script("window.stop();")
            log.warning(E)
        finally:
            return None

    def reload_page(self) -> None:
        try:
            self._sel.navigate().refresh()
        except WebDriverException as E:
            log.warning(E)
        finally:
            return None

    def close(self) -> None:
        try:
            self._sel.close()
        except BaseException:
            pass

        try:
            self._sel.quit()
        except BaseException:
            pass
