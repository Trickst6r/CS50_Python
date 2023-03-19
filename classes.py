# class Point:
#     def __init__(self, input1, input2):
#         self.x = input1
#         self.y = input2


# p = Point(2, 8)
# print(p.x)
# print(p.y)


class Flight:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        self.passengers.append(name)  # Add new name to the end of the list


flight = Flight(3)
