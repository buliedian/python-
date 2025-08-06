#String

#q2.3
name1="eric"
name1=name1.title()
message=f"Hello {name1},would you like to learn some Pthon today?"
print(message)


#2.4
last_name='zhang'
first_name='fei'
full_name=f'{last_name}{first_name}'
print(full_name)
name_upper=f'{last_name.upper()}{first_name.upper()}'
print(name_upper)
name_title=f'{last_name.title()}{first_name.title()}'
print(name_title)


#2.5
famous_person="Albert Einstein"
message=f'{famous_person} once said," A person who never made a mistake never \
tried anything new "'
print(message)

#2.6
name1='\tzhang fei\t'
name2='zhangsan\nsss'
print(name1)
print(name1.lstrip())
print(name1.rstrip())
print(name1.strip())


