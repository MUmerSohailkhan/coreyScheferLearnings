from functools import wraps
import time


# def startEndDecorator(func):
#     def wrapper():
#         print('i am')
#         func()
#         print('and i am computer programmer')
#     return wrapper
#
#
# @startEndDecorator
# def printName():
#     print('M Umer Sohail Khan')
#
# # printName=startEndDecorator(printName)
# printName()


# def timeit(func):
#     @wraps(func)
#     def timeit_wrapper(*args, **kwargs):
#         start_time = time.perf_counter()
#         result = func(*args, **kwargs)
#         end_time = time.perf_counter()
#         total_time = end_time - start_time
#         print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds and sum is {result}')
#         return result
#     return timeit_wrapper
#
# @timeit
# def calculate_something(num):
#
#     total = sum((x for x in range(0, num**2)))
#
#     return total
#
# calculate_something(10000)


import time



def decFunctions(func):
    def wrapper(num):
        startTime=time.perf_counter()
        resultedSum=func(num)
        endTime=time.perf_counter()
        totalTime=endTime-startTime
        print(f'time taken by {func.__name__} is {totalTime:.4f}s')
    return wrapper



@decFunctions
def calculateSomething(num):
    total=sum(x for x in range(0,num))
    return total


calculateSomething(100000000)





