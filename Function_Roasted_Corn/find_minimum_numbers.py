def find_minimum_number (numbers):
    minimum_number = numbers[0]

    for num in numbers:
        if num < minimum_number:
          minimum_number = num
    return minimum_number
