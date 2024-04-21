#N3_________________________________

numbers = [ 1, 2, 3, 4, 5]
total = 0

for i in numbers:
    total = i + total
    arithmetical_mean = total / len(numbers)
 
print(arithmetical_mean)


#N4___________________________________


nums = [ 3, -2, 4, 6, -7]

negative_nums = []

positive_nums = []

for i in nums:
    if i < 0:
        negative_nums.append(i)
    else:
        positive_nums.append(i)
   

print("positive numbers", positive_nums)
print("negative numbers", negative_nums)


