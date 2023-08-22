# # def group_by_owners(files):
# #   newdict={}
# #   for x in files:
# #       print(x)
# #       files[x]=[x]
# #       print(files[x])
# #       newdict.update({x,str(files[x])})
# #   print(newdict)
# #
# #     # x=list((files[x]))
# #     # print(x)
# #   # return None
# #
# # if __name__ == "__main__":
# #     files = {
# #         'Input.txt': 'Randy',
# #         'Code.py': 'Stan',
# #         'Output.txt': 'Randy'
# #     }
# #     print(group_by_owners(files))
#
# # class IceCreamMachine:
# #
# #     def __init__(self, ingredients, toppings):
# #         self.ingredients = ingredients
# #         self.toppings = toppings
# #
# #     def scoops(self):
# #         newlist=[]
# #         for x in self.ingredients:
# #             for y in self.toppings:
# #                 print(newlist.append([x,y]))
# #         print(newlist)
# #
# #
# # if __name__ == "__main__":
# #     machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
# #     print(machine.scoops())  # should print: [['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]
#
# # def unique_names(names1, names2):
# #     name3=names1+names2
# #     # print(name3)
# #     uniqueName=set(name3)
# #     # print(uniqueName)
# #     return list(uniqueName)
# #
# # if __name__ == "__main__":
# #     names1 = ["Ava", "Emma", "Olivia"]
# #     names2 = ["Olivia", "Sophia", "Emma"]
# #     print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia
#
# # theList1=['umer',
# #           'L1F1',
# #           27]
# # thetupple1=('0093',
# #             'Umer',
# #             26)
# # theSet1={
# #     "apple",
# #     "banana",
# #     "cherry"
# # }
# # theDict1={'Name':'Umer',
# #           'Rno':'0093',
# #           'age':27,
# #           }
# #
# #
# # theString1='Sohail'
# # # full access
# # print(theString1)
# # # through index
# # print(theString1[2])
# # # patch access
# # print(theString1[0:2])
# # # negative index
# # print(theString1[-1:-3])
# # # accessing value
# # print(theDict1.values())
# # # accessing items
# # print(theDict1.items())
#
#
#
#
# # Through Loop
# # for x in theSet1:
# #     print(x)
#
# # !/bin/python3
#
# import math
# import os
# import random
# import re
# import sys
#
#
# #
# # Complete the 'plusMinus' function below.
# #
# # The function accepts INTEGER_ARRAY arr as parameter.
# #
#
# def plusMinus(arr):
#     # Write your code here
#     totlaElement = len(arr)
#     positve=0
#     negative=0
#     zero=0
#     for x in arr:
#         # print(x)
#         if x>0:
#             positve+=1
#         elif x<0:
#             negative+=1
#         else:
#             zero+=1
#
#     ratioPositive = positve / totlaElement
#     ratioNegative = negative / totlaElement
#     ratioZero=zero/totlaElement
#
#     print('%.6f' % ratioPositive)
#     print('%.6f' % ratioNegative)
#     print('%.6f' % ratioZero)
#
# if __name__ == '__main__':
#     n = int(input().strip())
#
#     arr = list(map(int, input().rstrip().split()))
#
#     plusMinus(arr)
#
# # lst=[2, 3, 2, 2, -3, 1, 4]
# #
# # print(lst.count(3))
# # for x in lst:
# #     if x==3:
# #         print('yes')
#
#
# def reversed_args(f):
#     return f
#
#
# int_func_map = {
#     'pow': pow,
#     'cmp': lambda a, b: 0 if a == b else [1, -1][a < b],
# }
#
# string_func_map = {
#     'join_with': lambda separator, *args: separator.join(args),
#     'capitalize_first_and_join': lambda first, *args: ''.join([first.upper()] + list(args)),
# }
#
# queries = int(input())
# for _ in range(queries):
#     line = input().split()
#     func_name, args = line[0], line[1:]
#     if func_name in int_func_map:
#         args = list(map(int, args))
#         print(reversed_args(int_func_map[func_name])(*args))
#     else:
#         print(reversed_args(string_func_map[func_name])(*args))


a=[]
a+=[3]
print(a)
# a.append(22)
# print(a)
# o='cdcdcd'
# a+=o
# print(a)
# a.append(o)
# print(a)
# a+=33
# print(a)