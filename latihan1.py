from random import random
n = int(input("masukkan nilai N:"))
i = 0
while i < n:
    a = random()
    if a < 2:
        i += 1
        print(f"data ke: {i} => {a}")
print("selesai")