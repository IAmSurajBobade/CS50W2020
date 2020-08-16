class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(2, 8)

print(p.x)
print(p.y)


class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passangers = []

    def addP(self, name):
        if not self.openSeats():
            return False
        self.passangers.append(name)
        return True

    def openSeats(self):
        return self.capacity - len(self.passangers)


myFlight = Flight(2)
people = ["Suraj", "Bob", "Sunny"]

for person in people:
    success = myFlight.addP(person)

    if (success):
        print(f"We added {person} to flight")
    else:
        print(f"We could not add {person} to flight")

print(myFlight.passangers)
