# For loop
for i in range(1, 6):
    print(i)

# While loop
i = 1
while i < 6:
    print(i)
    i += 1

# even numbers
for i in range(0, 21, 2):
    print(i)

# odd numbers
for i in range(1, 21, 2):
    print(i)


# break continue
for i in range(1, 10):
    if i == 3:
        break
    print(i)
print('End of programm')

for i in range(1, 10):
    if i == 3 or i == 5 or i ==7:
        continue
    print(i)
print('End of programm')

for char in "foo":
    print(char)