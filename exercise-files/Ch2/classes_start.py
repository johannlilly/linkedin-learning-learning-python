#
# Example file for working with classes
#

class myClass():
    # usually, the first argument to any method of a class is the `self` argument
    # `self` refers to the object itself -- the particular instance of the object
    def method1(self):
        print("myClass method1")
    
    def method2(self, someString):
        print("myClass method2 " + someString)

# anotherClass is based on myClass
class anotherClass(myClass):
    # overrides method in base class
    def method1(self):
        # call inherited method on super class from inside
        myClass.method1(self)
        print("anotherClass method1")
    
    # overrides method in base class
    def method2(self, someString):
        print("anotherClass method2 ")

def main():
    # instantiate object instance of class
    c = myClass()
    c.method1()
    c.method2("This is a string")

    # c2 is an instance of anotherClass
    c2=anotherClass()
    c2.method1()
    c2.method2("This is a string")

if __name__ == "__main__":
    main()
