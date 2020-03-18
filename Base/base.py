#coding:utf-8
import selenium
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
import os
import configparser
import time
from Common.log_option import Log_option


#Base层封装的是元素的操作方法，会调用Common中封装好的基础方法
class Base():
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.timeout = 10
        self.poll_frequency = 0.5
        self.log_option = Log_option()

    def getUrl(self,url):
        self.driver.get(url)

    def findElement(self, locator):
        """
        :param locator: 传入定位器参数locator=(By.XX,"value")
        :return: 返回元素对象
        """
        #方法二次封装Demo
        #WebDriverWait(self, driver, timeout, poll_frequency=POLL_FREQUENCY, ignored_exceptions=None)
        #elem = WebDriverWait(driver, timeout, t).until(lambda x: x.findElenmentById("name"))元素显示等待
        #locator定位器，locator(by,value)即是传入元素定位器和元素值)
        if not isinstance(locator, tuple):
            self.log_option.log('locator参数类型错误，必须传元祖类型：locator=(By.XX,"value")')
        else:
            print(type("正在定位元素信息：定位方式->%s,value值->%s"%(locator[0],locator[1])))
            self.log_option.log("正在定位元素信息：定位方式->%s,value值->%s"%(locator[0],locator[1]))
            try:
                time.sleep(2)
                elem = WebDriverWait(self.driver, self.timeout, self.poll_frequency).until(lambda x: x.find_element(*locator))
                return elem
            except:
                return print("定位不到元素")

    def findElements(self, locator):
        """
        :param locator: 传入定位器参数locator=(By.XX,"value")
        :return: 返回元素对象列表
        """
        elem = WebDriverWait(self.driver, self.timeout, self.poll_frequency).until(lambda x: x.find_elements(*locator))
        return elem



    def switchToFrame(self, locator):
        """
        :param locator: 传入定位器参数locator=(By.XX,"value")
        :return:
        """
        elem = self.findElement(locator)
        self.driver.switch_to.frame(elem)

    def switchToHandle(self):
        #获取当前所有窗口句柄
        handles = self.driver.window_handles
        #切换到新窗口句柄
        self.driver.switch_to.window(handles[1])

    def sendKey(self, locator, value):
        elem = self.findElement(locator)
        elem.send_keys(value)

    def click_btn(self, locator):
        time.sleep(2)
        elem = self.findElement(locator)
        elem.click()

    def get_text(self,locator):
        """

        @param locator:定位器
        @return:元素文本值
        """
        elem = self.findElement(locator)
        elem_text = elem.text
        print("文本值输出")
        print(elem_text)
        return elem_text

if __name__ == "__main__":
    base = Base(webdriver.Chrome("D:/chromedriver/chromedriver_win32_75/chromedriver.exe"))
    base.getUrl("https://www.ctrip.com")

