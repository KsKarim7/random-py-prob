# Write a python code of a program that reads the values for the three sides x, y, and z of a triangle, and then calculates its area. The area is calculated as follows:

# from math import sqrt

# x = int(input())
# y = int(input())
# z = int(input())


# s = x+y+z
# s /= 2
# x = s - x
# y = s - y
# z = s - z
# ans = s * sqrt(x*y*z)
# print(ans)

# 1. Write a function in Python that will take a string text as input from the user and returns the list of
# unique characters concatenated with their ASCII value at the front and back side.


# inp = input()


# def asci(inp):
#     strr = ''
#     lst = []
#     for i in inp:
#         if (i not in strr):
#             strr += i
#         else:
#             pass
#     for i in strr:
#         lst.append(str(ord(i))+i+str(ord(i)))
#     print(lst)


# asci(inp)


# 2. Write a function in Python that will take a string text as input from the user and returns a dictionary
# having the unique characters as the keys and the list of their both-way indexes (positive and negative
# index) as the values.


def func(inp):
    dictt = {}
    for i in range(len(inp)):
        dictt[inp[i]] = [i].append(10)

        # for j in range(len(inp), 0, -1):
        #     dictt[inp[i]] = j

        print(dictt)


func('pythonBook')
