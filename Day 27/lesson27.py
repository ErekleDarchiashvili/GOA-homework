
#N1___________________________

nums = [1, 1.5, 2, 2.5]

result = []

for i in nums:
    if i % 2 == 0:
        i = i * 2
        result.append(i)
    if i % 2 != 0:
        i = i * 4 
        result.append(i)

print(result)


#N2_______________________________



def lista(names):
    listo = []
    for i in range(len(names)):
        if i % 2 == 0:
            listo.append(names[i].upper())
        else:
            listo.append(names[i].lower())
    return listo

names = ["chad1", "chad2", "chad3", "chad4"]
listo = lista(names)
print(listo)
 



#N7_______________________________________


def collection1(collection, search_term):
    count = 0
    for item in collection:
        if item == search_term:
            count = count + 1
    return count


collection = [1, 1, 1, 2, 3, 4]
search_term = 1
print(collection1(collection, search_term))


#N8_________________________________________



def nums0(nums1):
    liste = []
    for i in nums1:
        if i % 2 != 0:
            liste.append(i)
    return liste



nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
liste = nums0(nums1)
print(liste)



#N9____________________________________________



def list3(list1, list2):
    return list1 + list2


list1 = [1, 5, 8]
list2 = [2, 3, 4]

combined_list = list3(list1, list2)
print(combined_list)







