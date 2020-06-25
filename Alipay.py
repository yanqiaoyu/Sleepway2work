'''
@Author: YanQiaoYu
@Github: https://github.com/yanqiaoyu?tab=repositories
@Date: 2020-06-01 23:06:39
@LastEditors: YanQiaoYu
@LastEditTime: 2020-06-25 08:52:20
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
         try:
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
         except Exception:
            break
         
      time.sleep(self.Time2Wait)

      #获取当前运动币的数量
      tmpStack=[]
      for elem in self.d.xpath("//android.view.View").all():
         if elem.text:   
            tmpStack.append(elem.text)
            if elem.text=='币':
               RunCoin = tmpStack[-2]
               
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
            try:
               touch(Template(self.ImgPath+"ThiefChicken.png"))
               time.sleep(self.Time2Wait)
               touch(Template(self.ImgPath+"KickThiefChicken.png"))
               time.sleep(self.Time2Wait)
               touch(Template(self.ImgPath+"NoComment.png"))
            except Exception:
               continue

      time.sleep(self.Time2Wait)

      '''
      #去朋友那里找回我们的小鸡
      if exists(Template(self.ImgPath+"GotoCallBack.png")):
         touch(Template(self.ImgPath+"GotoCallBack.png"))
         sleep(self.Time2Wait)
         #去了好友那里需要召回的是盗贼鸡
         #盗贼鸡存在两种可能,一种是其他人的盗贼鸡,一种是是自己的盗贼鸡
         #先利用find_all找出所有存在的鸡的坐标，再依次点击
         #这里不用exist的原因是，可能永远匹配别人的盗贼鸡而导致死循环
         Dic=find_all(Template(self.ImgPath+"ThiefChicken.png"))
         #Not Null
         if Dic:
            for i in Dic:   
               touch(i['result'])
               sleep(self.Time2Wait)
               if exists(Template(self.ImgPath+"InformFriendofThiefChicken.png")):
                  touch(Template(self.ImgPath+"InformFriendofThiefChicken.png"))
                  sleep(self.Time2Wait)

         sleep(self.Time2Wait)
      '''   
      #喂饲料
      touch(Template(self.ImgPath+"feed.png"))

      time.sleep(self.Time2Wait)

      if exists(Template(self.ImgPath+"FindChicken.png")):
         time.sleep(self.Time2Wait)
         touch(Template(self.ImgPath+"FindChicken.png"))
         time.sleep(self.Time2Wait)
         #去了好友那里需要召回的是盗贼鸡
         #盗贼鸡存在两种可能,一种是其他人的盗贼鸡,一种是是自己的盗贼鸡
         #先利用find_all找出所有存在的鸡的坐标，再依次点击
         #这里不用exist的原因是，可能永远匹配别人的盗贼鸡而导致死循环
         Dic=find_all(Template(self.ImgPath+"ThiefChicken.png"))
         time.sleep(self.Time2Wait)
         #Not Null
         if Dic:
            for i in Dic:   
               touch(i['result'])
               sleep(self.Time2Wait)
               if exists(Template(self.ImgPath+"InformFriendofThiefChicken.png")):
                  touch(Template(self.ImgPath+"InformFriendofThiefChicken.png"))
                  sleep(self.Time2Wait)         
         time.sleep(self.Time2Wait)
         touch(Template(self.ImgPath+"feed.png"))
      #获取爱心个数,饲料数
      #此应用暂不支持
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
         swipe((793, 573),(289, 573))
         sleep(self.Time2Wait)
         #领取黄金票
         self.d(text="天天领黄金").click()
         sleep(self.Time2Wait)
         '''
         if self.d(text="提取黄金").exists():
            pass
         elif self.d(text="立即领取").exists():
            self.d(text="立即领取").click()
         else:
            raise Exception("Not this way!")
         '''
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

      print("Now we have Gold Ticket:%s" % nowGoldTicket)
      
      sleep(self.Time2Wait)

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

      #如果存在弹窗广告
      if self.d(text="关闭蒙层").exists(timeout=3):
         self.d(text="关闭蒙层").click()
      

      #收集能量
      #广告中也可能存在能量球被匹配到
      Dic=find_all(Template(self.ImgPath+"Energy.png"))
      #If Not Null
      if Dic:
         for i in Dic:   
            touch(i['result'])
            sleep(self.Time2Wait)
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
      pass
      Dic=find_all(Template(self.ImgPath+"ThiefChicken.png"))
      print("We find:",Dic)
      if Dic:
         for i in Dic:
            print(i['result'])
            touch(i['result'])
   
   