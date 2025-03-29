def add_numbers(x, y):
    print('Sum of numbers: ', x + y)

def my_function(*kids):
  print("The youngest child is " + kids[0])

my_function("Emil", "Tobias", "Linus") # The youngest child is Emil

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function() # I am from Norway
my_function("Brazil")

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits) # apple banana cherry

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

def my_function(some_function):
  print('My function')

my_function(add_numbers(5, 5))

def my_function(some_function):
  def my_another_function():
    print('Another function')
   
  print('My function')
  my_another_function() 
my_function(add_numbers(5, 5))

# lambda functions
x = lambda a, x : a + x
print(x(5, 15))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))