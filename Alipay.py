'''
@Author: YanQiaoYu
@Github: https://github.com/yanqiaoyu?tab=repositories
@Date: 2020-06-01 23:06:39
@LastEditors: YanQiaoYu
@LastEditTime: 2020-06-14 13:58:23
@FilePath: /Sleepway2work/Alipay.py
'''
import time
from airtest.core.api import *

class Alipay:

   ImgPath = "./AlipayImg/"
   Time2Wait = 4
   
   def __init__(self,d):
      self.d =  d
      #Airtest初始化
      init_device("Android")
      
   '''
   @description: 支付宝->运动、收币
   @param {type} 
   @return: 
   '''
   def Sports(self):

      #打开支付宝
      self.d.app_start("com.eg.android.AlipayGphone", stop=True)
      #不等4秒竟然有时候点不到
      time.sleep(self.Time2Wait)
      #进入运动
      self.d(resourceId="com.alipay.android.phone.openplatform:id/app_text", text="运动").click()
      time.sleep(self.Time2Wait)
      #进入走路线
      self.d(text="走路线").click()

      time.sleep(self.Time2Wait)

      #GO
      self.d.xpath('//*[@resource-id="__react-content"]/android.view.View[1]/android.view.View[6]/android.view.View[2]').click()

      #这里等久一点
      time.sleep(10)

      #点宝箱
      PurpleFlag = SuperPurpleFlag = GoldFlag = 1
      while True:

         if exists(Template(self.ImgPath+"PurpleChest.png")):
            touch(Template(self.ImgPath+"PurpleChest.png"))
            sleep(self.Time2Wait)
            self.d(text="收下运动币").click()
         else:
            PurpleFlag = 0

         if exists(Template(self.ImgPath+"SuperPurpleChest.png")):
            touch(Template(self.ImgPath+"SuperPurpleChest.png"))
            sleep(self.Time2Wait)
            self.d(text="收下运动币").click()
         else:
            SuperPurpleFlag = 0

         if exists(Template(self.ImgPath+"GoldChest.png")):
            touch(Template(self.ImgPath+"GoldChest.png"))
            sleep(self.Time2Wait)
            self.d(text="收下运动币").click()
         else:
            GoldFlag = 0

         if PurpleFlag == SuperPurpleFlag == GoldFlag == 0:
            break

      time.sleep(self.Time2Wait)

      RunCoin = self.d.xpath('//*[@resource-id="__react-content"]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[2]').get_text()
      print("Now RunCoin:",RunCoin)

      time.sleep(self.Time2Wait)

   '''
   @description: 支付宝->蚂蚁庄园->赶走盗贼、找回小鸡、喂鸡
   @param {type} 
   @return: 
   '''
   def AntManor(self):

      self.d.app_start("com.eg.android.AlipayGphone", stop=True)
      time.sleep(self.Time2Wait)
      self.d(resourceId="com.alipay.android.phone.openplatform:id/app_text", text="蚂蚁庄园").click()
      time.sleep(self.Time2Wait)

      #检测盗贼鸡
      if not exists(Template(self.ImgPath+"ThiefChicken.png")):
         print("No Thief Chicken Now~")
         pass
      else:
         while exists(Template(self.ImgPath+"ThiefChicken.png")):
            touch(Template(self.ImgPath+"ThiefChicken.png"))
            time.sleep(self.Time2Wait)
            touch(Template(self.ImgPath+"KickThiefChicken.png"))
            time.sleep(self.Time2Wait)
            touch(Template(self.ImgPath+"NoComment.png"))

      time.sleep(self.Time2Wait)

      #找回我们的小鸡
      if exists(Template(self.ImgPath+"GotoCallBack.png")):
         touch(Template(self.ImgPath+"GotoCallBack.png"))
         sleep(self.Time2Wait)
         touch(Template(self.ImgPath+"CallBackOurChicken.png"))
         sleep(self.Time2Wait)

      #喂饲料，不管有没有都退出
      touch(Template(self.ImgPath+"feed.png"))

      time.sleep(self.Time2Wait)
   
   '''
   @description: 支付宝->朋友->蚂蚁财富
   @param {type} 
   @return: 
   '''
   #最好把这个公众号置顶,这样就不需要做一个“找不到就往下滚”的操作了
   def GoldTicket(self):
      
      #打开支付宝
      self.d.app_start("com.eg.android.AlipayGphone", stop=True)

      sleep(self.Time2Wait)

      #进入朋友界面
      self.d(resourceId="com.alipay.mobile.socialwidget:id/social_tab_text").click()

      sleep(self.Time2Wait)

      #进入蚂蚁财富公众号
      self.d(text="蚂蚁财富").click()

      sleep(self.Time2Wait)

      #假设今天蚂蚁财富并没有开放这个接口到首页,需要一个备份方案
      try:
         #领取黄金票
         self.d(text="天天领黄金").click()
         if not self.d(text="提取黄金").exists():
            raise Exception("Not this way!")
      except:
         print("Chosing Another Way to Gold Ticket")
         self.d.press("back")
         sleep(self.Time2Wait)
         self.d(resourceId="com.alipay.android.widget.fortunehome:id/tab_description").click()
         sleep(self.Time2Wait)
         self.d(resourceId="com.alipay.android.widget.fortunehome:id/title", text="黄金").click()
         sleep(self.Time2Wait)
         self.d(text="黄金票").click()
         

      sleep(self.Time2Wait)

      #领完黄金票，点击XX
      if self.d.xpath('//*[@resource-id="root"] \
                        /android.view.View[13] \
                        /android.view.View[3] \
                        /android.view.View[2]').exists:
         self.d.xpath('//*[@resource-id="root"] \
                        /android.view.View[13] \
                        /android.view.View[3] \
                        /android.view.View[2]').click()

      sleep(self.Time2Wait)
      
      #获取当前黄金票的数量
      tmpStack=[]
      for elem in self.d.xpath("//android.view.View").all():
         if elem.text:   
            tmpStack.append(elem.text)
            if elem.text=='份':
               nowGoldTicket = tmpStack[-2]

      sleep(self.Time2Wait)

      print("Now we have Gold Ticket:%s" % nowGoldTicket)

   '''
   @description: 支付宝->蚂蚁森林
   @param {type} 
   @return: 
   '''
   def AntForest(self):
      #打开支付宝，进入蚂蚁森林
      self.d.app_start("com.eg.android.AlipayGphone", stop=True)
      sleep(self.Time2Wait)
      self.d(resourceId="com.alipay.android.phone.openplatform:id/app_text", text="蚂蚁森林").click()
      time.sleep(self.Time2Wait)

      #收集能量
      #由于广告中也可能存在能量球被匹配到，所以设置一个跳出下面这个循环的计时器
      WhileCount = 0
      while exists(Template(self.ImgPath+"Energy.png")) and WhileCount < 5:
         touch(Template(self.ImgPath+"Energy.png"))
         WhileCount += 1

      time.sleep(self.Time2Wait)

      #获取当前能量
      NowEnergy = self.d(resourceId="J_userEnergy").get_text()
      print("Now Energy is %s", NowEnergy)

      time.sleep(self.Time2Wait)


   '''
   @description: 仅用于测试
   @param {type} 
   @return: 
   '''
   def Test(self):
      '''
      while exists(Template(self.ImgPath+"Energy.png")):
         touch(Template(self.ImgPath+"Energy.png"))
      '''
      #领完黄金票，点击XX
      if self.d.xpath('//*[@resource-id="root"] \
                        /android.view.View[13] \
                        /android.view.View[3] \
                        /android.view.View[2]').exists:
         self.d.xpath('//*[@resource-id="root"] \
                        /android.view.View[13] \
                        /android.view.View[3] \
                        /android.view.View[2]').click()
