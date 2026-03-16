number_list = [4, 6, 8, 7, 9, 17, 85, 44, 77]

sum = 0
average = 0

for digit in (number_list):
   
   sum += digit
   average = sum / len(number_list)

print(average)   
