# from django.test import TestCase

# # Create your tests here.

# import pytest
# from django.test import TestCase

# from bs4 import BeautifulSoup
# from selenium.webdriver import Chrome

# # Create your tests here.

# PITCHFORK_URL = "https://pitchfork.com/reviews/albums/?page=1"


# def test_making():
#     browser = SeleniumClient(Chrome())
#     scrubber = PitchForkScruber(browser, PITCHFORK_URL)
#     data = scrubber.update_data()

#     for case in data["data"]:
#         try:
#             record = Review(**case)
#             record.save()
#         except: 
#             pass

# def test_rv_audio():
#     ta_converter = AudioMaker()
#     txt = "Fucking hell"
#     audio_object = ta_converter.get_audio_object(txt)

#     pk =  ReviewsPage().get_latest_id()
#     record = ReviewsPage().get_record_by_pk(pk)
#     motherfuckr = ReviewAudio(review=record)
#     motherfuckr.save(audio=audio_object, name=pk)

# def test_one_positive():
#     browser = SeleniumClient(Chrome())
    
#     scrubber = PitchForkScruber(browser, PITCHFORK_URL)
#     scrubber.update_data()


# def test_two_positive():
#     html = """<div class="SplitScreenContentHeaderTitleBlock-hkbQxz kmTHjj"><div data-testid="ContentHeaderRubric"><div class="RubricWrapper-cSwECA brBvdr rubric SplitScreenContentHeaderRubric-lcYYrD iengFe"><a class="RubricLink-DDpgX kanVZ rubric__link" href="/reviews/albums/" data-uri="82c7aea0401905b54e2265f312358463"><span class="RubricName-eXGqmo bHYiSS">Albums</span></a></div></div><h1 data-testid="ContentHeaderHed" class="BaseWrap-sc-UrHlS BaseText-fFrHpW SplitScreenContentHeaderHed-fyeLMD boMZdO ZveqB jKrbpd"><em>Food for Worms</em></h1><ul class="SplitScreenContentHeaderArtistWrapper-hpQdA gOjUjm"><a href="/artists/34225-shame/" class="BaseWrap-sc-UrHlS BaseText-fFrHpW BaseLink-ha-DYir SplitScreenContentHeaderArtistLink-bpJROv boMZdO caZQdM fkewAw dYpzNU" data-uri="ae5290f138bc8d89f4f4036acad8ef27"><div class="BaseWrap-sc-UrHlS BaseText-fFrHpW SplitScreenContentHeaderArtist-lfLzFP boMZdO eLfbIf jePiWC">Shame</div></a></ul><time data-testid="SplitScreenContentHeaderReleaseYear" class="SplitScreenContentHeaderReleaseYear-gTFXAs pnGip">2023</time><div class="SocialIconsWrapper-ixiuvW ikVcrF social-icons social-icons--standard SplitScreenContentHeaderSocialShare-liOabM lbFlHr" data-event-boundary="click" data-event-click="{&quot;pattern&quot;:&quot;SocialIcons&quot;}" data-in-view="{&quot;pattern&quot;:&quot;SocialIcons&quot;}" data-include-experiments="true"><ul data-testid="socialIconslist" class="SocialIconsList-Nwcjr bFHhOT social-icons__list"><li class="SocialIconsListItem-hZqgEy ihqfrw social-icons__list-item social-icons__list-item--facebook social-icons__list-item--standard"><a aria-label="Share on Facebook" class="external-link SocialIconExternalLink-guTSJT kyIAYO social-icons__link social-icons__link--facebook" data-event-click="{&quot;element&quot;:&quot;ExternalLink&quot;,&quot;outgoingURL&quot;:&quot;https://www.facebook.com/dialog/feed?&amp;display=popup&amp;caption=Shame%3A%20Food%20for%20Worms&amp;app_id=207089362687909&amp;link=https%3A%2F%2Fpitchfork.com%2Freviews%2Falbums%2Fshame-food-for-worms%2F%3Futm_source%3Dfacebook%26utm_medium%3Dsocial%26utm_campaign%3Donsite-share%26utm_brand%3Dpitchfork%26utm_social-type%3Dearned&quot;}" href="https://www.facebook.com/dialog/feed?&amp;display=popup&amp;caption=Shame%3A%20Food%20for%20Worms&amp;app_id=207089362687909&amp;link=https%3A%2F%2Fpitchfork.com%2Freviews%2Falbums%2Fshame-food-for-worms%2F%3Futm_source%3Dfacebook%26utm_medium%3Dsocial%26utm_campaign%3Donsite-share%26utm_brand%3Dpitchfork%26utm_social-type%3Dearned" rel="nofollow noopener" target="_blank" data-uri="731aff0d1f7e8fdb1ff95469f75ee246"><div class="SocialIconContainer-fbpuVh gFIcvv social-icons__icon-container"><svg class="SocialIconNetworkIconComponent-krIrVs rrIrT icon icon-facebook" focusable="false" viewBox="0 0 32 32" width="32" height="32" fill="none" xmlns="http://www.w3.org/2000/svg"><title>Facebook</title><path d="M13.621 11.099V13.302H12V15.995H13.621V24H16.951V15.995H19.186C19.186 15.995 19.395 14.704 19.496 13.292H16.964V11.45C16.964 11.175 17.327 10.804 17.686 10.804H19.5V8H17.033C13.539 8 13.621 10.696 13.621 11.099Z" fill="black"></path></svg></div></a></li><li class="SocialIconsListItem-hZqgEy ihqfrw social-icons__list-item social-icons__list-item--email social-icons__list-item--standard"><a aria-label="Share via Email" class="external-link SocialIconExternalLink-guTSJT kyIAYO social-icons__link social-icons__link--email" data-event-click="{&quot;element&quot;:&quot;ExternalLink&quot;,&quot;outgoingURL&quot;:&quot;mailto:?subject=Shame%3A%20Food%20for%20Worms&amp;body=https%3A%2F%2Fpitchfork.com%2Freviews%2Falbums%2Fshame-food-for-worms%2F%3Futm_source%3Donsite-share%26utm_medium%3Demail%26utm_campaign%3Donsite-share%26utm_brand%3Dpitchfork&quot;}" href="mailto:?subject=Shame%3A%20Food%20for%20Worms&amp;body=https%3A%2F%2Fpitchfork.com%2Freviews%2Falbums%2Fshame-food-for-worms%2F%3Futm_source%3Donsite-share%26utm_medium%3Demail%26utm_campaign%3Donsite-share%26utm_brand%3Dpitchfork" rel="nofollow noopener" target="_blank" data-uri="6e56e37974096ec48d0c18e4243fae03"><div class="SocialIconContainer-fbpuVh gFIcvv social-icons__icon-container"><svg class="icon icon-email" focusable="false" viewBox="0 0 32 32" width="32" height="32" xmlns="http://www.w3.org/2000/svg"><title>Email</title><path d="M6 23h20V9H6v14zm3.631-12H22.37l-6.368 5.661L9.631 11zM24 12.227V21H8v-8.773l8.002 7.109L24 12.227z" fill-rule="evenodd"></path></svg></div></a></li><li class="SocialIconsListItem-hZqgEy ihqfrw social-icons__list-item social-icons__list-item--pinterest social-icons__list-item--standard"><a aria-label="Share on Pinterest" data-pin-do="nothing" class="external-link SocialIconExternalLink-guTSJT kyIAYO social-icons__link social-icons__link--pinterest" data-event-click="{&quot;element&quot;:&quot;ExternalLink&quot;,&quot;outgoingURL&quot;:&quot;https://www.pinterest.com/pin/create/button/?url=https%3A%2F%2Fpitchfork.com%2Freviews%2Falbums%2Fshame-food-for-worms%2F%3Futm_source%3Dpinterest%26utm_medium%3Dsocial%26utm_campaign%3Donsite-share%26utm_brand%3Dpitchfork%26utm_social-type%3Dearned&amp;media=https://media.pitchfork.com/photos/6373dd0f6d88ac716c39d529/1:1/w_360,c_limit/Food%20for%20Worms%20digital%20art.jpg&quot;}" href="https://www.pinterest.com/pin/create/button/?url=https%3A%2F%2Fpitchfork.com%2Freviews%2Falbums%2Fshame-food-for-worms%2F%3Futm_source%3Dpinterest%26utm_medium%3Dsocial%26utm_campaign%3Donsite-share%26utm_brand%3Dpitchfork%26utm_social-type%3Dearned&amp;media=https://media.pitchfork.com/photos/6373dd0f6d88ac716c39d529/1:1/w_360,c_limit/Food%20for%20Worms%20digital%20art.jpg" rel="nofollow noopener" target="_blank" data-uri="f0001c049e1d532af45c78f36fc649db"><div class="SocialIconContainer-fbpuVh gFIcvv social-icons__icon-container"><svg class="SocialIconNetworkIconComponent-krIrVs rrIrT icon icon-pinterest" focusable="false" viewBox="0 0 32 32" width="32" height="32" fill="none" xmlns="http://www.w3.org/2000/svg"><title>Pinterest</title><path d="M15.169 18.448C14.793 20.093 14.425 21.678 13.623 22.928C13.377 23.311 13.13 23.793 12.71 24C12.09 20.807 13.387 18.12 13.899 15.436C13.246 14.103 13.652 11.846 15.051 11.59C17.077 11.22 16.543 13.664 16.2 14.8C16.01 15.424 15.671 16.021 15.722 16.705C15.835 18.146 17.648 18.24 18.577 17.497C19.909 16.436 20.295 14.385 20.164 12.7C19.967 10.135 17.062 8.85997 14.496 9.88497C13.173 10.413 11.973 11.628 11.799 13.413C11.709 14.353 11.906 15.104 12.276 15.634C12.331 15.715 12.523 15.857 12.552 16.072C12.61 16.506 12.352 16.974 12.116 17.298C10.802 16.92 10.124 15.741 10.016 14.248C9.76596 10.848 12.558 8.26397 15.841 8.02197C19.348 7.76497 22.126 9.78896 22.384 12.74C22.576 14.933 21.797 17.14 20.561 18.329C19.631 19.221 17.656 20.096 16.041 19.242C15.684 19.052 15.524 18.82 15.169 18.448Z" fill="black"></path></svg></div></a></li></ul></div></div>"""

#     browser = SeleniumClient()
#     scrubber = PitchForkScruber(browser, PITCHFORK_URL)

#     assert scrubber._get_text_data_of_review(html) == {"title": "Food for Worms", "author": "Shame", "year": "2023"}


# def test_three_positive():
#     html = """<div class="SplitScreenContentHeaderLeadWrapper-hRNksR eEPSno"><div data-testid="ContentHeaderLeadAsset" class="SplitScreenContentHeaderLedeBlock-gzOQYf ipXZGD"><span class="SpanWrapper-kGOugJ QEGhz responsive-asset SplitScreenContentHeaderLede-dguJnW VhKZz"><picture class="ResponsiveImagePicture-jJyKit mrcDn SplitScreenContentHeaderLede-dguJnW VhKZz responsive-image"><source media="(max-width: 767px)" srcset="https://media.pitchfork.com/photos/6373dd0f6d88ac716c39d529/1:1/w_120,c_limit/Food%20for%20Worms%20digital%20art.jpg 120w, https://media.pitchfork.com/photos/6373dd0f6d88ac716c39d529/1:1/w_240,c_limit/Food%20for%20Worms%20digital%20art.jpg 240w, https://media.pitchfork.com/photos/6373dd0f6d88ac716c39d529/1:1/w_320,c_limit/Food%20for%20Worms%20digital%20art.jpg 320w" sizes="100vw"><source media="(min-width: 768px)" srcset="https://media.pitchfork.com/photos/6373dd0f6d88ac716c39d529/1:1/w_120,c_limit/Food%20for%20Worms%20digital%20art.jpg 120w, https://media.pitchfork.com/photos/6373dd0f6d88ac716c39d529/1:1/w_240,c_limit/Food%20for%20Worms%20digital%20art.jpg 240w, https://media.pitchfork.com/photos/6373dd0f6d88ac716c39d529/1:1/w_320,c_limit/Food%20for%20Worms%20digital%20art.jpg 320w" sizes="100vw"><img alt="Shame Food for Worms" class="ResponsiveImageContainer-dmlCKO hWKgYV responsive-image__image" src="https://media.pitchfork.com/photos/6373dd0f6d88ac716c39d529/1:1/w_450%2Cc_limit/Food%2520for%2520Worms%2520digital%2520art.jpg"></picture></span></div><div class="SplitScreenContentHeaderScoreBox-eOKJab gUzFzM"><div class="ScoreBoxWrapper-cqxrzg hvtCii"><div class="ScoreCircle-cIILhI hUIQbu"><p class="BaseWrap-sc-UrHlS BaseText-fFrHpW Rating-cIWDua boMZdO ehZJoO bGSqyX">7.7</p></div></div></div></div>"""

#     browser = SeleniumClient()
#     scrubber = PitchForkScruber(browser)
#     output_image_src ="https://media.pitchfork.com/photos/6373dd0f6d88ac716c39d529/1:1/w_450%2Cc_limit/Food%2520for%2520Worms%2520digital%2520art.jpg"

#     assert scrubber._get_image_of_review(html) == {"image_src": output_image_src, "album_score": "7.7"}

# def test_four_positive():
#     browser = SeleniumClient()
#     scrubber = PitchForkScruber(browser)
#     scrubber._test_shit()