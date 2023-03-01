
from __future__ import absolute_import, unicode_literals

from selenium.webdriver import Chrome
from celery import shared_task

from .components.driver import SeleniumClient
from .components.pitchfork import PitchForkScruber
from .models import Review


@shared_task
def update():
    PITCHFORK_URL = "https://pitchfork.com/reviews/albums/?page=1"
    
    browser = SeleniumClient(Chrome())
    scrubber = PitchForkScruber(browser, PITCHFORK_URL)
    scrubber.update_data()
    data = scrubber.get_actual_data()

    for case in data["data"]:
        try:
            record = Review(**case)
            record.save()
        except: 
            pass
    
    browser.close()