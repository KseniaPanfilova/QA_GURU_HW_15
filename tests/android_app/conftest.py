import allure
import allure_commons
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selene import browser, support
from utils.allure_attachs import attach_screenshot, attach_screen_xml_dump
import project


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    # options = UiAutomator2Options().load_capabilities({
    #     'appium:udid': project.config.udid,
    #     'appium:ignoreHiddenApiPolicyError': project.config.ignoreHiddenApiPolicyError,
    #     'appium:app': project.config.app,
    #     'appium:appWaitActivity': project.config.appWaitActivity,
    # }
    # )
    #
    # browser.config.driver_remote_url = project.config.remote_url
    # browser.config.driver_options = options
    with allure.step('init app session'):
        browser.config.driver = webdriver.Remote(
            project.config.remote_url,
            options=project.config.to_driver_options()
        )
    browser.config.timeout = project.config.timeout

    browser.config._wait_decorator = support._logging.wait_with(context=allure_commons._allure.StepContext)

    yield

    attach_screenshot()

    attach_screen_xml_dump()

    browser.quit()
