def all_the_same(my_list):
     same = True
     first_number = my_list[0]
     index = 0
     while index < len(my_list) and same:
          if my_list[index] != first_number: 
               same = False
          index = index + 1
          print(my_list[index])
     return same

my_list=[5,5,5,1,0,0,0]

print(all_the_same(my_list))