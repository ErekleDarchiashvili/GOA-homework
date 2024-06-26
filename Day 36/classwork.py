def filter_list(l):
    filter_list = []
    
    for i in l:
        if i.isalpha():
            filter_list.append(i)
    return filter_list

l = [1,'a','b',0,15]