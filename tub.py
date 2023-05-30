a = int(input(". . ."))
b = 0
for i in range(1,a+1):
    b += a % i == 0
if b == 2 and a > 1:
    print("Tub")
else:
    print("Tub emas")