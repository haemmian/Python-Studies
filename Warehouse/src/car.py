""" This file is the Car-class file """
from dataclasses import dataclass


@dataclass
class Car:
    """
    Class of Car
    """
    __slots__ = ["_brand", "_vehicle_registration_number", "_colour", "_engine_power",
                 "_value", "_capacity"]
    # pylint: disable=too-many-arguments
    _value: int
    _capacity: int
    _engine_power: int
    _colour: str
    _vehicle_registration_number: int
    _brand: str

    def __str__(self) -> str:
        return f"Value: {self._value}, Capacity: {self._capacity}, Engine power: " \
               f"{self._engine_power}, colour: {self._colour}, Vehicle ID: " \
               f"{self._vehicle_registration_number}, \t Brand: {self._brand}"

    @property
    def brand(self) -> str:
        """
        Returns the brand
        """
        return self._brand

    @property
    def vehicle_registration_number(self) -> int:
        """
        Returns the Registration Number
        """
        return self._vehicle_registration_number


@dataclass
class RaceCar(Car):
    """
    Class of Race-Car
    """
    __slots__ = ["_brand", "_vehicle_registration_number", "_colour", "_engine_power",
                 "_value", "_capacity", "_top_speed"]
    # pylint: disable=too-many-arguments
    _value: int
    _capacity: int
    _engine_power: int
    _colour: str
    _vehicle_registration_number: int
    _brand: str
    _top_speed: int

    def __post_init__(self):

        super().__init__(self._value, self._capacity, self._engine_power,
                         self._colour, self._vehicle_registration_number,
                         self._brand)

    def __str__(self) -> str:
        return f"Value: {self._value}, Capacity: {self._capacity}, Engine power: " \
               f"{self._engine_power}, colour: {self._colour}, Vehicle ID: " \
               f"{self._vehicle_registration_number}, \t Brand: {self._brand}" \
               f", Top speed: {self._top_speed}"
