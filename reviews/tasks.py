from __future__ import absolute_import, unicode_literals

from .components.driver import SeleniumClient
from .components.pitchfork import PitchForkScruber
from selenium.webdriver import Chrome
from .models import Review

from celery import shared_task


@shared_task
def add(x, y):
    return x + y

@shared_task
def update():
    PITCHFORK_URL = "https://pitchfork.com/reviews/albums/?page=1"
    browser = SeleniumClient(Chrome())
    scrubber = PitchForkScruber(browser, PITCHFORK_URL)
    data = scrubber.update_data()

    for case in data["data"]:
        try:
            record = Review(**case)
            record.save()
        except: 
            pass