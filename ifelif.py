age = 27

if age < 18:
    print("You are not old enough to vote.")
elif age >= 18 and age < 21:
    print("You can vote but you cannot drink.")
elif age >= 21:
    print("You can vote and drink.")
else:
    print("Invalid age.")

# and

x = 5
y = 10
z = 15

# using 'and' operator
if x < y and y < z:
    print("y is between x and z")
else:
    print("y is not between x and z")

# or

x = 5
y = 10
z = 15

# using 'or' operator
if x > y or y > z:
    print("y is not between x and z")
else:
    print("y is between x and z")

# not 

x = 5
y = 10

# using 'not' operator
if not x > y:
    print("x is not greater than y")
else:
    print("x is greater than y")

# and 	Returns True if both statements are true	    x < 5 and  x < 10	
# or	Returns True if one of the statements is true	x < 5 or x < 4	
# not	Reverse the result, returns False if the result is true

# is 	Returns True if both variables are the same object	x is y	
# is not	Returns True if both variables are not the same object	x is not y


age = 20
status = "Adult" if age >= 18 else "Youth"
print(status)  # Виведе: Дорослий


result = 1 if True else 0
print(result)  # Виведе: 1