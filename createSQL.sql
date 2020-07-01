create database if not EXISTS sleepway2work;

use sleepway2work;

create table if not exists mytable
(
    itemID int unsigned primary key not null auto_increment,
    AppName VARCHAR(20) NOT NULL,
    itemName VARCHAR(20) NOT NULL,
    itemCount INT NOT NULL,
    oldItemCount INT NOT NULL,
    updateTime DATETIME
);

INSERT INTO mytable(AppName, itemName, itemCount, oldItemCount, updateTime) 
VALUES('Maxplus', 'MaxplusGold', 0, 0, '1000-01-01 00:00:00');
INSERT INTO mytable(AppName, itemName, itemCount, oldItemCount, updateTime) 
VALUES('Alipay', 'RunCoin', 0, 0, '1000-01-01 00:00:00');
INSERT INTO mytable(AppName, itemName, itemCount, oldItemCount, updateTime) 
VALUES('Alipay', 'GoldTicket', 0, 0, '1000-01-01 00:00:00');
INSERT INTO mytable(AppName, itemName, itemCount, oldItemCount, updateTime) 
VALUES('Alipay', 'Energy', 0, 0, '1000-01-01 00:00:00');
INSERT INTO mytable(AppName, itemName, itemCount, oldItemCount, updateTime) 
VALUES('Alipay', 'Egg', 0, 0, '1000-01-01 00:00:00');
INSERT INTO mytable(AppName, itemName, itemCount, oldItemCount, updateTime) 
VALUES('JingDong', 'JingDou', 0, 0, '1000-01-01 00:00:00');
INSERT INTO mytable(AppName, itemName, itemCount, oldItemCount, updateTime) 
VALUES('JingDong', 'GangBeng', 0, 0, '1000-01-01 00:00:00');
INSERT INTO mytable(AppName, itemName, itemCount, oldItemCount, updateTime) 
VALUES('JingDong', 'JingTie', 0, 0, '1000-01-01 00:00:00');


