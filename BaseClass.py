#coding=utf-8

__author__='ben.chaung'
from pybi import Pybi

'''
基础类,用于所有页面的继承
'''

class base_page(Pybi):

    def __init__(self, driver):
        self.driver = Pybi('chrome')


class Login(base_page):

    '''
    用于最终测试用例编写时的调用,demo主要是编写登录类
    '''

    def set_username(self, username):
        self.driver.set_value('id=>username', username)

    def set_password(self, password):
        self.driver.set_value('id=>password', password)

    def login(self):
        self.driver.click("xpath=>//li/input[@type='button']")

    def get_login_info(self):
        self.driver.get_text("xpath=>//ul/li[@class='error']")


class create_ex(base_page):
    '''
    创建考试的类
    '''

    def set_exname(self, exname):

        pass

