'''
@Author: YanQiaoYu
@Github: https://github.com/yanqiaoyu?tab=repositories
@Date: 2020-06-10 23:01:57
@LastEditors: YanQiaoYu
@LastEditTime: 2020-06-24 20:17:17
@FilePath: /Sleepway2work/JingDong.py
'''

import uiautomator2 as u2
import time
from airtest.core.api import *

class JingDong:
    ImgPath = "./JingDongImg/"
    Time2Wait = 6
    
    def __init__(self, d):
        self.d =  d
        init_device("Android")

    '''
    @description: 京东-> 签到领京豆
    @param {type} 
    @return: 
    '''
    def JingDou(self):
        #确保每次打开都是重新打开,而不是调用后台已存在的进程
        self.d.app_start("com.jingdong.app.mall", stop=True)

        time.sleep(self.Time2Wait)

        #进入个人页面
        self.d(resourceId="com.jingdong.app.mall:id/xk", text="我的").click()

        time.sleep(self.Time2Wait)

        #进入签到
        self.d(resourceId="com.jd.lib.personal:id/ah9", text="京豆").click()

        time.sleep(self.Time2Wait)

        #签到
        try:
            
            self.d(text="去签到领京豆").click()
            
            time.sleep(self.Time2Wait)
            '''
            self.d(text="签到领京豆").click()

            time.sleep(self.Time2Wait)

            self.d.press("back")

            time.sleep(self.Time2Wait)
            '''

            self.d(text="抽京豆").click()

            GoIndex = assert_exists(Template(self.ImgPath+"GO.png"))
            touch(GoIndex)
        except Exception:
            self.d.press("back")
            time.sleep(self.Time2Wait)
            JingDou = self.d(resourceId="com.jd.lib.personal:id/ah_").get_text()
            print(JingDou)
        
        time.sleep(self.Time2Wait)

    '''
    @description: 京东金融 -> 签到领钢镚
    @param {type} 
    @return: 
    '''    
    def GangBeng(self):
        #打开APP
        self.d.app_start("com.jd.jrapp", stop=True)

        time.sleep(self.Time2Wait)

        self.d(resourceId="com.jd.jrapp:id/home_header_grid_title", text="每日签到").click()
        

        time.sleep(self.Time2Wait)

        if exists(Template(self.ImgPath+"GetGangBeng.png")):
            touch(Template(self.ImgPath+"GetGangBeng.png"))

        time.sleep(self.Time2Wait)

    '''
    @description: 京东金融 -> 京贴
    @param {type} 
    @return: 
    '''
    def JingTie(self):
        #打开APP
        self.d.app_start("com.jd.jrapp", stop=True)

        time.sleep(self.Time2Wait)
        
        #self.d(resourceId="com.jd.jrapp:id/home_header_grid_title", text="领金贴").click()
        swipe((540, 1550),(540, 950))

        time.sleep(self.Time2Wait)

        try:
            self.d(resourceId="com.jd.jrapp:id/tv_profit", text="金贴").click()
            time.sleep(self.Time2Wait)
            self.d(text="签到领金贴").click()
            time.sleep(self.Time2Wait)
        except Exception:
            pass

    '''
    @description: 京东 -> 双签奖励
    @param {type} 
    @return: 
    '''    
    def DoubleCheck(self):
        #确保每次打开都是重新打开,而不是调用后台已存在的进程
        self.d.app_start("com.jingdong.app.mall", stop=True)

        time.sleep(self.Time2Wait)

        #进入个人页面
        self.d(resourceId="com.jingdong.app.mall:id/xk", text="我的").click()

        time.sleep(self.Time2Wait)

        #进入签到
        self.d(resourceId="com.jd.lib.personal:id/ah9", text="京豆").click()

        time.sleep(self.Time2Wait)

        #签到
        try:
            self.d(text="已签到").click()

            time.sleep(self.Time2Wait)

            self.d(text="双签领豆").click()

            if exists(Template(self.ImgPath+"CompleteDoubleCheck.png")):
                time.sleep(self.Time2Wait)
                touch(Template(self.ImgPath+"CompleteDoubleCheck.png"))
        except Exception:
            pass

        time.sleep(self.Time2Wait)