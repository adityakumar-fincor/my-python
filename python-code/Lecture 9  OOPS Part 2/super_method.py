"""
Super method = super() method is used to access methods of the parents class
"""
 
class car:
    def __init__(self, type):
        self.type = type
    @staticmethod
    def start():
        print("car started..")
    @staticmethod
    def stop():
        print("car stopped")

class toyta(car):
    def __init__(self, name, type):
        super().__init__(type)
        super().start()
        self.brand = name

car1 = toyta("prius", "disel",)
print(car1.type)
