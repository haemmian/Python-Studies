""" This file is the Warehouse Class-file """
from typing import Optional  # used against mypy
from car import Car


class Warehouse:
    """
    The Warehouse class which keeps all the cars
    """
    __slots__ = ["capacity", "parking_slots"]

    def __init__(self, capacity: int):
        self.parking_slots: list[Optional[Car]] = []
        self.capacity = capacity

    def park_car(self, car: Car):
        """
        @brief parks a car in the warehouse
        @param car to park
        """
        self.parking_slots.append(car)
        print("car parked")

    def get_car(self, index: int) -> Optional[Car]:
        """
        @brief gets the parked car at index
        @param index of the parked car
        @return the car at specified index
        """
        if not self.parking_slots:
            print("no Cars are in the warehouse!")
            return None
        print(f"Get car at parking slot {index}")
        tmp_car = self.parking_slots[index]
        # By adding None to this place, the parking slots will not be shifted
        self.parking_slots[index] = None
        return tmp_car

    def current_amount_of_cars(self) -> Optional[int]:
        """
        @brief gets the number of cars in the warehouse
        @return number of cars in the warehouse
        """
        if not self.parking_slots:
            print("no Cars are in the warehouse!")
            return None

        return len(self.parking_slots)

    def warehouse_capacity(self) -> int:
        """
        @brief gets the capacity  in the warehouse
        @return Capacity
        """
        return self.capacity

    def get_all_cars_sorted(self) -> list[Car]:
        """
        @brief gets all cars in a list and sorted by ID
        @return list of cars
        """
        tmp_car_list = [item for item in self.parking_slots if item is not None]
        tmp_car_list.sort(key=lambda x: x.vehicle_registration_number)
        self.parking_slots.clear()
        return tmp_car_list

    def get_all_cars(self) -> list[Car]:
        """
        @brief gets all cars in a list
        @return list of cars
        """
        tmp_car_list = [item for item in self.parking_slots if item is not None]
        self.parking_slots.clear()
        return tmp_car_list
