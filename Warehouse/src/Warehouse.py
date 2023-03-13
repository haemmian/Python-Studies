from Car import Car


class Warehouse:
    parking_slots: list[Car] = []

    def __init__(self, capacity: int):
        self.capacity = capacity

    def park_car(self, car: Car):
        """
        @brief parks a car in the warehouse
        @param car to park
        """

        Warehouse.parking_slots.append(car)
        print("car parked")

    def get_car(self, index: int) -> Car:
        """
        @brief gets the parked car at index
        @param index of the parked car
        @return the car at specified index
        """
        if Warehouse.parking_slots:
            print(f"Get car at parking slot {index}")
            tmp_car = Warehouse.parking_slots[index]
            Warehouse.parking_slots[index] = 0
            return tmp_car
        else:
            print("no Cars are in the warehouse!")

    def current_amount_of_cars(self):
        """
        @brief gets the number of cars in the warehouse
        @return number of cars in the warehouse
        """
        if Warehouse.parking_slots:
            return len(Warehouse.parking_slots)
        else:
            print("no Cars are in the warehouse!")

    def warehouse_capacity(self) -> int:
        """
        @brief gets the capacity  in the warehouse
        @return Capacity
        """
        return self.capacity

    def get_all_cars_sorted(self) -> list[Car]:
        ls = self.parking_slots.copy()
        ls.sort(key=lambda x: x.vehicle_registration_number)
        self.parking_slots.clear()
        return ls

    def get_all_cars(self) -> list[Car]:
        ls = self.parking_slots.copy()
        self.parking_slots.clear()
        return ls
