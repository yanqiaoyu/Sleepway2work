'''
@Author: YanQiaoYu
@Github: https://github.com/yanqiaoyu?tab=repositories
@Date: 2020-06-10 23:01:57
@LastEditors: YanQiaoYu
@LastEditTime: 2020-06-30 13:28:37
@FilePath: /Sleepway2work/JingDong.py
'''

import uiautomator2 as u2
import time
from airtest.core.api import *
from helper import logdeco

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
    @logdeco
    def JingDou(self):
        try:
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
            self.d(text="去签到领京豆").click()
            
            time.sleep(self.Time2Wait)
            
            self.d(text="签到领京豆").click()

            time.sleep(self.Time2Wait)

            self.d.press("back")

            time.sleep(self.Time2Wait)
            

            self.d(text="抽京豆").click()

            GoIndex = assert_exists(Template(self.ImgPath+"GO.png"))
            touch(GoIndex)
        except Exception:
            pass
        
        time.sleep(self.Time2Wait)

    '''
    @description: 京东金融 -> 签到领钢镚
    @param {type} 
    @return: 
    '''
    @logdeco    
    def GangBeng(self):
        #打开APP
        #考虑到可能有广告弹窗影响自动化的鲁棒性,增加for循环+try的代码
        for i in range(3):
            try:
                self.d.app_start("com.jd.jrapp", stop=True)

                time.sleep(self.Time2Wait)

                self.d(resourceId="com.jd.jrapp:id/home_header_grid_title", text="每日签到").click()
                

                time.sleep(self.Time2Wait)

                for i in range(3):
                    if exists(Template(self.ImgPath+"GetGangBeng.png")):
                        time.sleep(self.Time2Wait)
                        touch(Template(self.ImgPath+"GetGangBeng.png"))
                        break

                time.sleep(self.Time2Wait)
                break
            except Exception:
                continue

    '''
    @description: 京东金融 -> 京贴
    @param {type} 
    @return: 
    '''
    @logdeco
    def JingTie(self):
        #打开APP
        self.d.app_start("com.jd.jrapp", stop=True)

        time.sleep(self.Time2Wait)
        
        #self.d(resourceId="com.jd.jrapp:id/home_header_grid_title", text="领金贴").click()
        swipe((540, 1550),(540, 650))

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
    @logdeco
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
            for i in range(3):
                if exists(Template(self.ImgPath+"CompleteDoubleCheck.png")):
                    time.sleep(self.Time2Wait)
                    touch(Template(self.ImgPath+"CompleteDoubleCheck.png"))
                    break
        except Exception:
            pass

        time.sleep(self.Time2Wait)

    '''
    @description: 计算当前所有收益
    @param {type} 
    @return: 
    '''
    
    @logdeco
    def CaculateAll(self):
        result={}
        try:
            #确保每次打开都是重新打开,而不是调用后台已存在的进程
            self.d.app_start("com.jingdong.app.mall", stop=True)

            time.sleep(self.Time2Wait)

            #进入个人页面
            self.d(resourceId="com.jingdong.app.mall:id/xk", text="我的").click()

            time.sleep(self.Time2Wait)

            #这里本来想用遍历XPath的方式找到京豆的，但是Text为空
            JingDou = d(resourceId="com.jd.lib.personal:id/ah_").get_text()

            if JingDou:
                result["JingDou"] = JingDou
            else:
                result["JingDou"] = None
        except Exception:
            pass

        time.sleep(self.Time2Wait)

        try:               
            self.d.app_start("com.jd.jrapp", stop=True)

            time.sleep(self.Time2Wait)

            self.d(resourceId="com.jd.jrapp:id/iv_fifth_icon").click()

            time.sleep(self.Time2Wait)

            #钢镚
            Gangbeng = self.d(resourceId='com.jd.jrapp:id/tv_label_title', instance=1)
            #京贴
            JingTie = self.d(resourceId='com.jd.jrapp:id/tv_label_title', instance=2)

            if Gangbeng:
                result["GangBeng"] = Gangbeng
            else:
                result["GangBeng"] = None
            
            if JingTie:
                result["JingTie"] = JingTie
            else:
                result["Jingtie"] = None
        except Exception:
            pass
        
        return result