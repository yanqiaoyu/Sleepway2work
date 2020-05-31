# -*- coself.ding: UTF-8 -*- 
import uiautomator2 as u2
import time
from connmysql import ConnDB

class dotamax():
   def __init__(self,d):
      self.d =  d

   def Gold(self):
      print(self.d.info)
      #确保每次打开都是重新打开,而不是调用后台已存在的进程
      self.d.app_start("com.dotamax.app", stop=True)

      #每日签到成功后,点击确定
      #监控弹窗(在线程中监控)
      self.d.watcher.when("确定").click()
      self.d.watcher.start()
      time.sleep(10)
      self.d.watcher.stop()

      #点击左上角的用户资料
      self.d(resourceId="com.dotamax.app:id/fl_user_title_icon").click()

      #获取当前的金币数
      nowGold = self.d(resourceId="com.dotamax.app:id/tv_max_coin").get_text()
      localtime = time.asctime( time.localtime(time.time()))
      print(localtime,"Now Gold:",nowGold)

      '''
      db = ConnDB()
      # 创建游标
      cursor = db.connect()
      cursor.execute("SELECT itemCount FROM mytable where AppName='dotamax' and itemName='goldcoin'")
      row_2 = cursor.fetchall()
      print(row_2)

      time.sleep(3)
      '''
      #关闭当前APP,这里如果用了app_clear会导致需要重新登陆账号
      self.d.app_stop('com.dotamax.app')

handle = dotamax(u2.connect())
handle.Gold()

