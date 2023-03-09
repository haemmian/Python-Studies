

class Car:
    def __init__(self, value, capacity, top_speed):
        self.value = value
        self.capacity = capacity
        self.top_speed = top_speed

    def __str__(self):
        return f"Value: {self.value}, Capacity: {self.capacity}, TopSpeed: {self.top_speed}"
