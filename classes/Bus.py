class TwilightBus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, person):
        self.passengers.append(person)

    def drop(self, person):
        self.passengers.remove(person)


class Bus:
    def __init__(self, passengers=None):
        if passengers is None:
            passengers = []
        self.passengers = passengers

    def pick(self, person):
        self.passengers.append(person)

    def drop(self, person):
        self.passengers.remove(person)


b1 = Bus(['Alice', 'Jack', 'David'])
b1.pick('Laura')
print(b1.passengers)

b1.drop('Alice')
print(b1.passengers)

b2 = Bus()
print(id(b2.passengers))
print(b2.passengers)

b3 = Bus()
b3.pick('Harry')
print(id(b3.passengers))
print(b3.passengers)
print(b2.passengers)

print(id(b1), id(b2), id(b3))


volleyball_team = ['Sue', 'Tina', 'Maya','Diana','Pat']
bus = TwilightBus(volleyball_team)
bus.drop('Tina')
bus.drop('Pat')

print(volleyball_team)

