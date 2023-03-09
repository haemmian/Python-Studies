

class Warehouse:


    parking_slots = []

    def __init__(self, capacity):
        self.capacity = capacity


    def park_car(self, car):
        """
        @brief parks a car in the warehouse
        @param car to park
        """
        Warehouse.parking_slots.append(car)
        print("car parked")

    def get_car(self, index):
        """
        @brief gets the parked car at index
        @param index of the parked car
        @return the car at specified index
        """
        # if Warehouse.parking_slots.count() == 0 and Warehouse.parking_slots[0] is None:
        #     print("error")
        # else:
        return Warehouse.parking_slots.pop(index)

