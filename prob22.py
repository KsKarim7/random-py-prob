# practice prob 09
class Fruit:
    Total_order = 0

    def __init__(self, Order_ID, weight):
        self.Order_ID = Order_ID
        self.weight = weight
        Fruit.Total_order = Fruit.Total_order+1

    def __str__(self):
        return self.Order_ID+", Weight: "+str(self.weight)


class Mango(Fruit):
    # write your code here
    def __init__(self, id, weight, typ, uPrice):
        super().__init__(id, weight)
        self.typ = typ
        self.uPrice = uPrice
        self.tPrice = self.weight * uPrice

    def __str__(self):
        return f'{self.Order_ID}, Weight: {self.weight}, Variety: {self.typ}, Total Price: {self.tPrice}'


class JackFruit(Fruit):
    # write your code here
    def __init__(self, id, weight, uPrice):
        super().__init__(id, weight)
        self.uPrice = uPrice
        self.tPrice = self.weight * uPrice

    def __str__(self):
        return f'{self.Order_ID}, Weight: {self.weight}, Total Price: {self.tPrice}'


m1 = Mango("Order Id 1", 5, "GopalVog", 250)
print(m1)
m2 = Mango("Order Id 2", 5, "HariVanga", 230)
print(m2)
j1 = JackFruit("Order Id 3", 5, 250)
print(j1)
j2 = JackFruit("Order Id 4", 4, 210)
print(j2)
print("Total number of Orders: "+str(Fruit.Total_order))
print("==================")
print(m1+m2)
print("==================")
print(j1+j2)
