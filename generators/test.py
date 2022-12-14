import random

def fincubes(n):

    for i in range(n):
        yield i**3


for x in fincubes(3):
    print(x)


def rand_num(low, high, n):
    for i in range(n):
        yield random.randint(low, high)

for x in rand_num(1, 10 , 12):
    print(x)

a = 10
b = a

print(a==b)
a = 11
print(a)
print(b)