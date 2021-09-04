from random import randint

print("Welcome to dice simulator !")

ran = []

while True:
    a = input("To roll dice, press 'e'\nTo exit, press 'q'\n")

    if a == "e":
        try:
            e = abs(int(input("How many dice you want to roll :\n")))
            for i in range(1,e+1):
                i = randint(1,6)
                ran.append(i)
            print(ran)
            ran = []
        except:
            print("ERROR")
            continue

    elif a == "q":
        break

    else:
        continue

