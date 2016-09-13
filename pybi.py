# coding=utf-8

__author__ ='ben.chaung'

'''
pybi在python加selenium基础上,对于一些常用方法的封装,只需要对该类的简单继承,即可使用
'''

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import sys
reload(sys)

sys.setdefaultencoding('utf-8')

class Pybi(object):

    def __init__(self, browser_name='ff'):

        '''
        初始化pybi类,主要是初始化浏览器,默认为ff,可以传入其他的浏览器名称,比如chrome,ie等,注意传入参数为小写
        '''

        if browser_name == 'firefox' or browser_name == 'ff':
            driver = webdriver.Firefox()
        elif browser_name == 'chrome':
            driver  = webdriver.Chrome()
        elif browser_name == "internet explorer" or browser_name == "ie":
            driver = webdriver.Ie()

        '''
        异常处理,如果浏览器打开失败等,则抛出对应的异常
        '''

        try:
            self.driver = driver
        except Exception:

            raise NameError(u"传入的浏览器名称 %s 没有被发现,请确认输入的是'ie','chrome'或者'ff'!!" % browser_name)

    def wait_element(self, location ,stime =5 ):
        '''
        用于定义页面元素的等待方法,如平时使用的time.sleep(5)的效果,一般情况下,使用id,name,和xpath就足够了
        使用方法:driver.wait_element("location=>#classname", 10)
        :param location: 表示location样式
        :param stime: 表示等待的时间
        '''
        if "=>" not in location:
            raise NameError(u"定位语法不是这么写的朋友,看看是不是少了'=>'!!!")

        by = location.split("=>")[0]
        value = location.split("=>")[1]

        if by == 'id':
            WebDriverWait(self.driver, stime, 1).until(EC.presence_of_element_located((By.ID, value)))
        elif by == 'name':
            WebDriverWait(self.driver, stime, 1).until(EC.presence_of_element_located((By.NAME, value)))
        elif by == "class":
            WebDriverWait(self.driver, stime, 1).until(EC.presence_of_element_located((By.CLASS_NAME, value)))
        elif by == "link_text":
            WebDriverWait(self.driver, stime, 1).until(EC.presence_of_element_located((By.LINK_TEXT, value)))
        elif by == "xpath":
            WebDriverWait(self.driver, stime, 1).until(EC.presence_of_element_located((By.XPATH, value)))
        elif by == "location":
            WebDriverWait(self.driver, stime, 1).until(EC.presence_of_element_located((By.location_SELECTOR, value)))

        else:
            raise NameError(u"定位元素失败,请使用id,name,class,link_text,xpath,location 等方法!!")


    def find_element(self,location):
        '''
        用于封装selenium的查找元素的方法
        :param location:
        :return: 返回对应的元素对象供操作
        '''

        if "=>" not in location:
            raise NameError(u"定位语法不是这么写的朋友,看看是不是少了'=>'!!!")

        by = location.split('=>')[0]
        value = location.split('=>')[1]

        if by =='id':
            element = self.driver.find_element_by_id(value)
        elif by == 'name':
            element = self.driver.find_element_by_name(value)
        elif by == "class":
            element = self.driver.find_element_by_class_name(value)
        elif by == "link_text":
            element = self.driver.find_element_by_link_text(value)
        elif by == "xpath":
            element = self.driver.find_element_by_xpath(value)
        elif by == "location":
            element = self.driver.find_element_by_location_selector(value)

        else:
            raise NameError(u"听话,定位元素失败,请使用id,name,class,link_text,xpath,location 等方法!!")

        return element

    def open_url(self, url):
        '''
        封装打开对应浏览器的方法
        调用方法:  open_url('www.sxw.cn')
        :param url:
        :return:
        '''

        self.driver.get(url)


    def set_value(self, location, value):
        '''
        用于对input等输入参数
        调用方法: driver.set_value('location=>#classname','hello')
        :param location: 定位语法
        :param value: 需要设置的内容
        :return:
        '''

        #防止页面元素还没有出现,所以先确认元素已经存在
        self.wait_element(location)
        pybi_element = self.find_element(location)
        pybi_element.send_keys(value)

    def reset_value(self, location):
        '''
        清除文本框等已经存在的内容
        调用方法:
        :param location:
        :return:
        '''
        self.wait_element(location)
        pybi_element = self.find_element(location)
        pybi_element.clear()

    def click(self, location):

        self.wait_element(location)
        pybi_element = self.find_element(location)
        pybi_element.click()

    def right_click(self, location):

        self.wait_element(location)
        pybi_element = self.find_element(location)
        ActionChains(self.driver).context_click(pybi_element).perform()

    def close(self):

        self.driver.close()

    def quit(self):

        self.driver.quit()

    def get_text(self, location):

        self.wait_element(location)
        pybi_element = self.find_element(location)
        return pybi_element.text

    def get_display(self, location):

        self.wait_element(location)
        el = self.find_element(location)
        return el.is_displayed()

    def get_title(self):

        return self.driver.title

    def get_url(self):

        return self.driver.current_url

    def wait(self, stime):

        self.driver.implicitly_wait(stime)

    def switch_to_frame(self, location):
        '''
        切换到新的窗口

        用法:
        driver.switch_to_frame("location=>#classname")
        '''
        self.wait_element(location)
        iframe_el = self.find_element(location)
        self.driver._switch_to.frame(iframe_el)


if __name__ == '__main__':

    driver = Pybi("chrome")