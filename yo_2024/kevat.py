# a number such as 2 works, 8 does not, this code is a fixed version
n: int = int(input("n: ")) # n = 8
m: int = n
while n > 1:
    for a in range(2, m + 1):
        if n % a == 0:
            print(a)
            n = n // a
            break

