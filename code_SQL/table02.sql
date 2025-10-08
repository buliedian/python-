#2.DDL数据表的操作
/*2.1建表语法
	建表语法总结
 create table [if not exists] 表名（
 #列的信息
 列名 类型 [列的约束] [列的注释]，
 列名 类型 [列的约束] [列的注释]，
 ......
 列名 类型 [列的约束] [列的注释]
 ）[描述] [注释]

建表事项:
1.表名，列名，列类型 必须填写
2.推荐使用 if not exists 
*/


#短语表的小练习
CREATE DATABASE IF NOT EXISTS book_libs CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_as_cs;
USE book_libs;
CREATE TABLE IF NOT EXISTS books(
book_name VARCHAR(20) COMMENT '图书名称',
book_price DOUBLE(4,1) COMMENT '图书价格',
book_num INT COMMENT '图书数量'
)CHARSET=utf8mb4 COMMENT '图书表';

SHOW TABLES FROM book_libs;
