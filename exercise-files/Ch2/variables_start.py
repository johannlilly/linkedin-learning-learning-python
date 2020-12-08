# 
# Example file for variables
#

# Declare a variable and initialize it
f=0
print(f)


# re-declaring the variable works
f="abc"
print(f)


# ERROR: variables of different types cannot be combined
# python is a strongly-typed language, even though you don't have to declare the variable type before you use it
# type is inferred
print("this is a string" + str(123))


# Global vs. local variables in functions
def someFunction():
  f="def"
  print(f)

someFunction() # >>> def
print(f) # >>> abc

def someFunction():
  global f
  f="def"
  print(f)

someFunction() # >>> def
print(f) # >>> def

del f # delete definition of variable previously declared
print(f) # >>> "NameError: name 'f' is not defined"

