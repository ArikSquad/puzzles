# collatz value generator
def collatz_g(x: int):
    n = x
    while n != 0:
        if x == 1:
            n = 0
        elif x % 2 == 1:
            x = 3*x+1
        elif x % 2 == 0:
            x = 0.5*x
        yield x

# iterate through a collatz generator until 1 has been given as a value
def collatz(a: int) -> [int]:
    l = [a] # list with first value as alkuarvo
    gen = collatz_g(a)
    s = True # should continue
    while s:
        r: int = int(next(gen))
        if (r == 1): # don't loop infinitely on 1
            s = False
        l.append(r)

    return l

# Collatz sequence with starting value 23
print(f"23 : {collatz(23)}")

# dictionary to hold alkuarvo and the length
d = {}
for i in range(2, 101):
    cl = collatz(i)
    d[i] = len(cl)

# sort items by their value
d = sorted(d.items(), key=lambda item: item[1], reverse=True)[:5]

i = 0
# iterate through the lists
for k, v in d:
    i += 1
    print(f"Pituus: {k} Alkuarvo: {v}")
    # five have been shown
    if i == 5:
        break

