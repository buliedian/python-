alien_0={'color':'green','speed':'slow'}
#print(alien_0['points'])这是个错误的举例
#get指定键返回默认值
point_value=alien_0.get('points',"找不到")
print(point_value)
#6.2
OnePerson={'firstname':'zhang','lastname':'fei',\
           'age':18,'city':'whhan'}
print("this person's message")
print(OnePerson)
print(OnePerson.items())
#items() 返回键值列表
for i,j in OnePerson.items():
    print(i+'\n')
    print(j)
#keys()遍历所有键
for key in OnePerson.keys():
    print(f'key is {key}\n')

favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby'
    }
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()},thank you for talking the poll")

lang=favorite_languages
print(lang.values())
print(type(lang.values()))
for lan in set(lang.values()):
    print(lan.title())




#批量创建外星人
    aliens=[]
    for alien_number in range(30):
        new_alien={
            'color':'green',
            'points':'5',
            'speed':'slow'
            }
        aliens.append(new_alien)

    for alien in aliens[:5]:
        print(alien)
    print(f'Total number of aliens is {len(aliens)}')




















    

    
           
