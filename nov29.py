# task16
lst = []
counter = 0

inp = input().split(', ')


for i in inp:
    lst.append(int(i))
print(f'My list: {lst}')
max = lst[0]


for i in lst:
    if (i > max):
        max = i
        counter += 1
lst.pop(counter)
maxx = lst[0]
counter = 0
for i in lst:
    if (i > maxx):
        maxx = i
        counter += 1
print(
    f'Second largest number in the list is {maxx} which was found at index {counter}')
# print(counter)
