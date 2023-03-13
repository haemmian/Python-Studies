from Car import Car
from Car import Race_Car
from Warehouse import Warehouse

# Car initialization (value, capacity, engine Power, colour, vehicle ID)

car_one: Car = Car(value=150, capacity=4, engine_power=123, colour="blue", vehicle_registration_number=1234)
car_two: Car = Car(133, 3, 443, "red", 1)
car_three: Race_Car = Race_Car(value=2000, capacity=2, engine_power=500, colour="red", vehicle_registration_number=997, top_speed=250)
warehouse: Warehouse = Warehouse(15)

warehouse.park_car(car_one)
warehouse.park_car(car_two)
warehouse.park_car(car_three)

print("Current amount of cars in the warehouse:", warehouse.current_amount_of_cars())

print("max. capacity of Warehouse: ", warehouse.warehouse_capacity())

all_Cars = warehouse.get_all_cars_sorted()

for car in all_Cars:
    print(car)
