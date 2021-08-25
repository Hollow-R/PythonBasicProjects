
entry = """
See all even, odd, prime numbers from 0 to the number you entered
"""

print(entry)
n = int(input("Enter the number :"))

def Odd(x):
    odd = 0
    for i in range(2,x+1):
        if x%i == 0:
            odd+=1
    if odd == 1:
        m.append(x)

l = []
k = []
m = []

for s in range(1,n+1):
    if s%2 == 0:
        k.append(s)
    if s%2 != 0:
        l.append(s)
    Odd(s)

print("Even Numbers :\n",k)
print("Prime Numbers :\n",l)
print("Odd Numbers :\n",m)
