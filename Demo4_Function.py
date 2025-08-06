#位置参数
def describe_pet1(animal_type,pet_name):
    """显示宠物的信息"""
    print(f'\n i have a {animal_type}')
    print(f'my {animal_type} name is {pet_name}')

describe_pet1('dog','haha')

#关键词实参
def describe_pet2(animal_type,pet_name):
    """显示宠物的信息"""
    print(f'\n i have a {animal_type.title()}')
    print(f'my {animal_type.title()} name is {pet_name.title()}')

describe_pet2(animal_type='cat',pet_name='jojo')


#默认值
def describe_pet3(pet_name,animal_type='dog'):
    """显示宠物的信息"""
    print(f'\n i have a {animal_type.title()}')
    print(f'my {animal_type.title()} name is {pet_name.title()}')

describe_pet3(pet_name='wiwi')
describe_pet3('wiwi')


#实参可选
def get_formatted_name(first_name,last_name,middle_name=''):
    """返回完整的名字"""
    if middle_name:
        full_name=f'{first_name} {middle_name} {last_name}'
    else:
        full_name=f'{first_name} {last_name}'
    return full_name.title()

musician=get_formatted_name('john','hooker','lee')
print(musician)



#任意数量实参

def make_pizza(*toppings):
    """打印客户所有的浇汁"""
    print(toppings)

make_pizza('pepperoni')#香肠
make_pizza('mushrooms','green peppers','extra cheese')


# *topping 创建了一个空元组

def make_pizza1(size,*toppings):
    """概述要制作的披萨"""
    print(f'\nMaking a {size}-inch pizza with the\
follwing toppings:')
    for topping in toppings :
        print(f'-{topping}')

make_pizza1(16,'peperoni')
make_pizza1(12,'mushrooms','green peper','extra cheese')

#字典
def build_profile(first,last,**user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    user_info['first_name']=first
    user_info['last_name']=last
    return user_info
user_profile=build_profile('albert','einstein',
                           location='priceton',
                           field='physics')
print(user_profile)
























