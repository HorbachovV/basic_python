class Car:
    """This class represents a car object."""
    
    def __init__(self, make, model, year):
        """Constructor method that sets the make, model, and year of the car."""
        self.make = make
        self.model = model
        self.year = year
        
    def start_engine(self):
        """Method that simulates starting the car's engine."""
        print("The engine has been started.")
        
    def stop_engine(self):
        """Method that simulates stopping the car's engine."""
        print("The engine has been stopped.")

my_car = Car("Toyota", "Corolla", 2022)

my_car.start_engine()    # Output: The engine has been started.
my_car.stop_engine()     # Output: The engine has been stopped.


# Class inheritance

class Vehicle:
    """This class represents a vehicle object."""
    
    def __init__(self, make, model, year):
        """Constructor method that sets the make, model, and year of the vehicle."""
        self.make = make
        self.model = model
        self.year = year
        
    def start_engine(self):
        """Method that simulates starting the vehicle's engine."""
        print("The engine has been started.")
        
    def stop_engine(self):
        """Method that simulates stopping the vehicle's engine."""
        print("The engine has been stopped.")


class Car(Vehicle):
    """This class represents a car object, which inherits from the Vehicle class."""
    
    def __init__(self, make, model, year, num_doors):
        """Constructor method that sets the make, model, year, and number of doors of the car."""
        super().__init__(make, model, year)
        self.num_doors = num_doors
        
    def unlock_doors(self):
        """Method that simulates unlocking the car's doors."""
        print("The doors have been unlocked.")
        
    def lock_doors(self):
        """Method that simulates locking the car's doors."""
        print("The doors have been locked.")


class Motorcycle(Vehicle):
    """This class represents a motorcycle object, which inherits from the Vehicle class."""
    
    def __init__(self, make, model, year, num_wheels):
        """Constructor method that sets the make, model, year, and number of wheels of the motorcycle."""
        super().__init__(make, model, year)
        self.num_wheels = num_wheels
        
    def balance(self):
        """Method that simulates balancing the motorcycle."""
        print("The motorcycle is now balanced.")

my_car = Car("Toyota", "Corolla", 2022, 4)
my_motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2022, 2)

my_car.start_engine()     # Output: The engine has been started.
my_car.unlock_doors()     # Output: The doors