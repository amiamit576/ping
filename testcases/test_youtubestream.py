from Pageobject.youtube import  Youtube






class Test_Youtube:

    def test_youtube(self,setup):
        self.driver=setup
        self.yt=Youtube(self.driver)
        self.yt.open_youtube()
        self.yt.select_vedio()
        self.yt.pause_play()

