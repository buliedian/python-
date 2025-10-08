
/*
1.1数据库创建
	创建数据库 create database 数据库名；
	判断后创建数据库 create database  if not exists 数据库名;
	创建数据库指定字符集 create database 数据库名 character set 字符集；
	创建数据库指定排序方式 create database 数据库名 collate 排序方式;
	创建数据库指定字符集和排序方式 create database 数据库名 character set 字符集 collate 排序方式；
	查询数据库的字符集和排序方式
		mysql8:默认 utf8mb4 utfmb4_0900_ai_ci
		show variables like 'character_set_database';
		show variables like 'collation_database';
        练习：创建ddl_d1库，指定字符集为utf8,且排序方式为大小写敏感的utf8mb4_0900_as_cs模式
        create databade ddl_dl character set utf8 collate utf8mb4_0900_as_cs;
*/
CREATE DATABASE IF NOT EXISTS ddl_d1 CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_as_cs;
/*1.2数据库查看
	查看所有数据库 show databases；
	查看当前数据库 select database();
	查看库下所有表 show tables from 数据库名;
	查看创建库的信息与语句 show create database 数据库名；
	选中的切换库 use 数据库名;
	注意：对数据库进行操作之前，必选要选中数据库。 use 数据库；
	*/
SHOW DATABASES;
SELECT DATABASE();
USE mysql;
SHOW TABLES FROM mysql;
SHOW CREATE DATABASE ddl_d1;
/*1.3数据库修改
	修改字符集 alter database 数据库名 character set 字符集；
	修改排序方式 alter database 数据库名 collate 排序方式；
	修改字符集和排序方式 alter if exists database 数据库名 character set 字符集 collate 排序方式；
	注意：数据库中没有修改数据库名的方法。如果要这样，首先备份数据，删除旧库，创建新库，回复数据。
	*/
/*1.4数据库删除
	直接删除 drop database 数据库名；
	判断删除 drop database if exists 数据库名；
	注意：删除是一个非常危险的命令，一定要慎重。
	*/
CREATE DATABASE IF NOT EXISTS blog_platform CHARACTER SET utf8mb4;
SHOW DATABASES;
USE blog_platform;
SHOW CREATE DATABASE blog_platform;
SHOW VARIABLES LIKE 'character_set_database';
SHOW VARIABLES LIKE 'collation_database';
ALTER DATABASE blog_platform COLLATE utf8mb4_0900_as_cs;
DROP DATABASE IF EXISTS blog_platform;

/*answer
	create database if not exists blog_platform character set utf8mb4;
	use blog_platform;
	show variables like 'character_set_database';
	show variables like 'collation_database';
	alter database blog_platform collate utfmb4_0900_as_cs;
	drop database if exists blog_platform;
	show databases;
*/
