"""This is the Main file"""
from typing import Optional
from car import Car
from car import RaceCar
from warehouse import Warehouse

# Car initialization (value, capacity, engine Power, colour, vehicle ID, (TopSpeed,) Brand)

car_one: Car = Car(value=50000, capacity=5, engine_power=200, colour="black",
                   vehicle_registration_number=445445, brand="BMW")
car_two: Car = Car(value=45000, capacity=5, engine_power=180, colour="turquoise",
                   vehicle_registration_number=987654, brand="Audi")
car_three: RaceCar = RaceCar(value=200000, capacity=2, engine_power=400, colour="red",
                             vehicle_registration_number=111777, top_speed=300, brand="Ferrari")
warehouse: Warehouse = Warehouse(15)

warehouse.park_car(car_one)
warehouse.park_car(car_two)
warehouse.park_car(car_three)

print("Current amount of cars in the warehouse:", warehouse.current_amount_of_cars())

print("max. capacity of Warehouse: ", warehouse.warehouse_capacity())

audi: Optional[Car] = warehouse.get_car(1)

if isinstance(audi, Car):
    print("retrieved Car: ", audi.brand)

print(warehouse.get_all_cars_sorted())
