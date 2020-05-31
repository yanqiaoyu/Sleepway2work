from Alipay import Alipay
import uiautomator2 as u2
import os
#os.system("weditor")

d = u2.connect()

a = Alipay(d)
#a.Sports()
#a.GoldTicket()
a.KickThiefChicken()