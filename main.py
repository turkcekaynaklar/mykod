#Single or Double Quotes?  String variables can be declared either by using single or double quotes:
s = "ÇiftTırnak"
# is the same as
t = 'tektırnak'
print(s)
print(t)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))
a = 4
A = "Sally"

print(a)
print(A)
"""Variable Names 
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables) variable değişken """
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

x, y, z = "1", "2", "Cherry"

print(x)
print(y)
print(z)
m =  x + y
print(m)
print(x+y)
x, y, z = 1, 2, "Cherry"
print(x+y)

def myfunc():
  print("Python is " + z)

myfunc()
