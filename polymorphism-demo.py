class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("Driving")

class Boat:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("Sail")

class Plane:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("Fly")

carobj=Car("Tata","Indica")
boatobj=Boat("Indian","Chetak")
planeobj=Plane("King","Fisher")

for i in (carobj,boatobj,planeobj):
    i.move()