
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox

from reviews.components.interfaces.IBuilder import IBuilder
from reviews.components.interfaces.IDriverAdapter import IDriverAdapter
from reviews.components.selenium_adapter import SeleniumAdapter
from reviews.components.pitchfork_scruber import PitchForkScruber


class PitchFScrubberBuilder(IBuilder):
    def _build_driver(self) -> IDriverAdapter:
        selenium = SeleniumAdapter(Firefox())
        return selenium

    def _build_scrubber(self, driver: IDriverAdapter) -> PitchForkScruber:
        scrubber = PitchForkScruber(driver)
        return scrubber
    
    def build(self) -> PitchForkScruber:
        driver = self._build_driver()
        scrubber = self._build_scrubber(driver)

        return scrubber
