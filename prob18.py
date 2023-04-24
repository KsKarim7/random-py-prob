# practice prob 5
class Smartphone:
    def __init__(self, name=None):
        self.name = name
        self.feature = {}
        # self.type = ''

    def addFeature(self, feature, typ):
        # self.feature = feature
        # self.type = typ
        if (self.name == None):
            print("Feature can not be added without phone name")
        else:
            if (feature not in self.feature):
                self.feature[feature] = typ
            else:
                self.feature[feature] += ', ' + typ

    def setName(self, name):
        self.name = name

    def printDetail(self):
        print(f'Phone Name: {self.name}')
        for k, v in self.feature.items():
            print(f'{k}: {v}')


s1 = Smartphone()
print("=================================")
s1.addFeature("Display", "6.1 inch")
print("=================================")
s1.setName("Samsung Note 20")
s1.addFeature("Display", "6.1 inch")
s1.printDetail()
print("=================================")
s2 = Smartphone("Iphone 12 Pro")
s2.addFeature("Display", "6.2 inch")
s2.addFeature("Ram", "6 GB")
print("== == == == == == == == == == == == == == == ===")
s2.printDetail()
s2.addFeature("Display", "Amoled panel")
s2.addFeature("Ram", "DDR5")
print("=================================")
s2.printDetail()
print("=================================")
