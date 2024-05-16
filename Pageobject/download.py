import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec


class Large_download:

    # Xpath

    chrome_icon_xp='//android.widget.TextView[@content-desc="Chrome"]'
    add_tab_xp='//android.widget.ImageButton[@content-desc="Switch or close tabs"]'
    open_new_tab='//android.widget.TextView[@resource-id="com.android.chrome:id/new_tab_view_desc"]'
    search_textbox_xp='//android.widget.EditText[@resource-id="com.android.chrome:id/search_box_text"]'
    searched_item_xp='//android.widget.TextView[@resource-id="com.android.chrome:id/line_1" and @text="Test Files"]'
    download_details_xp='//android.widget.Button[@resource-id="com.android.chrome:id/message_primary_button"]'
    ten_b_file_xp='//android.widget.TextView[@text="10GB.bin"]'
    dowload_again_Uiautomator='new UiSelector().resourceId("com.android.chrome:id/positive_button")'
    download_again_xp='//android.widget.Button[@resource-id="com.android.chrome:id/positive_button"]'
    more_options_xp='//android.widget.ImageButton[@content-desc="Customise and control Google Chrome"]'
    download_options_xp='//android.widget.LinearLayout[@resource-id="com.android.chrome:id/downloads_menu_id"]'
    pause_resume_btn_xp='//android.widget.ImageButton[@content-desc="Pause" or @content-desc="Resume"]'
    check_paused_or_dwnloading='//android.widget.TextView[@resource-id="com.android.chrome:id/caption"]'

    def __init__(self,driver):
        self.driver=driver


    def big_file_download(self,url):
        self.driver.find_element(AppiumBy.XPATH,self.chrome_icon_xp).click()
        time.sleep(2)
        self.driver.find_element(AppiumBy.XPATH,self.add_tab_xp).click()
        time.sleep(2)
        self.driver.find_element(AppiumBy.XPATH,self.open_new_tab).click()
        time.sleep(1)
        self.driver.find_element(AppiumBy.XPATH,self.search_textbox_xp).send_keys(url)
        time.sleep(1)
        self.driver.find_element(AppiumBy.XPATH,self.searched_item_xp).click()
        try:
            file_download=WebDriverWait(self.driver,10)
            file_download.until(Ec.visibility_of_element_located((AppiumBy.XPATH,self.ten_b_file_xp)))
            self.driver.find_element(AppiumBy.XPATH,self.ten_b_file_xp).click()




        except NoSuchElementException:
             time.sleep(1)
             print("download  element  not appear")

        try:
            downloadAgain_options_appear =WebDriverWait(self.driver,60)
            downloadAgain_options_appear.until(Ec.visibility_of_any_elements_located((AppiumBy.ANDROID_UIAUTOMATOR,self.dowload_again_Uiautomator)))
            self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,self.dowload_again_Uiautomator).click()
        except (NoSuchElementException,TimeoutException):
            if TimeoutException:
                print("To much time taking to download")
            else:
                print("Downloading first time")
    def check_file_download(self):

        try:
            self.driver.find_element(AppiumBy.XPATH,self.download_details_xp).click()

        except:

            self.driver.find_element(AppiumBy.XPATH,self.more_options_xp).click()
            time.sleep(2)
            self.driver.find_element(AppiumBy.XPATH,self.download_options_xp).click()
            time.sleep(2)

        try:
            download_icon=self.driver.find_element(AppiumBy.XPATH,self.pause_resume_btn_xp)
            if download_icon.is_displayed():
                downloadconfirm=self.driver.find_element(AppiumBy.XPATH,self.check_paused_or_dwnloading).text
                phrase = "paused"
                if phrase not in downloadconfirm:
                    print("pass the test")
                else:
                    print ("video download paused")

        except NoSuchElementException:
            print("Downloading is not started")


        self.driver.back()
        self.driver.execute_script('mobile: pressKey', {"keycode": 3})
        self.driver.back()






