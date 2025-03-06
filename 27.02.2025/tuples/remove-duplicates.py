list  = ["suvam", 5, 77.8, 'char', 5, 77.8, 5, 'char']
for i in range (0, (len(list)-1)):
    if(list.count(list[i]) > 1):
        list.remove(list[i])
print(list)