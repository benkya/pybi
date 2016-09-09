# coding=utf-8

import unittest
from pybi import *
import BaseClass
import time

class demo_test(unittest.TestCase):

    def setUp(self):

        self.driver = Pybi('chrome')#实例化pybi类

        self.url='http://192.168.2.47:8080/SXWFrame/main/loginPage.do'#定义URL

    def tearDown(self):

        self.driver.quit()#使用quit方法退出浏览器


    def test_login(self):

        '''
        不使用page模式的话,用以下代码

        mydriver = self.driver
        mydriver.open_url(self.url)

        mydriver.set_value('id=>username','admin') #使用set_value方法设置username文本框的值,其中set_value方法默认调用了find_element方法。
        mydriver.set_value('id=>password','123456') #使用set_value方法设置password 用id的方式

        mydriver.click("xpath=>//li/input[@type='button']") #使用click方法点击登录按钮。用xpath的方式

        '''

        '''
        以下方式为使用page模式,page模式的好处就是,在真正的测试用例中,不需要很多页面定位的语句等,这些定位语句都在page中,如果以后页面元素进行了调整,则只需要维护page,而不用维护测试用例
        '''
        self.driver.open_url(self.url)
        time.sleep(2)
        login_page = BaseClass.Login(self.driver)
        login_page.set_username('admin')
        login_page.set_password('123456')
        login_page.login()

        time.sleep(2)

        now_url = self.driver.get_url()

        self.assertEqual('http://192.168.2.47:8080/SXWFrame/main/loginSuccessPage.do', now_url)



if __name__ == '__main__':

    unittest.main()




