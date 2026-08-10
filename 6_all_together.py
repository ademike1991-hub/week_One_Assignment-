class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def is_old(self):
        if self.year < 2010:
            return "Old car"
        else:
            return "New car"


cars = [
    Car("Toyota", 2005),
    Car("Tesla", 2022),
    Car("Honda", 1998)
]

for car in cars:
    print("Brand:", car.brand)
    print("Year:", car.year)
    print("Status:", car.is_old())