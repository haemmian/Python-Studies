from Car import Car
from Warehouse import Warehouse

# Car initialization (value, capacity, engine Power, colour, vehicle ID)

car_one: Car = Car(value=150, capacity=4, engine_power=123, colour="blue", vehicle_registration_number=1234)
car_two: Car = Car(133, 3, 443, "red", 9876)
print(str(car_one))
print(str(car_two))

warehouse: Warehouse = Warehouse(15)

warehouse.park_car(car_one)
warehouse.park_car(car_two)

print("Current amount of cars in the warehouse:", warehouse.current_amount_of_cars())
returned_car: Car = warehouse.get_car(1)

print(warehouse.warehouse_capacity())
print(str(returned_car))
