class MyClass(object):
    message="Hello Developer"
    def show(self):
        print(self.message)

    def __init__(self):
        print("Constructor is called")
instance = MyClass()
instance.show()