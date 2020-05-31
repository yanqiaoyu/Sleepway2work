drop database if exists sleepway2work;

create database sleepway2work;

use sleepway2work;

create table mytable
(
itemID int unsigned primary key not null auto_increment,
AppName VARCHAR(20) NOT NULL,
itemName VARCHAR(20) NOT NULL,
itemCount VARCHAR(20) NOT NULL,
updateTime DATE
);
