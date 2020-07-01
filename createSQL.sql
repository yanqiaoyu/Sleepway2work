create database if not EXISTS sleepway2work;

use sleepway2work;

create table if not exists mytable
(
    itemID int unsigned primary key not null auto_increment,
    AppName VARCHAR(20) NOT NULL,
    itemName VARCHAR(20) NOT NULL,
    itemCount FLOAT NOT NULL,
    oldItemCount FLOAT NOT NULL,
    updateTime timestamp NOT NULL ON UPDATE CURRENT_TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO mytable(AppName, itemName, itemCount, oldItemCount) 
VALUES('Maxplus', 'MaxplusGold', 0, 0);
INSERT INTO mytable(AppName, itemName, itemCount, oldItemCount) 
VALUES('Alipay', 'RunCoin', 0, 0);
INSERT INTO mytable(AppName, itemName, itemCount, oldItemCount) 
VALUES('Alipay', 'GoldTicket', 0, 0);
INSERT INTO mytable(AppName, itemName, itemCount, oldItemCount) 
VALUES('Alipay', 'Energy', 0, 0);
INSERT INTO mytable(AppName, itemName, itemCount, oldItemCount) 
VALUES('Alipay', 'Egg', 0, 0);
INSERT INTO mytable(AppName, itemName, itemCount, oldItemCount) 
VALUES('JingDong', 'JingDou', 0, 0);
INSERT INTO mytable(AppName, itemName, itemCount, oldItemCount) 
VALUES('JingDong', 'GangBeng', 0, 0);
INSERT INTO mytable(AppName, itemName, itemCount, oldItemCount) 
VALUES('JingDong', 'JingTie', 0, 0);


