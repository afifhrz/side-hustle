class Animals():
    def __init__(self, leg, bulu, tipe):
        self.leg = leg
        self.bulu = bulu
        self.tipe = tipe

Dog = Animals(4, "Lembut", "Mamalia")

print(id(Dog.leg))
print(id(Dog.bulu))
print(id(Dog))