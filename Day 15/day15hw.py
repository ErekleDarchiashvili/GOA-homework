
#N1____________________________________



def name(full_name):
    names = full_name.split()
    first_letter = names[0][0]
    last_letter = names[-1][0]
    print(f"{first_letter}.{last_letter}")


name("Erekle Darchiashvili")




#N2_______________________________________


def print_ran(num_list):
    list_sum = sum(num_list)

    list_length = len(num_list)

    total = list_sum / list_length
    print(total)


num_list = [10, 20, 30, 40, 50]
print_ran(num_list)



#N3________________________________________


def is_pal(word):
    
    return word == word[::-1]


word = "level"


if is_pal(word):
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")


#N4____________________________________________
    


def remove_spaces(word1):
    word2 = word1.replace(" ", "")
    print(word2)


word1 = "Goal-Oriented Academy"
remove_spaces(word1)


#N5____________________________________________


def positive_and_negative(numbers):
    positive = 0
    negative = 0
    
    for num in numbers:
        if num > 0:
            positive = positive + num
    
    for num in numbers:
        if num < 0:
            negative = negative + num
    
    print(positive)
    print(negative)


numbers = [10, -5, 3, -8, 2, -1, 7]
positive_and_negative(numbers)


















