
#N1______________________________________________

def user_contacts(data):
    contacts = {}
    for i in data:
        name = i[0]
        zip_code = i[1] if len(i) > 1 else None
        contacts[name] = zip_code
    return contacts



#N2_______________________________________________


def fillable(stock, merch, n):
    if merch in stock and stock[merch] >= n:
        return True
    return False
