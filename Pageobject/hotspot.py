import time

from  appium import  webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from  UTILITY.customlogger import  LogGen



class Hotspot:
    # get  the text bhot spot btn  to confirm is it on or off

    # xpath
        Search_box_Xp = '//android.widget.AutoCompleteTextView[@resource-id="com.android.launcher:id/search_src_text"]'
        setting_icon_xp='//android.widget.TextView[@content-desc="Settings"]'
        connection_and_sharing_xp='//android.widget.TextView[@resource-id="android:id/title" and @text="Connection & sharing"]'
        personal_hotspot_xp='//android.widget.TextView[@resource-id="android:id/title" and @text="Personal hotspot"]'
        personal_hotspot_option_xp='//android.widget.TextView[@resource-id="android:id/title" and @text="Personal hotspot"]'
        hotspot_on_off_btn_xp='(//android.widget.Switch[@resource-id="com.oplus.wirelesssettings:id/switchWidget"])[1]'
        hotspot_setting_xp='//android.widget.TextView[@resource-id="android:id/title" and @text="Hotspot settings"]'
        hotspot_name_xp='(//android.widget.LinearLayout[@resource-id="com.oplus.wirelesssettings:id/edittext_container"])[2]/android.widget.EditText'
        hotspot_password_xp='(//android.widget.LinearLayout[@resource-id="com.oplus.wirelesssettings:id/edittext_container"])[4]/android.widget.EditText'
        hotspot_save_menu_xp='//android.widget.TextView[@resource-id="com.oplus.wirelesssettings:id/menu_save"]'
        Ap_band_current_xp='//android.widget.TextView[@resource-id="com.oplus.wirelesssettings:id/assignment" and @text="2.4 GHz"]'
        Ap_band_current1_xp='//android.widget.TextView[@resource-id="com.oplus.wirelesssettings:id/assignment" and @text="5 GHz"]'
        Ap_band_xp='//android.widget.TextView[@resource-id="android:id/title" and @text="AP band"]'
        ap_band_2ghz='//android.widget.TextView[@resource-id="com.oplus.wirelesssettings:id/popup_list_window_item_title" and @text="2.4 GHz"]'
        ap_band_5ghz='//android.widget.TextView[@resource-id="com.oplus.wirelesssettings:id/popup_list_window_item_title" and @text="5 GHz"]'
        #
        use_wifi6='(//android.widget.Switch[@resource-id="android:id/switch_widget"])[2]'

        #===============================================Device2 Xpath==============================================================
        wifi_options='//android.widget.TextView[@resource-id="android:id/title" and @text="Wi-Fi"]'
        enable_wifi_options_xp='//android.widget.Switch[@resource-id="android:id/switch_widget"]'
        addnetwork_xp='//android.widget.TextView[@resource-id="android:id/title" and @text="Add network"]'
        add_hotspotname_xp='(//android.widget.LinearLayout[@resource-id="com.oplus.wirelesssettings:id/edittext_container"])[2]/android.widget.EditText'
        add_password_xp='(//android.widget.LinearLayout[@resource-id="com.oplus.wirelesssettings:id/edittext_container"])[4]/android.widget.EditText'
        save_button='//android.widget.TextView[@resource-id="com.oplus.wirelesssettings:id/menu_save"]'
        save_psw_dilogbx_xp='//android.widget.TextView[@resource-id="android:id/autofill_save_yes"]'


        # if google password confirmation box appear
        cancel_xp='//android.widget.Button[@resource-id="android:id/button1"]'
        auto_fill_popup_cancel_btn_xp='//android.widget.Button[@resource-id="android:id/autofill_dialog_no"]'
        # if  connection fail
        connection_fail_status_xp='//android.widget.TextView[@resource-id="com.oplus.wirelesssettings:id/alertTitle"]'
        connection_fail_btn_xp='//android.widget.Button[@resource-id="android:id/button1"]'
        save_password_popup_xp='//android.widget.TextView[@resource-id="android:id/autofill_save_no"]'

        # connection status
        selected_network_xp='(//android.widget.ImageView[@resource-id="com.oplus.wirelesssettings:id/signal"])[1]'
        # confirm by getting text
        statussummary_xp='//android.widget.TextView[@resource-id="com.oplus.wirelesssettings:id/wifi_status_summary"]'


        logger=LogGen.loggen()


        def __init__(self,driver):
            self.driver=driver





        def open_setting(self):
            try:
                self.driver.find_element(AppiumBy.XPATH,self.setting_icon_xp).click()

            except:
                self.driver.swipe(523, 2308, 523, 686)
                time.sleep(1)
                self.driver.find_element(AppiumBy.XPATH, self.Search_box_Xp).send_keys('Settings')
                self.driver.find_element(AppiumBy.XPATH, self.setting_icon_xp).click()

        def open_hotspot(self):

            self.driver.find_element(AppiumBy.XPATH,self.connection_and_sharing_xp).click()
            time.sleep(1)
            self.driver.find_element(AppiumBy.XPATH,self.personal_hotspot_xp).click()
            self.logger.info("Opend Hotspot")



        def enable_hotspot(self):

              scroll_btn=self.driver.find_element(AppiumBy.XPATH,self.hotspot_on_off_btn_xp)
              self.logger.info("check on or off")
              scroll_status=scroll_btn.get_attribute('checked')
              if scroll_status=='false':
                scroll_btn.click()
              else:
                  print("Hotspot Already on")
              time.sleep(3)


        def change_setting(self,psw):
            global hotspot_name
            global hotspot_psw
            self.driver.find_element(AppiumBy.XPATH,self.hotspot_setting_xp).click()
            hotspot_name= self.driver.find_element(AppiumBy.XPATH,self.hotspot_name_xp).text
            print(hotspot_name)
            self.driver.find_element(AppiumBy.XPATH, self.hotspot_password_xp).clear()
            self.driver.find_element(AppiumBy.XPATH,self.hotspot_password_xp).send_keys(psw)
            time.sleep(3)
            try:
                self.driver.find_element(AppiumBy.XPATH,self.Ap_band_current_xp).click()
                time.sleep(1)
                self.driver.find_element(AppiumBy.XPATH,self.ap_band_5ghz).click()
                print("Changed Ap band  to 5ghz")
            except NoSuchElementException:
                try:
                    self.driver.find_element(AppiumBy.XPATH,self.Ap_band_current1_xp).click()
                    time.sleep(1)
                    self.driver.find_element(AppiumBy.XPATH,self.ap_band_2ghz).click()
                    print("Changed Ap band to  2.4ghz")
                except NoSuchElementException:
                    print ("band is not selected")

            save_btn=self.driver.find_element(AppiumBy.XPATH,self.hotspot_save_menu_xp)
            save_status=save_btn.get_attribute('enabled')
            if save_status=='true':
                save_btn.click()
            else:
                print("password already saved")
            hotspot_psw=psw
            print(hotspot_psw)
            self.driver.back()
            self.driver.execute_script('mobile: pressKey', {"keycode": 3})
            self.driver.back()
            self.logger.info("changed the setting  of hotspot")


        def connect_other(self):
            global hotspot_name
            global hotspot_psw
            self.logger.info(" changed the device ")
            self.driver.find_element(AppiumBy.XPATH,self.wifi_options).click()
            time.sleep(1)
            try:
                wifienable=self.driver.find_element(AppiumBy.XPATH,self.enable_wifi_options_xp)

                enable_status=wifienable.get_attribute('checked')
                if enable_status =='false':
                    wifienable.click()
                else :
                    print("wifi is enabled")

            except:
                    print("wifi selection  otion is not available")
            self.driver.swipe(523, 2308, 523, 50)
            #self.driver.swipe(523, 2308, 523, 300)
            self.driver.find_element(AppiumBy.XPATH,self.addnetwork_xp).click()
            time.sleep(1)
            self.driver.find_element(AppiumBy.XPATH,self.add_hotspotname_xp).send_keys(hotspot_name)
            time.sleep(1)
            self.driver.find_element(AppiumBy.XPATH,self.add_password_xp).send_keys(hotspot_psw)

            try:
                save_option=self.driver.find_element(AppiumBy.XPATH,self.save_button)
                if save_option.is_enabled() :
                    save_option.click()
                else :
                    password_length=len(hotspot_psw)
                    if password_length>=8:
                        print("Password  is  already  set")
                    else:
                        print("password is short")
            except:
                print("save option is not enabled")
            # In case worg password
            try:
                pw_error_msg=self.driver.find_element(AppiumBy.XPATH,self.connection_fail_status_xp)
                error_sts=pw_error_msg.get_attribute("displayed")
                if error_sts=='true':
                    self.driver.find_element(AppiumBy.XPATH,self.connection_fail_btn_xp).click()
                    print("Correct your password")
            except:
                print("you are already connected")
            self.logger.info("wifi connection established")


        def verify_connection(self):
            global hotspot_name
            try:
                self.driver.find_element(AppiumBy.XPATH,self.save_password_popup_xp).click()
            except NoSuchElementException:
                    print("popup Doesnot  Appear")

            time.sleep(5)
            self.driver.find_element(AppiumBy.XPATH,self.selected_network_xp).click()
            time.sleep(2)
            sts_summary=self.driver.find_element(AppiumBy.XPATH,self.statussummary_xp).text
            if sts_summary == "Connected":
                print("Connected")

            else:
                print("not connected")

            self.driver.back()
            self.driver.execute_script('mobile: pressKey', {"keycode": 3})
            self.driver.back()



                






















































