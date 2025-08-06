class Dog:
    """一次模拟小狗的简单尝试"""
    def __init__(self,name,age):
        """初始化name和age"""
        self.name=name
        self.age=age

    def sit(self):
        """模拟小狗收到命令时蹲下"""
        print(f'{self.name} is now sitting')

    def roll_over(self):
        """模拟小狗收到命令时打滚"""
        print(f'{sefl.name} rolled over!')


#   __init__() 特殊的方法

my_dog=Dog('willie',6)
you_dog=Dog('lucy',3)

print(f'my dog name is {my_dog.name},')
print(f'{my_dog.name} is {my_dog.age} years old')
my_dog.sit()

print(f'you dog name is {you_dog.name}')
print(f'{you_dog.name} is {you_dog.age} years old')
you_dog.sit()


      
