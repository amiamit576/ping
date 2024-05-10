from Pageobject.ping import Ping_Action
from Pageobject.longcall import Long_call


class Test_Ping:




    def test_ping(self,setup,setup2):

        self.driver=setup
        self.driver2=setup2
        self.obj=Ping_Action(self.driver)
        self.obj.ping_start()
        # self.call=Long_call(self.driver,self.driver2)
        # self.call.open_phone_Dialler()
        # self.call.click_dialpad()
        # self.call.Enter_number("+919466960314")
        # self.call.make_call()










