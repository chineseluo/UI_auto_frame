#coding:utf-8
from Base.base import Base
from selenium.webdriver.common.by import By
from selenium import webdriver

#封装携程首页操作对象及各个元素及操作方法
class Home_page(Base):

    def get_home_page_url(self, url):
        self.getUrl(url)

    def search_info(self, value):
        self.sendKey((By.ID, "_allSearchKeyword"), value)
        self.click_btn((By.ID, "search_button_global"))

    def click_insurance(self):
        self.click_btn((By.XPATH, "/html/body/div[10]/ul/li[9]/a"))

    def get_insurance_text(self):
        return self.get_text((By.XPATH, "//*[@id='root']/div/div/div/div[1]/div[2]/div[1]/div[2]/div[1]/label"))

    def get_city_text(self):
        return self.get_text((By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/h1/a"))

    def switch_driver_to_otherHandle(self):
        self.switchToHandle()

if __name__ == "__main__":
    home_page = Home_page(webdriver.Chrome("D:/chromedriver/chromedriver_win32_75/chromedriver.exe"))
    home_page.get_home_page_url("https://www.ctrip.com")
    home_page.search_info("成都")
