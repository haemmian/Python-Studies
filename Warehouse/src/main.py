from Car import Car
from Warehouse import Warehouse

# Car initialization (value, capacity, topspeed)

car_one = Car(value=150, capacity=4, top_speed=180)
car_two = Car(133, 3, 240)
print(str(car_one))

warehouse = Warehouse(15)

warehouse.park_car(car_one)
warehouse.park_car(car_two)

returned_car = warehouse.get_car(1)

print(str(returned_car))
