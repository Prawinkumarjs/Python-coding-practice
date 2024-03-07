from Car import Car

car_1 = Car("Chevy", "Corvette", 2021, "blue")
car_2 = Car("Ford", "Mustang", 2021, "blue")

car_1.wheel = 12

Car.wheel = 2

print(car_1.wheel)
print(car_2.wheel)

