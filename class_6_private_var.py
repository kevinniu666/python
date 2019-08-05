class MyClass(object):
    def __init__(self,name="unset",color="White"):
        print("Constructor is called with params %s,%s" % (name,color))
        self.__name = name
        self.__color = color

    def __del__(self):
        print("Destructor is called for %s" % self.__name)


instance = MyClass("Kevin","Red")
print(instance.__name)
del instance
