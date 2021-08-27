def choice(u,it):
    if it == 1:
        it = "Rock"
    elif it == 2:
        it = "Paper"
    elif it == 3:
        it = "Scissors"

    if u == 1:
        u = "Rock"
    elif u == 2:
        u = "Paper"
    elif u == 3:
        u = "Scissors"

    print(f"\nYou chose {u}, computer chose {it}.\n")
    print(a, " - ", b)

from random import randint

a = 0
b = 0

while True:
    u = int(input("Rock - 1\nPaper - 2\nScissors - 3\n"))
    it = randint(1,3)

    if u==1:
        if it==1:
            choice(u,it)
        elif it==2:
            b += 1
            choice(u,it)
        elif it==3:
            a += 1
            choice(u,it)

    if u==2:
        if it==1:
            a += 1
            choice(u,it)
        elif it==2:
            choice(u,it)
        elif it==3:
            b += 1
            choice(u,it)

    if u==3:
        if it==1:
            b += 1
            choice(u,it)
        elif it==2:
            a += 1
            choice(u,it)
        elif it==3:
            choice(u,it)

    if b == 3:
        print("Computer Won")
        break
    elif a == 3:
        print("Player Won")
        break

