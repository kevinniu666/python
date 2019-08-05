class MyClass(object):
    message="Hellow Class"

    def __init__(self,name="unset",color="White"):
        print("Constructor %s is called with %s" % (name,color))
        self.name="Niubi"
        self.color="Red"

    def __del__(self):
        print ("Destructor is called with %s" % self.name)

    def show(self):
        print(self.message)
        print("here is %s in %s" % (self.name,self.color))


instance1=MyClass("David")
instance1.show()
instance2 = MyClass("Wilson","Black")
instance2.show()

print("Color of instance 2 is %s" % instance2.color)

print("Color of instance 1 is %s" % instance1.color)

# del instance1,instance2