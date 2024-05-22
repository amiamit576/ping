from appium import webdriver
from appium.options.android import UiAutomator2Options
import pytest

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    udid='1a565c34',
    ignoreHiddenApiPolicyError = 'true',
    noReset = 'true'
      )
appium_server_url = 'http://localhost:4723'

@pytest.fixture()
def setup():

    driver=webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
    return driver

capabilitie = dict(
    platformName='Android',
    automationName='uiautomator2',
    udid='d695bb5d',
    ignoreHiddenApiPolicyError = 'true',
    noReset = 'true'
      )
appium_ser_url = 'http://localhost:4723'

@pytest.fixture()
def setup2():

    driver2=webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilitie))
    return driver2

