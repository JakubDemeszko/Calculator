import math
a = float(input("Input the a value: "))
b = float(input("Input the b value: "))
c = float(input("Input the c value: "))
delta = b**2 - 4 * a * c

if delta > 0:
    print("Function has 2 zero places.")
    z = math.sqrt(delta)
    x1 = ((-1 * b) - z) / (2 * a)
    x2 = ((-1 * b) + z) / (2 * a)
    print(x1, x2)
elif delta == 0:
    print("Function has 1 zero place.")
    z = math.sqrt(delta)
    x0 = (-1 * b) / (2 * a)
    print(x0)
else:
    print("Funckja has no zero places.")

n1 = int(input("Input your left range: "))
n2 = int(input("Input your right range: "))
values = []
for i in range(n1, n2+1):
    fx = a * i**2 + b * i + c
    print("Function value in " + str(i) + " is equal: " + str(fx))
