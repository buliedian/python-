#3.1 and 3.2 and 3.3
names=['zhangsan','lisi','wangwu','zhangerniang']
for name in names:
    print(name)
for name in names:
    message=f'{name},hello'
    print(message)

list=['spring','autumn','summer','winter']
#修改 list[0]='chuntian'
#添加  append 列表末尾添加 list.append('five')
    #  insert 指定位置插入 list.insert(0,seanson)
#删除  del 删除指定位置 del list[0]
    #   pop 默认删除最后一个  list.pop()
    #       用索引删除指定元素   list.pop(1)
    #  remove 删除值的元素


#3.4
person_of_banquet=['a','b','c','d']
for person in person_of_banquet:
    message=f'dear {person},invite you to eat dinner'
    print(message)
print("c can't go")
person_of_banquet[2]='h'
print(f'{person_of_banquet[2]} will go')
person_of_banquet.insert(0,'e')
person_of_banquet.insert(2,'f')
person_of_banquet.append('g')
for person in person_of_banquet:
    message=f'dear {person},invite you to eat dinner'
    print(message)
list1=list
print(list1)
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)
# sorted() 临时排序
list2=['spring','autumn','summer','winter']
print("                    ")
print(list2)
print(sorted(list2))
print(list2)
list2.reverse()
print(list2)
print(len(list2))

#3.8
place=['hangzhou','shenzhen','xinjiang','beijing']
print(place)
print(sorted(place))
print(place)
print(len(place))



























