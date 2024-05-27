import time

from  Pageobject.hotspot import  Hotspot



class Test_Hotspot:










     def test_hotspot_setting(self,setup,setup2):
        self.driver=setup
        self.driver2=setup2
        self.hotspt=Hotspot(self.driver)
        self.hotspt.open_setting()
        time.sleep(1)
        self.hotspt.open_hotspot()
        time.sleep(1)
        self.hotspt.enable_hotspot()
        time.sleep(1)
        self.hotspt.change_setting('1234560986')
        time.sleep(5)
        self.connect=Hotspot(self.driver2)
        time.sleep(1)
        self.connect.open_setting()
        time.sleep(1)
        self.connect.connect_other()
        time.sleep(4)
        self.connect.verify_connection()




