import random
x = random.randint(1, 1000)
xmm = random.randint(1, 2)
answer_one = x + x
answer_two = x - x
xx = str(x)
if xmm == 1:
    print("What is " + xx + "+" + xx)
    inp = int(input(": "))
    if inp == answer_one:
        print("Correct")
    else:
        print("Wrong")
else:
    print("What is " + xx + "-" + xx)
    inp = int(input(": "))
    if inp == answer_two:
        print("Correct")
    else:
        print("Wrong")
