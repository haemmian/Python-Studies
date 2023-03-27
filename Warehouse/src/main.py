"""This is the Main file"""
from typing import Optional
import car
from warehouse import Warehouse

# Car initialization (value, capacity, engine Power, colour, car ID, Brand, (TopSpeed))

car_one: car.Car = car.Car(50000, 5, 200, "black", 445445, "BMW")
car_two: car.Car = car.Car(5000, 5, 180, "turquoise", 987654, "Audi")
car_three: car.RaceCar = car.RaceCar(200000, 2, 400, "red", 111777, "Ferrari", 300)
warehouse: Warehouse = Warehouse(15)

warehouse.park_car(car_one)
warehouse.park_car(car_two)
warehouse.park_car(car_three)

print("Current amount of cars in the warehouse:", warehouse.current_amount_of_cars())

print("max. capacity of Warehouse: ", warehouse.warehouse_capacity())

audi: Optional[car.Car] = warehouse.get_car(1)

print("Current amount of cars in the warehouse:", warehouse.current_amount_of_cars())

if isinstance(audi, car.Car):
    print("retrieved Car: ", audi.brand)
