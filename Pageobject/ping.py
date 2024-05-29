import time

from appium import  webdriver
from appium.webdriver.common.appiumby import  AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as Ec





class Ping_Action:
    # locator
    # ping Xpath
    Search_box_Xp = '//android.widget.AutoCompleteTextView[@resource-id="com.android.launcher:id/search_src_text"]'
    ping_xp = '//android.widget.TextView[@content-desc="Ping"]'
    ping_resultp_btn_xp='//android.widget.TextView[@resource-id="android:id/title" and @text="PING"]'
    ping_setting_xp = '//android.widget.ToggleButton[@resource-id="com.lipinic.ping:id/btnSettings"]'
    ping_button_xp = '//android.widget.Button[@resource-id="com.lipinic.ping:id/btnStartPing"]'
    packet_size_xp = '//android.widget.EditText[@resource-id="com.lipinic.ping:id/editTextPacketSize"]'
    ping_result_display_xp = '//android.widget.TextView[@resource-id="com.lipinic.ping:id/txtResult"]'
    ping_history_result_option = '//android.widget.TextView[@resource-id="android:id/title" and @text="HISTORY"]'
    ping_hisory_current_xp = '(//android.widget.RelativeLayout[@resource-id="com.lipinic.ping:id/rlvItem"])[1]'


    # in case of Add Display
    close_add_xp='//android.widget.TextView[@text="CLOSE"]'
    skip_vedio_Xp = '//android.widget.TextView[@resource-id="com.lipinic.ping:id/txtResult"]'
    skip_vedio_alternate_Xp="//android.widget.Button"

    cross_x_xp = '//android.widget.Button'
    # result page
    result_full_xp='//android.widget.TextView[@resource-id="com.lipinic.ping:id/txtDetail"]'
    result_page_moreoption_xp = '//android.widget.ImageView[@content-desc="More options"]'
    result_share_Xp = '//android.widget.TextView[@resource-id="com.lipinic.ping:id/title"]'
    result_share_alternate_xp='//android.widget.TextView[@text="Share"]'
    result_share_app = '//android.widget.TextView[@resource-id="android:id/text1" and @text="Gmail"]'
    gmail_mail_txt_Xp='//android.view.ViewGroup[@resource-id="com.google.android.gm:id/peoplekit_autocomplete_chip_group"]/android.widget.EditText'
    gmail_send_button='//android.widget.Button[@content-desc="Send"]'
    inertial_close_button='//android.widget.ImageButton[@content-desc="Interstitial close button"]'




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


    def ping_withoutAdd(self,mail):
        self.driver.find_element(AppiumBy.XPATH,self.result_page_moreoption_xp).click()
        time.sleep(2)
        try:
            self.driver.find_element(AppiumBy.XPATH, self.result_share_Xp).click()
        except NoSuchElementException:
            print("try alternate option")
            self.driver.find_element(AppiumBy.XPATH, self.result_share_alternate_xp).click()

        self.driver.find_element(AppiumBy.XPATH, self.result_share_app).click()
        time.sleep(2)
        self.driver.find_element(AppiumBy.XPATH, self.gmail_mail_txt_Xp).send_keys(mail)
        time.sleep(2)
        self.driver.find_element(AppiumBy.XPATH, self.gmail_send_button).click()
        time.sleep(1)
        self.driver.back()
        self.driver.find_element(AppiumBy.XPATH, self.ping_resultp_btn_xp).click()
        self.driver.back()

    def check_resultpage(self,mail):
        result = self.driver.find_element(AppiumBy.XPATH, self.result_full_xp)
        if result.is_displayed():
            self.ping_withoutAdd(mail)
        else:
            print("Result  page not displayed")


    def ping_stop(self,mail):
        try:
            self.driver.find_element(AppiumBy.XPATH,self.ping_xp).click()
        except:
            self.driver.swipe(523, 2308, 523, 686)
            time.sleep(1)
            self.driver.find_element(AppiumBy.XPATH, self.Search_box_Xp).send_keys('Ping')
            self.driver.find_element(AppiumBy.XPATH, self.ping_xp).click()

        self.driver.find_element(AppiumBy.XPATH,self.ping_button_xp).click()
        self.driver.find_element(AppiumBy.XPATH,self.ping_history_result_option).click()
        time.sleep(3)
        self.driver.find_element(AppiumBy.XPATH,self.ping_hisory_current_xp).click()
        time.sleep(5)
        try:
            # result page is opening
            self.check_resultpage(mail)

        except NoSuchElementException:
            waitt0EndAdd=WebDriverWait(self.driver,60)

            try:
                waitt0EndAdd.until(Ec.visibility_of_element_located((AppiumBy.XPATH, self.inertial_close_button)))
                another_cross=self.driver.find_element(AppiumBy.XPATH, self.inertial_close_button)
                another_cross.click()



            except(NoSuchElementException,TimeoutError):
                close_element = self.driver.find_element(AppiumBy.XPATH, self.close_add_xp)
                if close_element.is_displayed():
                    close_element.click()
                else:
                        try:
                            cross=self.driver.find_element(AppiumBy.XPATH,self.cross_x_xp)
                            if cross.is_displayed():
                                cross.click()
                        except:
                            print("Another type of Add appear")

            time.sleep(3)
            self.check_resultpage(mail)









                    













