import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec


class Large_download:

    # Xpath
    url="https://ash-speed.hetzner.com/"
    chrome_icon_xp='//android.widget.TextView[@content-desc="Chrome"]'
    search_textbox_xp='//android.widget.EditText[@resource-id="com.android.chrome:id/search_box_text"]'
    searched_item_xp='//android.widget.TextView[@resource-id="com.android.chrome:id/line_1" and @text="Test Files"]'
    ten_b_file_xp='//android.widget.TextView[@text="10GB.bin"]'
    more_options_xp='//android.widget.ImageButton[@content-desc="Customise and control Google Chrome"]'
    download_options_xp='//android.widget.LinearLayout[@resource-id="com.android.chrome:id/downloads_menu_id"]'
    pause_resume_btn_xp='//android.widget.ImageButton[@content-desc="Pause" or @content-desc="Resume"]'
    check_paused_or_dwnloading='//android.widget.TextView[@resource-id="com.android.chrome:id/caption"]'

    def __init__(self,driver):
        self.driver=driver


    def big_file_download(self,url):
        self.driver.find_element(AppiumBy.XPATH,self.chrome_icon_xp).click()
        time.sleep(1)
        self.driver.find_element(AppiumBy.XPATH,self.search_textbox_xp).send_keys(url)
        time.sleep(1)
        self.driver.find_element(AppiumBy.XPATH,self.searched_item_xp).click()
        time.sleep(3)
        self.driver.find_element(AppiumBy.XPATH,self.ten_b_file_xp).click()
    def check_file_download(self):
        self.driver.find_element(AppiumBy.XPATH,self.more_options_xp).click()
        time.sleep(1)
        self.driver.find_element(AppiumBy.XPATH,self.download_options_xp).click()
        time.sleep(2)
        try:
            download_icon=self.driver.find_element(AppiumBy.XPATH,self.pause_resume_btn_xp)
            if download_icon.is_dispalayed():
                downloadconfirm=self.driver.find_element(AppiumBy.XPATH,self.check_paused_or_dwnloading).text
                phrase = "paused"
                if phrase not in downloadconfirm:
                    print("pass the test")
                else:
                    print ("video download paused")

        except NoSuchElementException:
            print("Dowwnloading is not started")





