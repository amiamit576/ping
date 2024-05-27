from UTILITY.customlogger import  LogGen


class Clear_all:

    #locator
    close_all_btn_Xp='//android.widget.Button[@content-desc="Close all"]'
    element_on_home_xp='//android.widget.TextView[@text="Play Store"]'
    phone_xp='//android.widget.TextView[@content-desc="Phone"]'
    logger=LogGen.loggen()






    def __init__(self,driver):
        self.driver=driver


    def clearAll(self):

        self.logger.error("hello world")

        # self.driver.execute_script('mobile: pressKey', {"keycode": 187})
        # self.driver.find_element(AppiumBy.XPATH,self.close_all_btn_Xp).click()
        # wait_for_enable=WebDriverWait(self.driver,30)
        # wait_for_enable.until(Ec.visibility_of_element_located((AppiumBy.XPATH,self.element_on_home_xp)))
        # self.driver.find_element(AppiumBy.XPATH,self.phone_xp).click()







