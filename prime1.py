from math import sqrt

flag = 1
n = int(input("Enter a number:"))
for i in range(2, int(sqrt(n) + 1)):
    if n % i == 0:
        flag = 0
        break
if n <= 1:
    flag = 0
if flag == 1:
    print(n, "is prime number")
else:
    print(n, "is not prime")
