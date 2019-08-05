class MyClass(object):

    message="Hello Class"

    def show(self):
        print(self.message)
        print("Here is %s in %s!" % (self.name,self.color))

    @staticmethod
    def printMessage():
        print("printMessage is called")
        print(MyClass.message)

    @classmethod
    def createObj(cls,name,color):
        print("Object will be created: %s(%s,%s)" % (cls.__name__, name, color))
        return cls(name,color)

    def __init__(self,name="unset",color="Black"):
        print("Constructor is called with params:", name, " ", color)
        self.name = "Kevin"
        self.color = "Red"

    def __del__(self):
        print("Destructor is called with",self.name)


MyClass.printMessage()

inst = MyClass.createObj("Toby","Green")

print(inst.message)
