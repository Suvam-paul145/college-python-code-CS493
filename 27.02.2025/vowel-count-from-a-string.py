print("Enter a string: ")
string = input()
l = string.__len__()
print("the vowels in the string are: ")
for i in range (0, l):
    if(string[i] == 'a' or string[i] == 'e' or string[i] == 'i' or string[i] == 'o' or string[i] == 'u'):
        print(string[i])