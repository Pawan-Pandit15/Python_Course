# Poly - many - Object-oriented programming (OOP)
# Morphism - Form

# Method overloading
# Method overriding

#---------Method Overloading ------------

''' Method Overloading is not supported in python because python is a
      interpreted language python work line by line.'''

class Mo:
    def myfunction(self):
        print("function with no argument")

    def myfunction(self,a):
        print("function with 1 argument")

    def myfunction(self,a,b):
        print("function with 2 argument")

obj=Mo()
obj.myfunction(10,20)

'''here when i call function with no argument and 1 argument show error because 
    pyhton is a interpreter language call line by line that's why 
     overloading not support in python'''


