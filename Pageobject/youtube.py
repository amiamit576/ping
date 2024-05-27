import time

from  appium import  webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as Ec


class Youtube():
    # Xpath
    Search_box_Xp = '//android.widget.AutoCompleteTextView[@resource-id="com.android.launcher:id/search_src_text"]'
    google_options_xp='//android.widget.FrameLayout[@content-desc="Folder: Google"]'
    youtube_options_xp='//android.widget.TextView[@content-desc="YouTube"]'
    home_btn_xp='//android.widget.TextView[@resource-id="com.google.android.youtube:id/text" and @text="Home"]'
    youtube_search_xp='//android.widget.ImageView[@content-desc="Search"]'
    yotube_search_edit_text_xp='//android.widget.EditText[@resource-id="com.google.android.youtube:id/search_edit_text"]'
    select_options_xp='//android.widget.TextView[@resource-id="com.google.android.youtube:id/text"]'
    select_vedio_xp='//android.view.ViewGroup[@content-desc="Musafir - 1957 - मुसाफिर l Bollywood Vintage Hit Movie l Suchitra Sen , Shekhar , Nirupa Roy – 2 hours, 15 minutes – Go to channel – LegendaryKishoreKumar - 8K views - 20 hours ago – play video"]/android.view.ViewGroup[1]/android.widget.ImageView'
    selected_vedio_options_Uiselector='new UiSelector().className("android.view.ViewGroup").instance(3)'
    control_button_grp_xp='//android.widget.RelativeLayout[@resource-id="com.google.android.youtube:id/controls_button_group_layout"]'
    skip_add_xp='//android.widget.ImageView[@resource-id="com.google.android.youtube:id/skip_ad_button_icon"]'
    another_vedio_instance_ui='new UiSelector().className("android.view.ViewGroup").instance(20)'



    #

    close_Add_cross_xpath='//android.widget.ImageView[@content-desc="Close ad panel"]'
    enter_full_screen_xpath='//android.widget.ImageView[@content-desc="Enter full screen"]'
    exit_full_screen_xpath='//android.widget.ImageView[@content-desc="Exit full screen"]'
    more_vedioes_xp='//android.widget.ImageView[@content-desc="Next video"]'




    # in case  differnet page opened


    def __init__(self,driver):
        self.driver=driver


    def open_youtube(self):
        try:
            self.driver.find_element(AppiumBy.XPATH,self.google_options_xp).click()
            time.sleep(2)
            self.driver.find_element(AppiumBy.XPATH,self.youtube_options_xp).click()
        except:
            self.driver.swipe(523, 2308, 523, 686)
            time.sleep(1)
            self.driver.find_element(AppiumBy.XPATH, self.Search_box_Xp).send_keys('YouTube')
            self.driver.find_element(AppiumBy.XPATH, self.youtube_options_xp).click()
        time.sleep(2)

    def select_vedio(self):
        self.driver.find_element(AppiumBy.XPATH,self.home_btn_xp).click()
        time.sleep(1)
        self.driver.find_element(AppiumBy.XPATH,self.youtube_search_xp).click()
        self.driver.find_element(AppiumBy.XPATH,self.yotube_search_edit_text_xp).send_keys("kishore kumar")
        try:
            self.driver.find_element(AppiumBy.XPATH,self.select_options_xp).click()
        except NoSuchElementException:
            print("select tab diappear ")
        time.sleep(1)
        #self.driver.find_element(AppiumBy.XPATH,self.select_vedio_xp).click()
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,self.selected_vedio_options_Uiselector).click()
        try:
            time.sleep(5)
            self.driver.find_element(AppiumBy.XPATH,self.skip_add_xp).click()
        except NoSuchElementException:
            time.sleep(3)
            print("no skip add button appear")
        try:
            control_btn=self.driver.find_element(AppiumBy.XPATH,self.control_button_grp_xp)
            if control_btn.is_displayed() :
                print("vedio is started")
        except NoSuchElementException:
            self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,self.another_vedio_instance_ui).click()
            








    def full_screen(self):

        self.driver.execute_script('mobile: doubleClickGesture', {'x': 629, 'y': 496})
        self.driver.find_element(AppiumBy.XPATH,self.enter_full_screen_xpath).click()
        time.sleep(1)
        self.driver.tap([(1000,200)])
        self.driver.execute_script('mobile: clickGesture', {'x': 1386, 'y': 639})
        self.driver.back()





    def pause_play(self):
        count=0
        for i in range (10):
            time.sleep(45)
            try:
                time.sleep(5)
                self.driver.find_element(AppiumBy.XPATH, self.skip_add_xp).click()
            except NoSuchElementException:
                time.sleep(3)
                print("no skip add button appear")

            self.driver.execute_script('mobile: doubleClickGesture', {'x': 629, 'y': 496})
            try:
                self.driver.find_element(AppiumBy.XPATH,self.more_vedioes_xp).click()
            except (NoSuchElementException,StaleElementReferenceException) as e:
                if isinstance(e,StaleElementReferenceException) :
                    self.driver.execute_script('mobile: doubleClickGesture', {'x': 1013, 'y': 589})
                    self.driver.execute_script('mobile: doubleClickGesture', {'x': 1013, 'y': 589})
                if isinstance(e,NoSuchElementException) :
                    self.driver.execute_script('mobile: doubleClickGesture', {'x': 1013, 'y': 589})
            count+=1
            print("total count",count)
        self.driver.back()
        self.driver.back()
        self.driver.back()























