# pizza1 = PizzaMachine()
# order1 = pizza1.customizePizza(["Cheese", "Pepperoni"],
# "Hot")
# print("1################################# ")
# print(order1)
# print("2================================")
# pizza2 = PizzaMachine("Vege")
# order2 = pizza2.customizePizza("Super Naga")
# print("3#################################")
# print(order2)
# print("4================================")
# pizza3 = PizzaMachine("Chicken Blast",12)
# order3 = pizza3.customizePizza(["Mushroom"])
# print("5#################################")
# print(order3)
# print("6================================")
# pizza4 = PizzaMachine("Beef Bonanza",16)
# order4 = pizza4.customizePizza(["Cheese","Beef kala
# bhuna"],"Mild")
# print("7#################################")
# print(order4)
# print("8================================")


# 1#################################
# Your 6-inch Hot spicy Regular Pizza is ready with
# Cheese,Pepperoni toppings. Enjoy!
# 2================================
# 3#################################
# No toppings specified! Can't bake pizza.
# 4================================
# 5#################################
# Your 12-inch Regular spicy Chicken Blast Pizza is ready
# with Mushroom toppings. Enjoy!
# 6================================
# 7#################################
# Sorry! Spice level not allowed. Can't bake pizza.
# 8================================

class PizzaMachine:
    def __init__(self, type=None, size=None):
        self.type = type
        self.size = size
        self.temp = ['Hot', 'Regular', 'Super Naga']

    def customizePizza(self, *pizza):
        if (len(pizza) == 1):
            print("No toppings specified! Can't bake pizza.")
        elif (self.type == None and self.size == None):
            if (pizza[1] in self.temp):
                print(f'Your 6-inch Hot spicy Regular Pizza is ready with
                      {str(pizza[0])[1:-1]} Enjoy!')
            else:
                print("Sorry! Spice level not allowed. Can't bake pizza.")
