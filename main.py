import random

rnm = random.randint(1, 100)
print("guess a number between 1-100")
gs = 0

while gs < 5:
    nm = int(input("enter num: "))
    gs += 1
    if nm == rnm:
        print("nice")
        check = False
        break
    if nm >= rnm:
        print("Lower")
    elif nm <= rnm:
        print("Higher")

    if gs == 4:
        print("One last chance")
    if gs >= 5:
        print("Better luck next time")

