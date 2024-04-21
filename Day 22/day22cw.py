

def manual_pop(collection, index):
    new_collection = []

    for i in range(0, len(collection)):
        if i != index:
            new_collection.append(collection[i])
    return new_collection


numbers = [1, 2, 3, 4, 5]
print(manual_pop(numbers, 0))













