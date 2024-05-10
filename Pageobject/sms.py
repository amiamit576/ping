from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
from  selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.support.wait import  WebDriverWait




class Long_msg:

    message=("A well-organized paragraph supports or develops a single controlling idea,")

    msg_xpath='//android.widget.TextView[@text="Messages"]'
    start_chat_Xpath='//android.widget.Button[@content-desc="Start chat"]'
    Search_contact_xpath='//android.widget.EditText[@resource-id="ContactSearchField"]'
    confirm_contact_xpath='//android.view.View[@resource-id="GlideMonogram"]'
    text_area_xpath='//android.widget.EditText[@resource-id="com.google.android.apps.messaging:id/compose_message_text"]'
    send_message_mms_xpath='//android.widget.ImageView[@content-desc="Send MMS"]'
    send_message_sms_xpath='//android.widget.ImageView[@content-desc="Send SMS"]'
    send_button_xpath='//android.widget.ImageView[@resource-id="com.google.android.apps.messaging:id/send_message_button_icon"]'
    double_click_xpath='//android.widget.ImageView[@resource-id="com.google.android.apps.messaging:id/status_icon"]'
    navigate_back_xpath='//android.widget.ImageButton[@content-desc="Navigate up"]'




    def __init__(self,driver):
        self.driver=driver

    def homepage(self):
        for i in range(2):
            self.driver.execute_script('mobile: pressKey', {"keycode": 3})


    def open_Msg(self):
        self.driver.find_element(AppiumBy.XPATH,self.msg_xpath).click()
        sleep(1)

    def compose_msg(self):
        self.driver.find_element(AppiumBy.XPATH,self.start_chat_Xpath).click()
        sleep(1)

    def enter_number(self,number):
        self.driver.find_element(AppiumBy.XPATH,self.Search_contact_xpath).send_keys(number)
        sleep(2)
        self.driver.find_element(AppiumBy.XPATH,self.confirm_contact_xpath).click()
        sleep(1)

    def type_Msg(self):
        self.driver.find_element(AppiumBy.XPATH, self.text_area_xpath).clear()
        sleep(1)
        self.driver.find_element(AppiumBy.XPATH,self.text_area_xpath).send_keys((self.message))
        sleep(2)

    def send_Msg_Verify(self):
        try:
            self.driver.find_element(AppiumBy.XPATH,self.send_message_sms_xpath).click()
        except:
            self.driver.find_element(AppiumBy.XPATH,self.send_button_xpath)
        sleep(5)
        confirm_delivery=WebDriverWait(self.driver,10)
        try:
            confirm_delivery.until(EC.visibility_of_element_located((AppiumBy.XPATH,self.double_click_xpath)))
            print("Message delivered")
        except:
            print("Message is not  Delivered")




        self.driver.find_element(AppiumBy.XPATH,self.navigate_back_xpath).click()
        self.driver.back()
        self.driver.back()





