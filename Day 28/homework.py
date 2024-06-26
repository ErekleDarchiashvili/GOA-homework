#N1______________________________________

# def solution(number):
#     if number < 0:
#         return 0
#     total_sum = 0
#     for i in range(number):
#         if i % 3 == 0 or i % 5 == 0:
#             total_sum = total_sum + i
#     return total_sum



def Out(a):
    print(a)
    a+=1
    if a!=5:
        Out(a)



def out(a):
    print(a)
    a-=1
    if a!=1:
        Out(a)


out(3)