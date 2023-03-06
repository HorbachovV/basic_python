age = 27

if age < 18:
    print("You are not old enough to vote.")
elif age >= 18 and age < 21:
    print("You can vote but you cannot drink.")
elif age >= 21:
    print("You can vote and drink.")
else:
    print("Invalid age.")