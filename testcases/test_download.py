import time

from  Pageobject.download import  Large_download


class Test_Download:


    def test_download(self,setup):
        url = "https://ash-speed.hetzner.com/"
        self.driver=setup
        self.dow=Large_download(self.driver)
        self.dow.big_file_download(url)

        self.dow.check_file_download()
