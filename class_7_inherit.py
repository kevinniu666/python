class Base(object):
    def __init__(self):
        print("Constructor of Base Class is called")

    def __del__(self):
        print("Destructor of Base Class is called")

    def move(self):
        print("mov is called in Base Class")
class SubA(Base):
    def __init__(self):
        print("Constructor of SubA is called")


    def move(self):
        print("mov in SubA is called")

class SubB(Base):
    def __del__(self):
        print("Destructor in SubB is called")
        super(SubB,self).__del__()


instA=SubA()
instA.move()
del instA
print("-------------------")
instB=SubB()
instB.move()
del instB
