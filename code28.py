#  Program to Find Numbers Divisible by Another Number


my_list = [12, 65, 54, 39, 102, 339, 221,]

#  anonymous function to filter
result = list(filter(lambda x: (x % 13 == 0), my_list))

print("Numbers divisible by 13 are",result)