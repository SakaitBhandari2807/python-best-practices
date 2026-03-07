class Car:
    def __init__(self, color, cartype, manufacturing_year, manufacturer_name):
        self.color = color
        self.type = cartype
        self.manufacturing_year = manufacturing_year
        self.manufacturer_name = manufacturer_name
    def __str__(self):
        return f"A brand new {self.color} {self.type} from {self.manufacturer_name} is ready in {self.manufacturing_year}"

    def drive(self):
        pass

class Builder:

    def __init__(self):
        self.color = None
        self.cartype = None
        self.manufacturing_year = None
        self.manufacturer_name = None

    def withColor(self, color):
        self.color = color
        return self

    def withType(self, cartype):
        self.cartype = cartype
        return self

    def withManufacturingYear(self, year):
        self.manufacturing_year = year
        return self

    def withManufacturerName(self, name):
        self.manufacturer_name = name
        return self

    def build(self):
        return Car(self.color, self.cartype, self.manufacturing_year, self.manufacturer_name)



honda = Builder()\
    .withColor('Gray')\
    .withType('Sedan')\
    .withManufacturingYear(2023)\
    .withManufacturerName('Honda')\
    .build()

print(honda)