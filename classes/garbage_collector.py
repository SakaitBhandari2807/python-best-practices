import weakref


def bye():
    print("...deleting the object")

s1 = {1,2,3}

print(type(s1))

s2 = s1

ender = weakref.finalize(s1, bye)

print(ender.alive)

del s1
print(ender.alive)

s2 = "spam"
print(ender.alive)

t1 = (1,2,3)
t2=tuple(t1)

print(t2 == t1)
print(t2 is t1)

t3 = t1[:]
print(t3 is t1)

print(id(t1), id(t2), id(t3))


l1 = [1,2,3]
l2=list(l1)

print(l1 == l2)
print(l2 is l1)
print(id(l1), id(l2))

t11 = (1,2,3)
t12 = (1,2,3)

print(t11 ==  t12)
print(t12 is t11)

s1='ABC'
s2='ABC'
print(s1==s2)
print(s1 is s2)
