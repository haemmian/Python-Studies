""" This file is the Car-class file """
from dataclasses import dataclass


@dataclass
class Car:
    """
    Class of Car
    """

    def __init__(self, value: int, capacity: int, engine_power: int, colour: str,  # pylint: disable=too-many-arguments
                 vehicle_registration_number: int, brand: str):
        self.brand = brand
        self.vehicle_registration_number = vehicle_registration_number
        self.colour = colour
        self.engine_power = engine_power
        self.value = value
        self.capacity = capacity

    def __str__(self) -> str:
        return f"Value: {self.value}, Capacity: {self.capacity}, Engine power: " \
               f"{self.engine_power}, colour: {self.colour}, Vehicle ID: " \
               f"{self.vehicle_registration_number}, \t Brand: {self.brand}"


@dataclass
class RaceCar(Car):
    """
    Class of Race-Car
    """

    def __init__(self, value: int, capacity: int, engine_power: int, colour: str,  # pylint: disable=too-many-arguments
                 vehicle_registration_number: int, brand: str, top_speed: int):
        self.top_speed = top_speed

        super().__init__(value=value, capacity=capacity, engine_power=engine_power,
                         colour=colour, vehicle_registration_number=vehicle_registration_number,
                         brand=brand)

    def __str__(self) -> str:
        return f"Value: {self.value}, Capacity: {self.capacity}, Engine power: " \
               f"{self.engine_power}, colour: {self.colour}, Vehicle ID: " \
               f"{self.vehicle_registration_number}, \t Brand: {self.brand}" \
               f", Top speed: {self.top_speed}"
