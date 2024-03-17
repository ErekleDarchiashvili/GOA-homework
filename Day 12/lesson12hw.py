

#N1____________________________________________


erekles_list = []


first_name = input("please enter your name: ")

last_name = input("please enter your last name: ")

age = int(input("please enter your age: "))

addres = input("please enter your addres: ")


erekles_list.append(first_name)
erekles_list.append(last_name)
erekles_list.append(age)
erekles_list.append(addres)


print(erekles_list[0:2])
print(erekles_list[1:3])
print(erekles_list[0:3])
print(erekles_list[1:4])





g = int(input("please enter an negative number: "))


for i in range(g,0):
    print(i)





























full_name = "Erekle Darchiashvili"

print(full_name[0:6])

print(full_name[6:30])



#N4____________________________________________


fav_films = ["Nights", "Count Me Out", "Let it happen", "Massive", "Skyline to"]

#couldnt think of any films so i wrote down my favorite songs

print(fav_films[0:1])
print(fav_films[-5:2])

print(fav_films[2:4])
print(fav_films[-3:5])

print(fav_films[3:5])
print(fav_films[-4:5])



#N5____________________________________________


user = input("enter name of the academy you study at: ")

right_choice = "Goa"


if user[0] == right_choice[0]:
    print("Goa academy is the best choice")
else:
    print("wrong choice")
















