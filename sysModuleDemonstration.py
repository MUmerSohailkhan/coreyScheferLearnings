# import sys
#
#
# #sys.stdin
# for line in sys.stdin:
#   if 'q' == line.rstrip():
#     break
#   print(f'Input : {line}')
#
# print("Exit")
#
# #sys.stdout
# sys.stdout.write('Geeks')
#
#
#
# #sys.argv
# n = len(sys.argv)
# print("Total arguments passed:", n)
#
# # Arguments passed
# print("\nName of Python script:", sys.argv[0])
#
# print("\nArguments passed:", end=" ")
# for i in range(1, n):
#   print(sys.argv[i], end=" ")
#
# # Addition of numbers
# Sum = 0
#
# for i in range(1, n):
#   Sum += int(sys.argv[i])
#
# print("\n\nResult:", Sum)

import os
print(os.environ.get('mygmail'))