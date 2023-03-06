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