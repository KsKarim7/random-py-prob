# 2. Assume, you have been given a dictionary named dict_1. The values of the dictionary will be a list or a tuple depending
# on the case of the dictionary key.
# If the key is in lower case, then the value will be in list format.
# If the key is in upper case, then the value will be in tuple format.
# Now, write a Python program that creates a new dictionary named “dict_primes” that contains only the prime numbers in the
# value. Then, finally, print the dictionary dict_primes.

# dict_1 = {"a": [5, 2, 55, 17], "P": (
#     11, 121, 222), "B": (37, 53, 71), "c": [45, 92, 50]}


# dict_primes = {}
# lst = []
# for k, v in dict_1.items():
#     if (ord(k) >= 65 and ord(k) <= 90):
#         for i in v:
#             for j in range(2, i):
#                 if (i % j == 0):
#                     pass
#                 else:
#                     lst.append(v)


# print(lst)

#     else:
#         dict_primes[i] = dict_1[i]

# for k, v in dict_primes:
#     for i in v:
#         for j in range(2, i):
#             if (i % j == 0):
