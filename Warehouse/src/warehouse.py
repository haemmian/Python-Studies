""" This file is the Warehouse Class-file """
from typing import Optional
from car import Car


class Warehouse:
    """
    The Warehouse class which keeps all the cars
    """
    __slots__ = ["_capacity", "_parking_slots", "_current_amount_of_cars"]

    def __init__(self, capacity: int):
        self._parking_slots: list[Optional[Car]] = []
        self._capacity = capacity
        self._current_amount_of_cars = 0

    def park_car(self, car: Car):
        """
        @brief parks a car in the warehouse
        @param car to park
        """
        self._parking_slots.append(car)
        self._current_amount_of_cars += 1
        print("car parked")

    def get_car(self, index: int) -> Optional[Car]:
        """
        @brief gets the parked car at index
        @param index of the parked car
        @return the car at specified index
        """
        if not self._parking_slots:
            print("no Cars are in the warehouse!")
            return None

        if type(self._parking_slots[index]) is None:
            print(f"There is no Car at parking slot {index}")
            return None

        print(f"Get car at parking slot {index}")
        tmp_car = self._parking_slots[index]

        # By adding None to this index, the parking slots will not be shifted
        self._parking_slots[index] = None
        self._current_amount_of_cars -= 1
        return tmp_car

    def current_amount_of_cars(self) -> Optional[int]:
        """
        @brief gets the number of cars in the warehouse
        @return number of cars in the warehouse
        """
        if not self._current_amount_of_cars:
            print("no Cars are in the warehouse!")
            return 0

        return self._current_amount_of_cars

    def warehouse_capacity(self) -> int:
        """
        @brief gets the capacity  in the warehouse
        @return Capacity
        """
        return self._capacity

    def get_all_cars_sorted(self) -> list[Car]:
        """
        @brief gets all cars in a list and sorted by ID
        @return list of cars
        """
        tmp_car_list = [item for item in self._parking_slots if item is not None]
        tmp_car_list.sort(key=lambda x: x.vehicle_registration_number())
        self._parking_slots.clear()
        self._current_amount_of_cars = 0
        return tmp_car_list

    def get_all_cars(self) -> list[Car]:
        """
        @brief gets all cars in a list
        @return list of cars
        """
        tmp_car_list = [item for item in self._parking_slots if item is not None]
        self._parking_slots.clear()
        self._current_amount_of_cars = 0
        return tmp_car_list
