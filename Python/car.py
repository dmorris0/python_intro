''' Example class illustrating inheritance '''

class Car:
    
    n_wheels = 4
    
    def __init__(self, make):
        self.make = make
    
    def __str__(self):
        return f'{self.make} with {self.n_wheels} wheels'
    
    def my_needs(self):
        print('I need a tank of fuel')

class ElectricCar(Car):

    def my_needs(self):
        print(f'I need a {self.make} supercharger')


if __name__=="__main__":

    car1 = Car('Ford')
    print(car1)
    car1.my_needs()

    car2 = ElectricCar('Tesla')
    print(car2)
    car2.my_needs()
    isinstance(car2,'Car')
    isinstance(car2,'ElectricCar')
    isinstance(car1,'ElectricCar')

