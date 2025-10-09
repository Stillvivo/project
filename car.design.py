class car:
    def __init__(self, nameofcar, colorofcar):
        self.name = nameofcar
        self.color = colorofcar
        if nameofcar is str:
            print(f"{nameofcar} is not a car")

        if colorofcar is str:
            print(f"{colorofcar} is not a color of car")

    @classmethod
    def ring_size(self, ring_size):
        self.ring_size = ring_size


car = car(input("enter your car name : "), input("enter your color of car name :"))
ring_size = car.ring_size(input("enter your size of ring : "))
print(f"name car is : {car.name} and color car is : {car.color} and size of ring is : {car.ring_size}")
