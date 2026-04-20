number_list = [4, 6, 8, 7, 9, 17, 85, 44, 77]

multiply_third_positions = 1

for index in range (2, len(number_list), 3):
   
   multiply_third_positions *= number_list[index]

print(multiply_third_positions)     
