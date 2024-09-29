import allure
import allure_commons
import pytest
import requests
from appium.options.android import UiAutomator2Options
from appium.webdriver import webdriver
from selene import browser, support
from utils.allure_attachs import attach_screenshot, attach_screen_xml_dump
import project


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = UiAutomator2Options().load_capabilities({
        "appium:udid": "emulator-5554",
        "appium:ignoreHiddenApiPolicyError": "true",
        "appium:app": "C:\\Users\\1111\\Downloads\\wikipedia.apk",
        "appium:appWaitActivity": "*",
        }
    )

    browser.config.driver_remote_url = project.config.remote_url
    browser.config.driver_options = options
    browser.config.timeout = project.config.timeout

    browser.config._wait_decorator = support._logging.wait_with(context=allure_commons._allure.StepContext)

    yield

    attach_screenshot()

    attach_screen_xml_dump()

    # session_id = browser.driver.session_id

    browser.quit()

    # response = requests.get(
    #     f'https://api.browserstack.com/app-automate/sessions/{session_id}.json',
    #     auth=(project.config.userName, project.config.accessKey),
    # ).json()
    #
    # video_url = response['automation_session']['video_url']
    #
    # allure.attach(
    #     '<html><body>'
    #     '<video width="100%" height="100%" controls autoplay>'
    #     f'<source src="{video_url}" type="video/mp4">'
    #     '</video>'
    #     '</body></html>',
    #     name='video recording',
    #     attachment_type=allure.attachment_type.HTML,
    # )
