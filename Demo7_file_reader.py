#相对路径
#with open('data/pi_digits.txt') as file_object:

#绝对路径
file_path='D:/pi_digits.txt'
with open(file_path) as file_object:
    contents=file_object.read()
print(contents.rstrip())

#open() 接受打开文件参数，在当前目录查找，返还表示文件的对象
#关键字with表示不再访问文件后将其关闭
