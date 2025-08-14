# Defining Function
"""
def add(arg1, arg2):
    total = arg1 + arg2
    return total


out = add(2, 3)
print(out)


def adder(arg1, arg2):
    total = arg1 + arg2
    print(total)

adder(10,50)
print(adder(10, 50))
"""


def summ(arg):
    x = 0
    for i in arg:
        x = x + i
    return x


#out = summ([10, 20, 30])
#print(out)

#summ([10,20],[30,50])

# Default Argument
def greetings(MSG="Morning"):
    print(f"Good {MSG}")
    print("Welcome to the function.")


greetings()
greetings("Evening")

# Keywords arguments
def vac_feedback(vac, efficacy):
    print(f"{vac} Vaccine is having {efficacy} % efficacy.")
    if (efficacy > 50) and (efficacy <= 75):
        print("Seems not so effective, Needs more trial.")
    elif (efficacy > 75) and (efficacy < 90):
        print("Can consider this vaccine.")
    elif efficacy >= 90:
        print("Sure, will take the shot.")
    else:
        print("Needs many more trials.")

#vac_feedback("Pfizer", 95)
#vac_feedback("Unknown", 45)
vac_feedback(efficacy=34, vac="Unknown")