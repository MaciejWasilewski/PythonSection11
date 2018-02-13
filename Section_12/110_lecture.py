class Kettle(object):
    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        if self.on:
            self.on = False
        else:
            self.on = True


kenwood = Kettle("Kenwood", 999.9)
print(kenwood.make, kenwood.price, kenwood.on)

print("Models: {0.make}, {0.price}".format(kenwood))

print(kenwood.on)
kenwood.switch_on()
print(kenwood.on)

Kettle.switch_on(kenwood)
print(kenwood.on)

print(Kettle.power_source)
print(kenwood.power_source)

print(Kettle.__dict__)
print(kenwood.__dict__)
