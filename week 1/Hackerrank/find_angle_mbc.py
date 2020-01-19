import math
a = int(input())
b = int(input())

c = math.sqrt(a**2 + b**2)

n = math.asin(a/c)


print(str(int(round(math.degrees(n)))) + "°")
