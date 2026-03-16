def find_maximum_number (numbers):
    
    maximum_number = numbers[0]

    for num in numbers:
        if maximum_number > num:
            maximum_number = num
    return maximum_number
