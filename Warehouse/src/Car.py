

class Car:
    def __init__(self, value: int, capacity: int, engine_power: int, colour: str, vehicle_registration_number: int):
        self.vehicle_registration_number = vehicle_registration_number
        self.colour = colour
        self.engine_power = engine_power
        self.value = value
        self.capacity = capacity

    def __str__(self) -> str:
        return f"Value: {self.value}, Capacity: {self.capacity}, Engine power: {self.engine_power}, colour: {self.colour}, Vehicle ID: {self.vehicle_registration_number}"
