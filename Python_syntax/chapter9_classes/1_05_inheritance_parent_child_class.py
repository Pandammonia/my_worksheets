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

# if you are adding too much information to a class (example a battery in an electric car might have a lot of attributes)
# such as charge, charge time, amps, watts, etc. Make a seperate class to hold these details like so

class Battery():
    """The model for a battery for an electric car"""
    def __init__(self, batterysize = 75):
        """Initilize the battery attirbutes"""
        self.batterysize = batterysize

    def describebattery(self):
        """Statement about battery"""
        print(f"This car has a {self.batterysize}-kWh battery.") 

    def get_range(self):
        """Print statement about batterys charge"""
        if self.batterysize == 75:
            range = 260
        elif self.batterysize == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car): #include parent class name here
    """Represents aspects of a car specifically an electric car"""
    def __init__(self, make, model, year):
        """initialize attributes of parent classs"""
        super().__init__(make,  model, year)
        self.battery = Battery()

    def fill_gas_tank(self): #if the parent class has an imcompatible method then name it the same in the childs class
        print("Electric cars dont have a gas tank!")

mytesla = ElectricCar('tesla', 'model s', '2020')
mytesla.battery.describebattery() #look at instance "mytesla" find "battery" attribute and call method "describe battery"
mytesla.battery.get_range()