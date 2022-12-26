# 2.We all know that the additive primaries are red, green, and blue. Now, write a Python program that will take a color sequence as a
# string from the user where R represents Red, G represents Green and B represents Blue. The program should print the choice of
# colors that is actually a tuple containing the sub-tuples as (color_name, color_frequency) only if the color_frequency for that color is
# at least one in the given color sequence. [You are not allowed to use count() function here.]
# Sample Input1:
# "RGBRRGBBR"
# Sample Output1:
# (('Red', 4), ('Green', 2), ('Blue', 3))

def rgb(str):
    R = 0
    G = 0
    B = 0
    rgb = ()
    for i in str:
        if ("R" == i):
            R += 1
        if ("G" == i):
            G += 1
        if ("B" == i):
            B += 1
            # tup = tuple('Red')
            # print(tup)

    # print(R, G, B)
    if (R > 1):
        red = ('Red', R)
        # print(red)
    if (G > 1):
        green = ('Green', G)
        # print(green)
    if (B > 1):
        blue = ('Blue', B)
        # print(blue)

    if (R > 1):
        rgb += (red,)
        # print((red), end='')
    if (G > 1):
        rgb += (green,)
        # print((green), end='')

    if (B > 1):
        rgb += (blue,)
        # print((blue), end='')

    # rgb = (red, green, blue)
    print(rgb)


rgb("RBRRBBR")
