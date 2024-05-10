# Question 1:

List = [10,501,22,37,100,999,87,351]

class Cirlce:
    # Constructor

    def __init(self):
        self.num = [10,501,22,37,100,999,87,351]
    # Method
    def read_number(self):
        print(self.num)

    # Create object

object = Cirlce()
object.read_number()



# Question 2:

# create a class private variable named pi=3.141
class myClass:
    a = 33
    def __privMeth(self):
         print("I'm inside class myClass")
    def hello(self):
        print("Private Variable value: ",myClass.a)
obj = myClass()
obj.hello()
obj.a


# Question 3:

# From the given List create two class Methods Area and Perimeter which will be going to calculate the Area and Perimeter

class circle:
    
    # Constructor
    def __init__(self,r):
        self.radius = r
    # 
    def area(self):
        self.radius**3.14

    def perimeter(self):
        self.radius*2*3.14

NewCircle = circle(5)
print(NewCircle.area)
print(NewCircle.perimeter)







    



