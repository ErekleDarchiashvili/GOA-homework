


def even_num_total(numbers):
    total = 0
    for i in numbers:
        if i % 2 == 0:
            total = total + i
    return total   
        

numbers = [1, 2, 3, 4, 5]


print(even_num_total(numbers))



#N3_________________________________



def odds_total(nums):
    total = 0
    total1 = 0
    for i in nums:
        if i % 2 != 0:
            total = total + i
        if i % 2 == 0:
            total1 = total1 + i
    return total, total1



nums = [1, 2, 3, 4, 5]


print(odds_total(nums))




#N4__________________________________


def list_len(ran_nums):
    return len(ran_nums)



ran_nums = [1, 2, 3, 4, 5]

print(len(ran_nums))

#N5____________________________________


mylist = [1, 2, 3, 4, 5]

mylist[4]


