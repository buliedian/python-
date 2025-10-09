# 2、MySQL数据库的安装（Mac）

<font color='red'>**注意：**</font>

<font color='red'>**必须用系统管理员身份运行mysql安装程序。**</font>

<font color='red'>**安装目录切记不要用中文。**</font>



## 步骤一：双击mysql8的安装向导

![1702303587689](MySQL8.0_安装和使用文档.assets\1702303587689.png)

## 步骤二：安装mysql

### 1、是否允许

![1702303706150](MySQL8.0_安装和使用文档.assets\1702303706150.png)

### 2、安装进度页面

![1702303884242](MySQL8.0_安装和使用文档.assets\1702303884242.png)

一直继续即可，直到configuration配置为止！

### 3、configuration配置选项

![1702303980348](MySQL8.0_安装和使用文档.assets\1702303980348.png)

选第一个，8.0新版本密码！！

![1702304070468](MySQL8.0_安装和使用文档.assets\image-20211127105018580.png)

输入一个至少八位的密码即可！finish,如果不变颜色证明密码位数不够！

### 4、mysql服务启动和停止

电脑/系统设置/最后有mysql服务

![1702304445489](MySQL8.0_安装和使用文档.assets\1702304445489.png)



## 步骤三：环境变量配置

### 1、mysql命令失效

​		 打开mac终端，输入mysql！！！

![1702304660221](MySQL8.0_安装和使用文档.assets\1702304660221.png)

### 2、 mysql环境变量

1. 打开环境配置文件

   vim  ~/.bash_profile

2. 加入mysql环境

   按 i 进入输入模式！

   PATH加入mysql路径/usr/local/mysql/bin

   ``` 
   # Setting PATH for Python 3.7
   # The original version is saved in .bash_profile.pysave
   # 在此处加入mysql/bin，多个变量之间使用：隔开！(/usr/local/mysql/bin  mysql安装位置)
   PATH="/usr/local/mysql/bin:/Library/Frameworks/Python.framework/Versions/3.7/bin:${PATH}"
   export M2_HOME=/Users/zhaoweifeng/maven/apache-maven-3.6.0
   export PATH=$PATH:$M2_HOME/bin
   export WORKON_HOME=$HOME/pythonvirtualenv
   export PROJECT_HOME=$HOME/PycharmProjects
   
   export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.ustc.edu.cn/homebrew-bottles/bottles #ckbrew
     eval $(/usr/local/Homebrew/bin/brew shellenv) #ckbrew
   ```

   退出保存

   esc

   shfit + ：

   wq （保存并退出）

3. 刷新环境文件

   ``` 
   source ~/.bash_profile
   ```

   

### 3、 测试链接

 打开mac终端，输入mysql！！！

``` 
mysql -uroot -p密码
```



