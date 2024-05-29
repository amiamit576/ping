import time

from Pageobject.ping import Ping_Action
from Pageobject.longcall import Long_call
from Pageobject.sms import Long_msg


class Test_Ping:




    def test_ping(self,setup,setup2):

        self.driver=setup
        self.driver2=setup2
        self.obj=Ping_Action(self.driver)
        self.obj.ping_start()
        # self.call=Long_call(self.driver,self.driver2)
        # self.call.open_phone_Dialler()
        # self.call.click_dialpad()
        # self.call.Enter_number('+918976965522')
        # self.call.make_call()
        # self.sms_dv1=Long_msg(self.driver)
        # self.sms_dv2=Long_msg(self.driver2)
        # for i in range(1):
        #     self.sms_dv1.open_Msg()
        #     self.sms_dv1.compose_msg()
        #     self.sms_dv1.enter_number('+918976965522')
        #     self.sms_dv1.type_Msg()
        #     self.sms_dv1.send_Msg_Verify()
        #     time.sleep(5)
        #     self.sms_dv2.homepage()
        #     self.sms_dv2.open_Msg()
        #     self.sms_dv2.compose_msg()
        #     self.sms_dv2.enter_number('+919653172104')
        #     self.sms_dv2.type_Msg()
        #     self.sms_dv2.send_Msg_Verify()
        self.obj.ping_stop("amiamit576@gmail.com")













