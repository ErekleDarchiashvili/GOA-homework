#______N1__________

# def litres(time):
#     time = time // 2
#     return time



# time = 3
# print(litres(time))



#______N3___________



# def grow(arr):
#     result = 1
#     for i in arr:
#         result = i * result
#     return result
        

# arr = [1, 2, 3, 4, 5]
# result = (grow(arr))
# print(result)



#_______N4____________


x = ["1, 2, 3, 4, 5, 6, 7, 8, 9,"]


def fake_bin(x):
    result = []
    for i in x:
        if i < 5:
            result.append(0)
        if i > 5:
            result.append(1)
    return result




result = fake_bin(int(x))
print(result)
