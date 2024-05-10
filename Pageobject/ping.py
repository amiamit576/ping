import time

from appium import  webdriver
from appium.webdriver.common.appiumby import  AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as Ec

class Ping_Action:
    # locator
    # ping Xpath
    Search_box_Xp = '//android.widget.AutoCompleteTextView[@resource-id="com.android.launcher:id/search_src_text"]'
    ping_xp = '//android.widget.TextView[@content-desc="Ping"]'
    ping_setting_xp = '//android.widget.ToggleButton[@resource-id="com.lipinic.ping:id/btnSettings"]'
    ping_button_xp = '//android.widget.Button[@resource-id="com.lipinic.ping:id/btnStartPing"]'
    packet_size_xp = '//android.widget.EditText[@resource-id="com.lipinic.ping:id/editTextPacketSize"]'
    ping_result_display_xp = '//android.widget.TextView[@resource-id="com.lipinic.ping:id/txtResult"]'
    ping_history_result_option = '//android.widget.TextView[@resource-id="android:id/title" and @text="HISTORY"]'
    ping_hisory_current_xp = '(//android.widget.RelativeLayout[@resource-id="com.lipinic.ping:id/rlvItem"])[1]'

    # in case of Add Display
    skip_vedio_Xp = '//android.widget.TextView[@resource-id="com.lipinic.ping:id/txtResult"]'
    cross_x_xp = '//android.widget.Button'
    # result page
    result_page_Xp = '//android.widget.ImageView[@content-desc="More options"]'
    result_share_Xp = '//android.widget.TextView[@resource-id="com.lipinic.ping:id/title"]'
    result_share_app = '//android.widget.TextView[@resource-id="android:id/text1" and @text="Gmail"]'

    def __init__(self,driver):
        self.driver=driver


    def ping_start(self):

        try:
            self.driver.find_element(AppiumBy.XPATH,self.ping_xp).click()
        except:
            self.driver.swipe(523, 2308, 523, 686)
            time.sleep(1)
            self.driver.find_element(AppiumBy.XPATH, self.Search_box_Xp).send_keys('Ping')
            self.driver.find_element(AppiumBy.XPATH, self.ping_xp).click()
        self.driver.find_element(AppiumBy.XPATH,self.ping_setting_xp).click()
        time.sleep(1)

        try:
            packet_size = self.driver.find_element(AppiumBy.XPATH, self.packet_size_xp)
            if packet_size.is_displayed():
                packet_size.clear()
                time.sleep(1)
                packet_size.send_keys('1024')
        except:
                print("Packet  size Already  set")

        time.sleep(1)
        Ping_btn=self.driver.find_element(AppiumBy.XPATH,self.ping_button_xp)
        ping_txt=Ping_btn.text
        if ping_txt =="STOP":
            Ping_btn.click()
            Ping_btn.click()
        else:
            Ping_btn.click()

        time.sleep(5)
        print("Ping is started")
        self.driver.execute_script('mobile: pressKey', {"keycode": 3})
