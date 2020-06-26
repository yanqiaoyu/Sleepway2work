'''
@Author: YanQiaoYu
@Github: https://github.com/yanqiaoyu?tab=repositories
@Date: 2020-06-01 23:06:39
@LastEditors: YanQiaoYu
@LastEditTime: 2020-06-26 10:35:21
@FilePath: /Sleepway2work/sleepway2work.py
'''
from Alipay import Alipay
from Maxplus import Maxplus
from JingDong import JingDong
import uiautomator2 as u2
import os

d = u2.connect()
d.unlock()

a = Alipay(d)
#a.Test()

a.Sports()
a.GoldTicket()
a.AntManor()
a.AntForest()

b = Maxplus(d)
b.Gold()

c = JingDong(d)
c.JingDou()
c.GangBeng()
c.JingTie()
c.DoubleCheck()