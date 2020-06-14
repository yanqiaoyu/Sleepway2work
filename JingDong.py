'''
@Author: YanQiaoYu
@Github: https://github.com/yanqiaoyu?tab=repositories
@Date: 2020-06-10 23:01:57
@LastEditors: YanQiaoYu
@LastEditTime: 2020-06-10 23:21:20
@FilePath: /Sleepway2work/JingDong.py
'''

import uiautomator2 as u2
import time

class JingDong:

    Time2Wait = 5
    
    def __init__(self, d):
        self.d =  d

    '''
    @description: 签到领京豆
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

        #
        self.d(text="去签到领京豆").click()

        time.sleep(self.Time2Wait)

        self.d(text="签到领京豆").click()
        