#chapter on classes. Classes are models of objects that have properties
class Person():
    """Describes person"""
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age +10
        self.occupation = occupation

    def description(self):
        print("You, "+self.name.title()+" satisfy the following:")
        print("You are ", self.age)
        print("You work as a " +self.occupation)
        print("You are a first-rate ass.")
class Dog():
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """initializes name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate dog sitting"""
        print(self.name.title() +" is now sitting!")

    def roll_over(self):
        """Simulate rolling over"""
        print(self.name.title() +" is rolling over!")

class Restaurant():
    def __init__(self, name, cuisine, number_served = 0):
        """initializes name and cuisine attributes"""
        self.name = name.title()
        self.cuisine = cuisine
        self.customers_served = number_served

    def business_state(self):
        """informs restaurant is open"""
        print(self.name.title() +" is now open for business!")

    def cuisine_type(self):
        """prints cuisine type"""
        print(self.name.title() +" serves " +self.cuisine +"!")

    def customers_today(self, customers):
        self.customers_served +=customers

    def total_customers(self):
        """prints number of customers served today"""
        print(self.name.title() +" has served " +str(self.customers_served) +"!")

    

class User():
    def __init__(self, first_name ,last_name, age, business = "computer programming"):
        """initializes first and last names of user"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.business = business
        self.login_number = 0

    def new_login(self):
        self.login_number +=1
        print("You have logged in " +str(self.login_number) +" times!")

    def reset_login(self):
        self.login_number = 0
        print("Your have logged in ", self.login_number, " times today!")

    def user_name(self):
        print("Your name is " +self.first_name.title() +" "+self.last_name.title() +"!")

    def user_attributes(self):
        """prints attributes of user"""
        self.user_name()
        print("You are "+str(self.age) +" years old.")
        print("Your work in "+self.business+".")
        print("You are a fool.")

class Car():
    """A simple representation of a car"""
    def __init__(self, make, model, year):
        """initializes car attributes"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def car_name(self):
        """determines car's name"""
        car_long_name = str(self.year) +" " +self.make +" " +self.model
        return car_long_name.title()

    def odometer_total(self):
        """prints odometer reading"""
        print("The "+self.car_name() +" has " +str(self.odometer_reading)+" miles.")

    def update_odometer(self, mileage):
        """
        updates odometer
        rejects change if lower than current value
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Sorry, I can't role the odometer back!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


    
