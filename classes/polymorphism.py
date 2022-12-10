class Animal:

    def __init__(self, name):
        print("Animal created..")
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")


class Dog(Animal):
    def __init__(self, name):
        print("Dog created..")
        self.name = name

    def speak(self):
        return self.name + ' says woof!'


class Cat(Animal):
    def __init__(self, name):
        print("Cat created..")
        self.name = name

    def speak(self):
        return self.name + ' says meow!'


niko = Dog('niko')
niko.speak()

felix = Cat('felix')
felix.speak()

# print(niko.speak())
# print(felix.speak())


# def pet_speak(pet):
#     print(pet.speak())
#
#
# for pet in [niko, felix]:
#     pet_speak(pet)

