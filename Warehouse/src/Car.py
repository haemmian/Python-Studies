

class Car:
    def __init__(self, value: int, capacity: int, top_speed: int):
        self.value = value
        self.capacity = capacity
        self.top_speed = top_speed

    def __str__(self) -> str:
        return f"Value: {self.value}, Capacity: {self.capacity}, TopSpeed: {self.top_speed}"
