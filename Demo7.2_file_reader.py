file_path='data/pi_digits.txt'
with open(file_path) as file_objection:
    lines=file_objection.readlines()
#readlines() 读取每一行，并存储在一个列表中
    
pi_string=''
for line in lines:
    pi_string+=line.strip()

print(pi_string)
print(len(pi_string))
