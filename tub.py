a = int(input("Sonlar kiriting: "))
b = 0
for i in range(1,a+1):
    b += a % i == 0
if b == 2 and a > 1:
    print("Tub son")
else:
    print("Bu tub son emas !")