import time

from  Pageobject.hotspot import  Hotspot
from Pageobject.clear import Clear_all


class Test_Hotspot:










     def test_hotspot_setting(self,setup,setup2):
        self.driver=setup
        self.driver2=setup2
        # self.hotspt=Hotspot(self.driver)
        # self.hotspt.open_setting()
        # time.sleep(1)
        # self.hotspt.open_hotspot()
        # time.sleep(1)
        # self.hotspt.enable_hotspot()
        # time.sleep(1)
        # self.hotspt.change_setting('123456789')
        self.connect=Hotspot(self.driver2)
        self.connect.open_setting()
        self.connect.connect_other()




