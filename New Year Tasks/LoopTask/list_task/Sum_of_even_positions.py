number_list = [4, 6, 8, 7, 9, 17, 85, 44, 77]

sum_of_even_position = 0

for index in range (0, len(number_list), 2):
   
   sum_of_even_position += number_list[index]

print(sum_of_even_position)     
