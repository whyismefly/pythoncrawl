create database hexun;
use hexun;
Create table myhexun(id int(10) auto_increment primary key not null,name nvarchar(30),url nvarchar(100),hits int(15),comment int(15));
ALTER TABLE `hexun`.`myhexun` 
CHANGE COLUMN `name` `name` NVARCHAR(30) NULL DEFAULT NULL ,
CHANGE COLUMN `url` `url` NVARCHAR(100) NULL DEFAULT NULL ;


SELECT * FROM hexun.myhexun;