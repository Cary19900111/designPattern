from enum import Enum
WHEEL = Enum("WHEEL","TOYO BONES")
WING = Enum("WING","UNLIMITED HOVER")
BODY = Enum("BODY","IRON GORGEOUS")
class AirPlane:
    def __init__(self,name):
        self.name = name
        self.wheel = None
        self.wing = None
        self.body = None
    def __str__(self):
        return "The {} plane contructed by {} {} and {} is taking off ".format(self.name,self.wheel,self.wing,self.body)

class J_10(object):
    def __init__(self):
        self.plane = AirPlane(self.__class__.__name__)
    def add_wheel(self):
        self.plane.wheel= WHEEL.TOYO
    def add_wing(self):
        self.plane.wing = WING.UNLIMITED
    def add_body(self):
        self.plane.body = BODY.IRON
    def contruct(self):
        for step in [self.add_wheel,self.add_wing,self.add_body]:
            step()
    def fly(self):
        print(self.plane)

if __name__ == "__main__":
    j_10 = J_10()
    j_10.contruct()
    j_10.fly()
