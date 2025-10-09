# 7、安装失败问题

## 安装问题1：无法打开MySQL8.0软件安装包？

​    在运行MySQL8.0软件安装包之前，用户需要确保系统中已经安装了.Net Framework相关软件，如果缺少此软件，将不能正常地安装MySQL8.0软件

![image-20211127170411358](MySQL8.0_安装和使用文档.assets/image-20211127170411358.png)

解决方案：到这个地址https://www.microsoft.com/en-us/download/details.aspx?id=42642下载Microsoft .NET Framework 4.5并安装后，再去安装MySQL。

## 安装问题2：需要C++库

另外，还要确保Windows Installer正常安装。Windows上安装MySQL8.0需要操作系统提前已安装好Microsoft Visual C++ 2015-2019。

![image-20211127170434387](MySQL8.0_安装和使用文档.assets/image-20211127170434387.png)

## 安装问题3：丢失MSVCP140.dll

![image-20211127170442613](MySQL8.0_安装和使用文档.assets/image-20211127170442613.png)

解决方案同样是，提前到微软官网https://support.microsoft.com/en-us/topic/the-latest-supported-visual-c-downloads-2647da03-1eea-4433-9aff-95f26a218cc0下载相应的环境。

如果电脑提示需要更新操作系统，请做好更新后再安装。

# 8、MySQL实例初始化失败问题

## 问题1：初始化系统库失败之中文乱码问题

例如：

mysqld: File '.\绐︽枃褰?bin.index' not found (OS errno 2 - No such file or directory)

解决方法：【计算机】右键-->【属性】  重命名计算机设备名称

![image-20220222180637898](MySQL8.0_安装和使用文档.assets/image-20220222180637898.png)

## 问题2：mysql服务启动失败

MySQL error 1042: Unable to connect to any of the specified MySQL hosts.

![image-20220222181221100](MySQL8.0_安装和使用文档.assets/image-20220222181221100.png)

![image-20220222181414534](MySQL8.0_安装和使用文档.assets/image-20220222181414534.png)

解决方案：

如果是专业版操作系统：

电脑–>管理–>本地用户和组–>组–>双击Administrators–>添加–>高级
把NETWORK SERVICE添加到Administrators组

![image-20220222182053069](MySQL8.0_安装和使用文档.assets/image-20220222182053069.png)

如果是家庭版操作系统：

计算机（点击鼠标右键）》管理（点击）》服务和应用程序（点击）》服务（点击）》MySQL80（点击鼠标右键）》属性》登录选项卡下将选择的此账户改为选择本地系统账户。之后重新执行excute

![image-20220222182341155](MySQL8.0_安装和使用文档.assets/image-20220222182341155.png)

![image-20220222182425252](MySQL8.0_安装和使用文档.assets/image-20220222182425252.png)

# 9、可视化工具连接MySQL8问题

有些图形界面工具，特别是旧版本的图形界面工具，在连接MySQL8时出现“Authentication plugin 'caching_sha2_password' cannot be loaded”错误。

![image-20211127170917407](MySQL8.0_安装和使用文档.assets/image-20211127170917407.png)

出现这个原因是MySQL8之前的版本中加密规则是mysql_native_password，而在MySQL8之后，加密规则是caching_sha2_password。

解决问题方法有两种：

第一种是升级图形界面工具版本。

第二种是把MySQL8用户登录密码加密规则还原成mysql_native_password。

第二种解决方案如下，用命令行登录MySQL数据库之后，执行如下命令修改用户密码加密规则并更新用户密码，这里修改用户名为“root@localhost”的用户密码规则为“mysql_native_password”，密码值为“123456”。

```sql
#修改'root'@'localhost'用户的密码规则和密码
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '密码'; 
#刷新权限
FLUSH PRIVILEGES;
```

![image-20211127171046998](MySQL8.0_安装和使用文档.assets/image-20211127171046998.png)

# 10、mysql8忘记root用户密码

当出现忘记root用户密码的情况时，如果此时有其他用户拥有系统库mysql的user表的UPDATE权限，可以由其他用户通过SET语句修改root用户密码。但是如果遇到一种特殊情况，此时没有其他用户，或者其他用户没有系统库mysql的user表的UPDATE权限，也没有GRANT（给用户授权）的权限，那么怎么处理呢？操作步骤如下：

1.首先停止mysql的服务
2.新建一个文本文件，文本文件中就写一条修改密码的语句

```mysql
ALTER USER 'root'@'localhost' IDENTIFIED BY '123456';
```

例如在D盘根目录下新建一个文本文件“root_newpass.txt”，文件内容就上面一条语句。

![image-20211128193356182](MySQL8.0_安装和使用文档.assets/image-20211128193356182.png)

![image-20211128193420899](MySQL8.0_安装和使用文档.assets/image-20211128193420899.png)

3.使用管理员权限运行cmd命令行，运行以下命令：

```mysql
mysqld --defaults-file="D:\ProgramFiles\MySQL\MySQLServer8.0_Data\my.ini" --init-file="d:\root_newpass.txt"
```

注意：my.ini文件的路径看你自己的安装路径，找数据目录

![image-20211128193734236](MySQL8.0_安装和使用文档.assets/image-20211128193734236.png)

上面命令意思就是初始化启动一次数据库，并运行这个修改密码的文件。效果演示如下：

![image-20211128193623962](MySQL8.0_安装和使用文档.assets/image-20211128193623962.png)

上面的命令执行后，就像卡住了一样，这就是启动MySQL服务了。

4.然后按CTRL+C结束上面的运行命令

![image-20211129084057307](MySQL8.0_安装和使用文档.assets/image-20211129084057307.png)

5.最后重新启动MySQL服务，用新密码登录即可

# 11、修改用户密码（记得原密码）

在命令行可以使用mysqladmin命令修改用户密码，命令格式如下：

```mysql
mysqladmin -u 用户名 -h 主机名  -p password "新密码"
Enter password:输入旧密码
```

![image-20211128194355818](MySQL8.0_安装和使用文档.assets/image-20211128194355818.png)

# 14、修改用户密码（不记得原密码）

例如：“root”用户登录后，修改用户名为“shangguigu1”，主机名为“localhost”的用户的密码为“atguigu”。

```mysql
SET PASSWORD FOR 'shangguigu1'@'localhost' = '新密码';
```

![image-20211128194603636](MySQL8.0_安装和使用文档.assets/image-20211128194603636.png)

