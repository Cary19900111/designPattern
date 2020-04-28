#FactoryMethod
class WxPay:
    @property
    def pay(self):
        return "go to WxPay"
class AliPay:
    @property
    def pay(self):
        return "go to AliPay"
def PayFactory(paymethod):
    payMode = {"wx":WxPay(),'ali':AliPay()}
    return payMode[paymethod]
def FactoryMethodMain(paymethod):
    product = PayFactory(paymethod)
    print(product.pay)
#AbstractFactory omit Abstract class because of dynamic language
class Children(object):
    def __init__(self,name):
        self.name = name
    def createball(self):
        self.ball = "football"
    def play(self):
        print("play {}".format(self.ball))

class Adult(object):
    def __init__(self,name):
        self.name= name
    def createball(self):
        self.ball = "Adult ball"
    def play(self):
        print("play{}".format(self.ball))

class PlayFactory(object):#虚拟层
    def __init__(self,factory,name):
        self.f = factory(name)
        self.f.createball()
    def play(self):
        self.f.play()
def AbstractFactoryMethodMain(paymethod,name):
    product1= PlayFactory(paymethod,name)
    product1.play()
if __name__=='__main__':
    # FactoryMethodMain("wx")
    AbstractFactoryMethodMain(Adult,"Cary")
    AbstractFactoryMethodMain(Children,"Cary")