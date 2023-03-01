
from bs4 import BeautifulSoup
from bs4 import Comment

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

from .interfaces.IScruber import IScruber
from .interfaces.IDriver import IDriverAdapter
from .driver import SeleniumClient


class PitchForkScruber(IScruber):
    def __init__(self, driver: SeleniumClient, home_url: str = None) -> None:
        if not isinstance(driver, IDriverAdapter):
            raise TypeError("driver should have IDriver interface")
        
        if home_url is not None:
            if not isinstance(home_url, str):
                raise TypeError("home url should be string")
        else:
            home_url = "https://pitchfork.com/reviews/albums/?page=1"

        self.__driver = driver
        self.__root = "https://pitchfork.com"
        self.__home_path = home_url

        self.__buffer = {
            "list_of_urls": None,
            "data": []
        }

    def update_data(self) -> None:
        self.__clear_buffer()

        self.__driver.go_to_page(self.__home_path)
        review_cards = self.__driver.get_all_elements((By.CLASS_NAME, "review"))[:12]
        
        self.__update_all_links(review_cards)
        self.__get_all_information_about_each_review()

    def get_actual_data(self):
        return self.__buffer

    def __clear_buffer(self):
        self.__buffer.clear()
        self.__buffer = {
            "list_of_urls": None,
            "data": []
        }

    def __update_all_links(self, cards: list[WebElement]) -> None:        
        links = []
        for card in cards:
            html = card.get_attribute('innerHTML')
            a_tag = BeautifulSoup(html, features="html.parser").find("a", {"class": "review__link"})
            links.append(f"{self.__root}{a_tag['href']}")

        self.__buffer['list_of_urls'] = links

    def __get_all_information_about_each_review(self) -> None:

        for link in self.__buffer['list_of_urls']:
            self.__driver.go_to_page(link)

            try:
                items = self.__driver.get_all_elements(
                    (By.CSS_SELECTOR,
                    ".GridItem-bwmuQH.bpJgOF.grid--item")
                )
                title_of_review = self.__driver.get_all_elements(
                    (By.CSS_SELECTOR, 
                    ".BaseWrap-sc-UrHlS.BaseText-fFrHpW.SplitScreenContentHeaderDekDown-fkATUS.boMZdO.eLfbIf.fZZtlk"))
                actual_review_text = self.__driver.get_all_elements(
                    (By.CSS_SELECTOR, 
                    ".BodyWrapper-csjEHZ.drLwOj.body.body__container.article__body"))

                actual_review_text = [el.get_attribute('innerHTML') for el in actual_review_text]
                title_of_review = title_of_review[0].get_attribute('innerHTML')
                names_container = items[0].get_attribute('innerHTML')
                image_container = items[1].get_attribute('innerHTML')
            except:
                print("Problem with container!!!!!!!!!!!!")
            else:
                data = dict()
                data.update(self.__get_text_data_of_review(names_container))
                data.update(self.__get_image_of_review(image_container))
                data.update(self.__get_title_of_review(title_of_review))
                data.update(self.__get_review_text(actual_review_text))
                self.__buffer["data"].append(data)
    
    def __get_text_data_of_review(self, html: str) -> dict:
        soup = BeautifulSoup(html, features="html.parser")

        album_title = soup.contents[0].contents[1].contents[0].contents[0]
        author = soup.contents[0].contents[2].contents[0].contents[0].contents[0]
        year = soup.contents[0].contents[3].contents[0]
        del soup

        return {"album_title": album_title, "album_author": author, "album_year": year}
    
    def __get_image_of_review(self, html: str) -> dict:
        soup = BeautifulSoup(html, features="html.parser")

        src = soup.contents[0].contents[0].contents[0].contents[0].contents[2]['src']
        score = soup.contents[0].contents[1].contents[0].contents[0].contents[0].contents[0]

        return {"image_src": src, "album_score": score}
    
    def __get_title_of_review(self, html: str) -> dict:
        soup = BeautifulSoup(html, features="html.parser")
        review_title = soup.contents[0]

        return {"review_title": review_title}
    
    def __get_review_text(self, review_text: list[str]) -> dict:
        def tag_visible(element):
            if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
                return False
            if isinstance(element, Comment):
                return False
            return True
        
        output_text = ""

        for html in review_text:
            soup = BeautifulSoup(html, features="html.parser")
            
            data = soup.find_all(string=True)
            visible_text = filter(tag_visible, data)
            output = u" ".join(t.strip() for t in visible_text)
            output = output.split("All products featured on Pitchfork are independently selected by our editors.")[0]
            output_text = output_text + output

        return {"review_text": output_text}
