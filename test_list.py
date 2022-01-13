from mylist import MyList

my_list=MyList(1,2,3,4)
print(my_list)

for item in my_list:
  print(item)

print(len(my_list))

print(reversed(my_list))

print(my_list.append(5,6))

print(my_list.insert(2,2.5).insert(3,2.75))

print(my_list.map(lambda x: x+1))

print(my_list.pop().pop(5))

print(my_list.remove(1).remove(2))