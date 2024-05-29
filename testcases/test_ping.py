import time

import testcases.test_download
from Pageobject.download import Large_download
from Pageobject.hotspot import Hotspot
from Pageobject.ping import Ping_Action
from Pageobject.longcall import Long_call
from Pageobject.sms import Long_msg
from Pageobject.youtube import Youtube
from UTILITY.customlogger import LogGen


class Test_Ping:




    logger=LogGen.loggen()

    def test_ping(self,setup,setup2):
        url = "https://ash-speed.hetzner.com/"
        self.logger.info("Start the test")
        self.driver=setup
        self.driver2=setup2
        self.logger.info("Setup is done")
        self.logger.info("Staring  the ping Action")
        self.obj=Ping_Action(self.driver)
        self.obj.ping_start()
        self.logger.info("Logger is started")
        self.obj = Ping_Action(self.driver)
        self.obj.ping_start()
        self.call = Long_call(self.driver, self.driver2)
        self.call.open_phone_Dialler()
        self.call.click_dialpad()
        self.call.Enter_number('+918976965522')
        self.call.make_call()
        self.sms_dv1 = Long_msg(self.driver)
        self.sms_dv2 = Long_msg(self.driver2)
        for i in range(2):
            self.sms_dv1.open_Msg()
            self.sms_dv1.compose_msg()
            self.sms_dv1.enter_number('+918976965522')
            self.sms_dv1.type_Msg()
            self.sms_dv1.send_Msg_Verify()
            time.sleep(5)
            self.sms_dv2.homepage()
            self.sms_dv2.open_Msg()
            self.sms_dv2.compose_msg()
            self.sms_dv2.enter_number('+919653172104')
            self.sms_dv2.type_Msg()
            self.sms_dv2.send_Msg_Verify()
        time.sleep(3)
        self.logger.info("large file downloading  started ")
        self.dow = Large_download(self.driver)
        self.dow.big_file_download(url)
        self.logger.info("Downloading  large file")
        self.dow.check_file_download()
        self.logger.info("large file download  complete")
        #Hotspot
        self.hotspt = Hotspot(self.driver)
        self.hotspt.open_setting()
        time.sleep(1)
        self.hotspt.open_hotspot()
        time.sleep(1)
        self.hotspt.enable_hotspot()
        time.sleep(1)
        self.hotspt.change_setting('1234560986')
        time.sleep(5)
        self.connect = Hotspot(self.driver2)
        time.sleep(1)
        self.connect.open_setting()
        time.sleep(1)
        self.connect.connect_other()
        time.sleep(4)
        self.connect.verify_connection()
        # youtube
        self.yt = Youtube(self.driver)
        self.yt.open_youtube()
        self.yt.select_vedio()
        self.yt.pause_play()

        self.obj.ping_stop("amiamit576@gmail.com")












