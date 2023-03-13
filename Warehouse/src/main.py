from Car import Car
from Car import Race_Car
from Warehouse import Warehouse

# Car initialization (value, capacity, engine Power, colour, vehicle ID)

car_one: Car = Car(value=50000, capacity=5, engine_power=200, colour="black", vehicle_registration_number=445445, brand="BMW")
car_two: Car = Car(value=45000, capacity=5, engine_power=180, colour="turquoise", vehicle_registration_number=987654, brand="Audi")
car_three: Race_Car = Race_Car(value=200000, capacity=2, engine_power=400, colour="red", vehicle_registration_number=111777, top_speed=300, brand="Ferrari")
warehouse: Warehouse = Warehouse(15)

warehouse.park_car(car_one)
warehouse.park_car(car_two)
warehouse.park_car(car_three)

print("Current amount of cars in the warehouse:", warehouse.current_amount_of_cars())

print("max. capacity of Warehouse: ", warehouse.warehouse_capacity())

audi = warehouse.get_car(1)

print("retrieved Car: ", audi.brand)
