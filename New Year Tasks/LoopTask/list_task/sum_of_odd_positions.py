number_list = [4, 6, 8, 7, 9, 17, 85, 44, 77]

sum_of_odd_position = 0

for index in range (1, len(number_list), 2):
   
   sum_of_odd_position += number_list[index]

print(sum_of_odd_position)     
