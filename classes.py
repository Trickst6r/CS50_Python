# __init__(): hàm khởi tạo () (constructor) của class
# class Point:
#     def __init__(self, input1, input2):
#         self.x = input1
#         self.y = input2


# p = Point(2, 8)
# print(p.x)
# print(p.y)


class Flight:
    # Create a new flight
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        # If no open seats available,
        # return False to indicate there are no open seats
        if not self.open_seats():
            return False
        # .append(): Add new name to the end of the list
        self.passengers.append(name)
        return True

    # Open_seats function to tell how many open seats there are
    def open_seats(self):
        # Open_seat function to return the capacity minus the number of passengers
        return self.capacity - len(self.passengers)


flight = Flight(3)

people = ["Ricardo", "Milos", "Anri", "Hitomi"]
for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seat for that {person}")

# Steps by steps:
# 1. Create a list of 4 people.
# 2. For each of those people, we're going to try and add the passenger,
# to the flight calling flight.add_passenger
