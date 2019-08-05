class MyClass():
    message="hello world"

    def show(self):
        print(self.message)

    def __init__(self,name="unset",color="black"):
        print("constructor is called with params,",name," ",color)

instance=MyClass("Kevin","White")
instance.show()
instance1=MyClass("Kevin")
instance1.show()
instance2=MyClass()
instance2.show()
instance3=MyClass("Kevin","Liu","Red")

