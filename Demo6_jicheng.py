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

class ElectricCar(Car):
    """电动车"""
    def __init__(self,make,model,year):
        """初始化父类"""
        super().__init__(make,model,year)
        self.battery_size=75

    def descripe_battery(self):
        print(f'The car has {self.battery_size}-KWh')
        

my_tesla=ElectricCar('tesla','models','2019')
print(my_tesla.get_descriptive_name())
my_tesla.descripe_battery()
