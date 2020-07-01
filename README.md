# Sleepway2work
让通勤时间拿来小憩，而不是点开各种APP进行签到

## 这个项目是用来做什么的？
通过[UIAutomator2](https://github.com/openatx/uiautomator2)，以及[Airtest](https://github.com/AirtestProject/Airtest)这两个本来用作APP自动化测试的框架，帮助我们实现在各种APP上完成一些诸如签到，领取XXX等日常操作。(通常这些事情我一般都会在通勤时间完成，但是每天来一次挺累的，为什么不做成自动化呢^_^)

## 如何使用？
首先你需要安装好[UIAutomator2](https://github.com/openatx/uiautomator2)，以及[Airtest](https://github.com/AirtestProject/Airtest)
具体的安装方法可以参考他们各自的Readme
安装好之后，如无异常，执行 sleepway2work.py 即可
```shell
python3 sleepway2work.py
```
注意：

1.请保持UIAutomator2与手机的通信顺畅

2.启动脚本时，请关闭Lantern(如果有开)，否则会出现启动异常


## 目前支持的自动化

### 阿里系

#### 支付宝

- [x] 支付宝运动:收集运动币，更新今日步数
- [x] 支付宝蚂蚁庄园:赶走盗贼小鸡，或者前往好友处召回小鸡并举报他人盗贼小鸡（如果有），喂鸡
- [x] 支付宝蚂蚁财富:自动领取黄金票
- [x] 支付宝蚂蚁森林:自动收集绿色能量

 
### 京东系

#### 京东APP && 京东金融

- [x] 领取京豆/京豆转盘
- [x] 领取钢镚
- [x] 领取京贴
- [x] 在领取了京豆与钢镚后，自动完成双签奖励

### 其他

#### MAX+

- [x] 上线即可领取M币

## 未来可能会完成的事情
- [ ] 每日签到完成后，收集当日的所有新数据，上传至个人服务器的数据库中
- [ ] 数据库的数据，可以发送到我的个人公众号上

~~- [X] 输出关键日志，记录每日签到的数据~~
