file_path="E:\Desktop\源代码文件\源代码文件\chapter_10\pi_million_digits.txt"
with open(file_path) as file_objection:
    lines=file_objection.readlines()

pi_string=''
for line in lines:
    pi_string+=line.strip()

birthday=input("输入你的生日:w")
if birthday in pi_string:
    print("yes")
else:
    print("No")
