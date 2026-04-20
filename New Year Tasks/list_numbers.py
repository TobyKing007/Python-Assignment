def sort_numbers():
    numbers = [4, 1, 3, 9, 2]
    #numbers.sort()
    sorted_numbers = sorted(numbers)
    return (sorted_numbers)

sort_numbers()



def even_numbers():

    numbers = [4, 1, 3, 5, 6,12, 15, 22, 56, 32, 33, 54, 67]
    
    for number in numbers:
        if number % 2 == 0:
            return (number)

even_numbers()



def combine_lists():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]

    combined =  list1 + list2

    return (combined)

combine_lists()



def words_greater_than_three_letters():
    words = ["lamb", "kit", "yam", "kings", "dogs", "man"]

    new_word = []

    for word in words:
        if len(word) > 3:
            new_word.append(word)
        
    return (new_word)

words_greater_than_three_letters()


def sorted_function(numbers):

    digits = len(numbers)
    
    for number in range(digits):

        


    
