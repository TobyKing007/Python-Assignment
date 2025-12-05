even_sum = 0
odd_even = 0

count = int(input("How many integers will you enter"))

for i in range(count):
    num = int(input("Enter an integer"))

    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

print("Sum of even integers:", even_sum)
print("Sum of odd integers:", odd_even)
