class Car:
    """模拟汽车"""
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        long_name=f'{self.year} {self.make} {self.model}'
        return long_name.title()

    def update_odometer(self,mileage):
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self,miles):
        self.odometer_reading+=miles

class Battery:
    """电动车电池"""
    def __init__(self,battery_size=75):
        """初始化电瓶"""
        self.battery_size=battery_size

    def describe_battery(self):
        """打印电池信息"""
        print(f'The car has {self.battery_size}-KWh')


class ElectricCar(Car):
    """电动车"""
    def __init__(self,make,model,year):
        """初始化父类"""
        super().__init__(make,model,year)
        self.battery=Battery()

        

my_tesla=ElectricCar('tesla','models','2019')
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()










