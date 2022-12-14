import datetime
import random

mytime = datetime.time(2, 20)

today = datetime.date.today()
print(type(today))

print(mytime)
print(mytime.minute)
print(mytime.hour)

#datetime

mydttm = datetime.datetime(2022, 12, 11, 11, 56, 1)
print(type(mydttm))

#current date is
print(type(datetime.datetime.today()))
print(datetime.datetime.today())

## data object

d1 = datetime.date(2020, 12, 11)
print(type(d1))
print(d1)

d2 = datetime.date(2022, 12, 11)
d3 = d2 - d1
print(type(d3))
print(d3)

print(round(6.6))
print(round(5.5))
print(round(4.5))
print(round(3.4))


# random.seed(101)
# print(random.randint(0, 100))

mylist = list(range(0,100))

print(random.choice(mylist))
print(random.choices(mylist, 10))

print(random.sample(mylist, k = 10))
print(random.uniform(0, 100))






