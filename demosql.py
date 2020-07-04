'''
@Author: YanQiaoYu
@Github: https://github.com/yanqiaoyu?tab=repositories
@Date: 2020-07-01 10:25:01
@LastEditors: YanQiaoYu
@LastEditTime: 2020-07-04 10:01:44
@FilePath: /Sleepway2work/sql.py
'''
import pymysql

class mysql:

    def __init__(self):
        for i in range(3):
            try:
                # 打开数据库连接
                self.db = pymysql.connect("","root","","sleepway2work")
                # 使用 cursor() 方法创建一个游标对象 cursor
                self.cursor = self.db.cursor()  
            except:
                continue      

    '''
    @description: 用以外部调用，进行数据更新
    @param {type} 
    @return: True:更新成功 
             False:更新失败 或 不需更新
    '''
    def UpdateMyData(self, dic):
        #获取更新前的数据
        if True == self.SelectOldData(dic):
            return True
        else:
            return False



    def SelectOldData(self, newDic):
        #对比传进来的值与旧的值，若相等则无需更新，返回False
        for key in newDic:
            try:
                self.cursor.execute("select itemCount from mytable where itemName='{}';".format(key))
                data = self.cursor.fetchone()
                if float(data[0]) == float(newDic[key]):
                    #一致，无需更新
                    continue
                else:
                    print("Data is {}, New data is {}".format(data[0], newDic[key]))
                    #key: key , newValue:newDic[key] oldValue:data[0]
                    #把oldvalue 更新到 oldItemCount newvalue 更新到 itemCount
                    self.cursor.execute("update mytable set oldItemCount='{}' where itemName='{}';".format(data[0], key))
                    self.cursor.execute("update mytable set itemCount='{}' where itemName='{}';".format(newDic[key], key))                    
            except:
                print("Something wrong")
                return False
        return True
    
    def CommitAndClose(self):
        # 关闭数据库连接
        self.db.commit()
        self.cursor.close()
        self.db.close()
    
    def RollBackAndClose(self):
        # 关闭数据库连接
        self.db.rollback()
        self.cursor.close()
        self.db.close()