class Car:
    """a simple car"""

    def __init__(self, make, model, year):
        """initialize attributes to make a car"""
        self.make = make
        self.model = model
        self.year = year 
        self.odometer_reading = 0  # this sets a default value for an attribute that doesnt need to be passed in on creation

    def get_descriptive_name(self):
        """Return a neat name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.") # we can set a method to alter this value as seen next

    def update_odometer(self, mileage):
        """set the new odometer reading"""
        """stop someone from rolling it BACK"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cant roll back the odometer dummy")

    def increment_odometer(self, miles):
        """adds given amount to mile clock"""
        self.odometer_reading += miles

class ElectricCar(Car):
    """Represents aspects of a car specifically an electric car"""
    def __init__(self, make, model, year):
        """initialize attributes of parent classs"""
        super().__init__(make,  model, year)

mytesla = ElectricCar('tesla', 'model s', '2020')
print(mytesla.get_descriptive_name())