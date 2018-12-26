# -*- coding: utf-8 -*-
import unittest
from imp import reload

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pytesseract
from pytesseract import image_to_string
import unittest, time, re, sys
from PIL import Image



class Ypt(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://218.3.78.235:8888/website/Login.aspx"
        self.verificationErrors = []
        self.accept_next_alert = True

    def get_streen(self):
        while True:
            driver = self.driver
            driver.save_screenshot('C://Image//aa.png')  # 截取当前网页，该网页有我们需要的验证码
            imgelement = driver.find_element_by_xpath("//*[@id='vcode']/img")  # 定位验证码
            location = imgelement.location  # 获取验证码x,y轴坐标
            size = imgelement.size  # 获取验证码的长宽
            rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']),
                  int(location['y'] + size['height']))  # 写成我们需要截取的位置坐标
            i = Image.open("C://Image//aa.png")  # 打开截图
            frame4 = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
            frame4.save('C://Image//frame4.png')
            img = Image.open('C://Image//frame4.png')
            img.load()
            aa =image_to_string(img)
            print (u"识别的验证码为：")
            print (aa)

            if aa != "":  # 如果识别为空，则再一次识别
                break
        return aa


    def test_ypt(self):
        now_time = open("yuheng.txt", "a")
        driver = self.driver
        driver.maximize_window()
        driver.get("http://218.3.78.235:8888/website/Login.aspx")
        driver.find_element_by_id("txtUserName").clear()
        driver.find_element_by_id("txtUserName").send_keys("米思米")
        driver.find_element_by_id("txtPassWord").clear()
        driver.find_element_by_id("txtPassWord").send_keys("111111")
        driver.find_element_by_id("txtValidateCode").clear()
        driver.find_element_by_id("txtValidateCode").send_keys(self.get_streen())
        time.sleep(5)
        driver.find_element_by_id("btnLogin").click()

        time.sleep(10)

    def is_element_present(self, how, what):
        try:
                self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True
if __name__ == "__main__":

    unittest.main()