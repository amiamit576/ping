# to iniate longcall
import time
from datetime import datetime

from appium import  webdriver
from appium.webdriver.common.appiumby import  AppiumBy
from selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from UTILITY.customlogger import LogGen


class Long_call:

    logger=LogGen.loggen()

    # xpath
    phn_dialer_xpath = '//android.widget.TextView[@content-desc="Phone"]'
    phn_dialer_andriodUi='new UiSelector().text("Phone")'

    recent_btn_xpath = '//android.view.View[@resource-id="com.google.android.dialer:id/navigation_bar_item_active_indicator_view"]'
    keypad_xpath = '//android.widget.ImageButton[@content-desc="key pad"]'
    textarea_num_xpath = '//android.widget.EditText[@resource-id="com.google.android.dialer:id/digits"]'
    Call_btn_xpath = '//android.widget.Button[@content-desc="dial"]'
    Num_call_btn_xp = '//android.widget.ImageView[@resource-id="com.google.android.dialer:id/call_button"]'
    Audio_End_button = '//android.widget.Button[@content-desc="End call"]'
    call_timer_xpath = '//android.widget.Chronometer[@resource-id="com.google.android.dialer:id/contactgrid_bottom_timer"]'

    def __init__(self,driver,driver2):
        self.driver=driver
        self.driver2=driver2


    def Recieve_call(self):
        self.driver2.tap([(893, 494)])
        self.logger.info("call is reccived")
        time.sleep(1)
        self.driver2.back()

    def open_phone_Dialler(self):
        try:
            self.driver.find_element(AppiumBy.XPATH,self.phn_dialer_xpath).click()
            time.sleep(1)
        except:
            self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,self.phn_dialer_andriodUi).click()
            time.sleep(1)
        self.logger.info("Dial pad is opened")
    def click_dialpad(self):
        self.driver.find_element(AppiumBy.XPATH,self.recent_btn_xpath).click()
        time.sleep(1)
        self.driver.find_element(AppiumBy.XPATH, self.keypad_xpath).click()
        self.logger.info("Dialpad is opened")

    def Enter_number(self, number):
        self.driver.find_element(AppiumBy.XPATH, self.textarea_num_xpath).send_keys(number)
        self.logger.info("Number is entered")

    def make_call(self):
        repeat = 5
        wait_for_call = WebDriverWait(self.driver, 26)
        total = 0
        cnt = 0
        Drop = 0
        switch = 0
        for i in range(repeat):
            total += 1
            timestamp = datetime.now().strftime("%Y-%m-%d___%H:%M:%S")
            try:
                self.driver.find_element(AppiumBy.XPATH, self.Call_btn_xpath).click()
            except Exception:
                try:
                    self.driver.find_element(AppiumBy.XPATH, self.Num_call_btn_xp).click()
                except Exception:
                    print("Both video  and call buttons are not present")
                    self.driver.save_screenshot(".\\Scrrenshots\\" + "call_dialerabsent.png")

            time.sleep(5)
            self.Recieve_call()
            try:
                wait_for_call.until(EC.visibility_of_element_located((AppiumBy.XPATH, self.call_timer_xpath)))
                self.logger.info("timer is visible")
                try:
                    wait_for_call.until(EC.presence_of_element_located((AppiumBy.XPATH, self.recent_btn_xpath)))
                    if self.driver.find_element(AppiumBy.XPATH, self.recent_btn_xpath).is_displayed():
                        Drop += 1
                        print('Call Drop--->', timestamp)
                        continue
                except:
                    cnt += 1
                    #self.driver.find_element(AppiumBy.XPATH, self.Audio_End_button).click()
                    print("Call was Successfull--->", cnt)
                    break

            except Exception:
                self.logger.error("Reciever end is not picking or switch Off or out of range")

                if total == repeat:
                    try:
                        self.driver.find_element(AppiumBy.XPATH, self.Audio_End_button).click()
                    except:
                        pass
                else:
                    continue
        print("Total Call Made--->", total)
        print("Total Call Drop--->", Drop)
        print("Total Test Call Pass-->", cnt)
        self.driver.back()
        self.driver.back()
        self.driver.back()













