print("a    b   pow(a, b)")

a = 1
b = 2

for i in range(5):
    power_value = int(pow(a, b))
    print(f"{a} {b} {power_value}")
    a += 1
    b += 1
