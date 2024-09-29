from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, be, have
from utils.allure_attachs import attach_screenshot

def test_open_article():
    with step('First onboarding page'):
        attach_screenshot()
        browser.element((AppiumBy.ID, 'org.wikipedia:id/primaryTextView')).should(
            have.exact_text('The Free Encyclopedia\n…in over 300 languages'))
        browser.element((AppiumBy.ID, 'org.wikipedia:id/fragment_onboarding_skip_button')).should(be.visible)
        browser.element((AppiumBy.ID, 'org.wikipedia:id/fragment_onboarding_forward_button')).should(
            have.exact_text('Continue'))
        browser.element((AppiumBy.ID, 'org.wikipedia:id/fragment_onboarding_forward_button')).click()

    with step('Second onboarding page'):
        attach_screenshot()
        browser.element((AppiumBy.ID, 'org.wikipedia:id/primaryTextView')).should(
            have.exact_text('New ways to explore'))
        browser.element((AppiumBy.ID, 'org.wikipedia:id/fragment_onboarding_skip_button')).should(be.visible)
        browser.element((AppiumBy.ID, 'org.wikipedia:id/fragment_onboarding_forward_button')).should(
            have.exact_text('Continue'))
        browser.element((AppiumBy.ID, 'org.wikipedia:id/fragment_onboarding_forward_button')).click()

    with step('Third onboarding page'):
        attach_screenshot()
        browser.element((AppiumBy.ID, 'org.wikipedia:id/primaryTextView')).should(
            have.exact_text('Reading lists with sync'))
        browser.element((AppiumBy.ID, 'org.wikipedia:id/fragment_onboarding_skip_button')).should(be.visible)
        browser.element((AppiumBy.ID, 'org.wikipedia:id/fragment_onboarding_forward_button')).should(
            have.exact_text('Continue'))
        browser.element((AppiumBy.ID, 'org.wikipedia:id/fragment_onboarding_forward_button')).click()

    with step('Fourth onboarding page'):
        attach_screenshot()
        browser.element((AppiumBy.ID, 'org.wikipedia:id/primaryTextView')).should(
            have.exact_text('Data & Privacy'))
        browser.element((AppiumBy.ID, 'org.wikipedia:id/fragment_onboarding_done_button')).should(
            have.exact_text('Get started'))
        browser.element((AppiumBy.ID, 'org.wikipedia:id/fragment_onboarding_done_button')).click()

    with step('Type search'):
        attach_screenshot()
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia:id/search_src_text")).type('Capibara')

    with step('Open first article'):
        attach_screenshot()
        results = browser.all((AppiumBy.ID, 'org.wikipedia:id/page_list_item_title'))
        results.first.click()
        browser.element((AppiumBy.CLASS_NAME, 'android.view.View')).should(have.text('Capybara'))
