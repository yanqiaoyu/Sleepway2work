# -*- coding: UTF-8 -*- 
#import uiautomator2 as u2
import time
from airtest.core.api import *

class Alipay:

   ImgPath = "./AlipayImg/"
   
   def __init__(self,d):
      self.d =  d
      #Airtest初始化
      init_device("Android")
      

   #增加运动步数
   def Sports(self):

      #打开支付宝
      self.d.app_start("com.eg.android.AlipayGphone", stop=True)
      #不等4秒竟然有时候点不到
      time.sleep(4)
      #进入运动
      self.d(resourceId="com.alipay.android.phone.openplatform:id/app_text", text="运动").click()
      time.sleep(2)
      #进入走路线
      self.d(text="走路线").click()

      #先点宝箱
      while exists(Template(self.ImgPath+"PurpleChest.png")):
         touch(Template(self.ImgPath+"PurpleChest.png"))
         sleep(2)
         self.d(text="收下运动币").click()

      time.sleep(2)

      RunCoin = self.d.xpath('//*[@resource-id="__react-content"]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[2]').get_text()
      print("Now RunCoin:",RunCoin)

      #GO
      self.d.xpath('//*[@resource-id="__react-content"]/android.view.View[1]/android.view.View[6]/android.view.View[2]').click()

   
   #赶走盗贼小鸡
   def KickThiefChicken(self):

      self.d.app_start("com.eg.android.AlipayGphone", stop=True)
      time.sleep(3)
      self.d(resourceId="com.alipay.android.phone.openplatform:id/app_text", text="蚂蚁庄园").click()

      time.sleep(3)
      #判断当前有没有盗贼鸡
      if not exists(Template(self.ImgPath+"ThiefChicken.png")):
         print("No Thief Chicken Now~")
         return -1
      else:
         while exists(Template(self.ImgPath+"ThiefChicken.png")):
            touch(Template(self.ImgPath+"ThiefChicken.png"))
            time.sleep(3)
            touch(Template(self.ImgPath+"KickThiefChicken.png"))
            time.sleep(3)
            touch(Template(self.ImgPath+"NoComment.png"))

   
   #最好把这个公众号置顶,这样就不需要做一个“找不到就往下滚”的操作了
   def GoldTicket(self):
      
      #打开支付宝
      self.d.app_start("com.eg.android.AlipayGphone", stop=True)

      #进入朋友界面
      self.d(resourceId="com.alipay.mobile.socialwidget:id/social_tab_text").click()

      #进入蚂蚁财富公众号
      self.d(text="蚂蚁财富").click()

      #领取黄金票
      self.d(text="天天领黄金").click()
      
      #获取当前黄金票的数量，这种获取方式鲁棒性不太行，暂时没有找到更好的办法
      nowGoldTicket = self.d.xpath('//*[@resource-id="root"] \
                        /android.view.View[2]/android.view.View[1]/android.view.View[3] \
                        /android.view.View[2]/android.view.View[1]').get_text()
      print("Now we have Gold Ticket:%s" % nowGoldTicket)