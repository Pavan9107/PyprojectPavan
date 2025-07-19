"""print("Hello World")"""

class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def mydreamcar(self):
        print("My dream car is",self.brand,self.model)

c=Car('tata','Harrier')
c.mydreamcar()


