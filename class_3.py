class MyClass(object):
    message="Hello Class"

    def __init__(self, name="unset", color="White"):
        print("Constructor is called with params: ",name," ",color)

    def __del__(self):
        print("Destructor is called")

    def show(self):
        print(self.message)


instance = MyClass("Kevin")

instance.show()
