
#N1__________________________________________________________

text = "erekle darchiashvili"

def new_text(text):
    low_case = text.lower()
    
    upper_case = text.upper()

    capitalized = text.capitalize()

    find_index = text.find("a")

    return low_case, upper_case, capitalized, find_index

print(new_text(text))

#2N___________________________________________________________


fruits = ["orange", "apple", "grape"]

user_choice1 = int(input("Which fruit do you want to delete from the list?: "))

def user_choice(fruits):
    new_fruit = "banana"
    fruits.pop(user_choice1)
    fruits.append("banana")
    return fruits

print(user_choice(fruits))





