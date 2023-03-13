# mutable - cannot change the value of variable 
# immutable - cannot change the value of variable
# str is  immutable
x, y, z = "Orange", "Banana", "Cherry"
a = 10
b = 20


print(a + b) #30
print(a - b) #-10
print(a * b) #200
print(b // a) #2
print(b % a)  #0
print(a**b) #100000000000000000000

#concatination
print(True + 5)  #6
print(False + 5) #5
print(type ('5' + '10')) #<class 'str'>

#f string
name, age, salary = 'John', 50, 25000
print(f"My name is {name}, my age is {age}, and i have such salary {salary}")
      
#input
num1 = input('Enter first number')
num2 = input('Enter second number')
print(type(num1)) #str


number1 = 100
number2 = 10.25
print(type(number1)) #int
print(type(number2)) #float

print(max(10, 20, 30))
print(min(10, 20, 30))

str1 = 'Welcome'
print(len(str1))
print(type(str1)) #str
name1 = str()
print(type(name1))
name2 = ''
print(type(name2))

#slicing []
str5 = 'welcome'
print(str5[1:3])   #el
print(str5[:6])    #welcom
print(str5[2:])    #lcome
print(str5[1: -1]) #elcom
print(str5[1: -2]) #elco

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)