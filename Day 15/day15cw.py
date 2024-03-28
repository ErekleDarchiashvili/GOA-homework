

def names(name):
    print(name)

names("Erekle")

names("Giorgi")





def add(user1, user2):
    print(user1 + user2)

add(5, 10)


def nums(user3, user4):
    print(user3 * user4)


nums(3, 10)




#1_____________________________

def devide(num1, num2):
    print(num1 / num2)


def plus(num1, num2):
    print(num1 + num2)


def minus(num1, num2):
    print(num1 - num2)


def multiplication(num1, num2):
    print(num1 * num2)


devide(10, 5)

plus(20, 10)

minus(10, 5)

multiplication(10, 5)


#შექმენით ფუნქცია, რომელსაც გადასცემთ მართკუთხედის სიგრძესა და სიმაღლეს, გამოითვლით მის ფართობს.


def rectangle(length, height):
    print(length * height)

rectangle(10, 2)



# დავალება3: შექმენით ფუნქცია, რომელსაც გადასცემთ მართკუთხედის ოთხ გვერდს, გამოითვლით მის პერიმეტრს.


def rectangle2(lenght1, lenght2, height1, height2):
    print(lenght1 + lenght2 + height1 + height2)

rectangle2(10, 10, 5, 5)



#დავალება4: შექმენით ფუნქცია, რომელიც მიიღებს არგუმენტად სიას და დაბეჭდეთ სიის რიცხვების ჯამი, არ გამოიყენოთ sum.

my_list = [1, 2, 3, 4, 5]



def calculate(my_list):
    total = 0
    for num in my_list:
        total = total + num
    print(total)



calculate(my_list)





#დავალება5: შექმენით ფუნქცია, რომელიც დაბეჭდავს კონკრეტული სიიდან მინიმალურ და მაქსიმალურ რიცხვებს, 
#არ გამოიყენოთ min და max. გამოიყენეთ def, for, if/else, indexing, prin




def print_min_max(ran_list):
    min = ran_list[0]
    max = ran_list[0]
    for i in ran_list:
        if min > i:
            min = i
        if max < i:
            max = i

    print(min, max)



print_min_max([2, 4, 6, 8, 10])


