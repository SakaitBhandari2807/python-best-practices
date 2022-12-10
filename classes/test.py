fruits = ['Kiwi', 'Plum', 'Water Melon', 'Apple', 'Orange']

print(sorted(fruits, key=lambda x: len(x)))


#
#
# .map(lambda x: (len(x), x)).sort


# inp = [10, 2, 4, 11,  6 , 5, 3 ]
#       # [ 0, 1 ,2 ,3, 4, 5, 6]
#
# def merge(list1, list2):
#
#     list3 = []
#     i = 0
#     j = 0
#     while i < len(list1) and j < len(list2):
#         if list1[i] <= list2[j]:
#             list3.append(list1[i])
#             i += 1
#         else:
#             list3.append(list2[j])
#             j += 1
#
#     while j < len(list2):
#             list3.append(list2[j])
#             j += 1
#
#     while i < len(list1):
#             list3.append(list1[i])
#             i += 1
#
#     return list3
#
#
# def sort(inp, low, high):
#
#     if low == high:
#         l = []
#         return l.append(inp[low])
#     else:
#         mid = low + (high - low)//2
#         print(mid, " :" , low, " :", high)
#         list1 = sort(inp, low, mid)
#         list2 = sort(inp, mid + 1, high)
#         list3 = merge(list1, list2)
#     return list3
#
#
# sort(inp, 0, len(inp) - 1)
#
#
# #employee_id, dept_id, salary
#
# #find the third highest salary of each department
#
# select a.dept_id, a.salary from (
# select dept_id, salary, dense_rank() over(partition by dept_id order by salary desc) as rnk
# from emp_table ) a
# where a.rnk = 3;


# class Employee:
#
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname
#
#
# e1 = Employee('A','E')
# e2 = Employee('C', 'A')
#
# l = [ e1, e2]
#
# l2 = sorted(l, key=lambda v1: v1.lastname )
#
# for i in l2:
#     print(i.firstname)

class dataloader:

    def __init__(self):
        print("dataloader ready...")

    def load(self):
        pass

class csv(dataloader):

    def __init__(self):
        print("csvloader ready...")

    def load(self):
        print("loading csv file")


class postgres(dataloader):

    def __init__(self):
        print("postgresloader ready..")

    def load(self):
        print("loading postgres data..")

class tableLoader:

    def __init__(self):
        pass


dl = dataloader()
dl.load()

cl = csv()
cl.load()

