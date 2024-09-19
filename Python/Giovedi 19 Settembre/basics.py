name = "Spoolyy"
age = 25
# if you wish to insert the value of a variable yourself use the method below
# name = input("insert your name: ")
# age = int(input("insert your age: "))

# if you wish to write decimal values ',' won't work. you MUST use '.' 
# f.ex.: NOT 3,14 // YES 3.14
print ("Hello i'm", name, "and i'm", age, "years old")

string = "ciao, mondo"
print(len(string))
print(string.upper)
print(string.split(','))
print(string.replace('mondo', 'universo'))

numeri = [3, 1, 4, 2, 5] 

print(len(numeri)) 
numeri.append(6) 
print(numeri) 
numeri.insert(2, 10) 
print(numeri) 
numeri.remove(4) #this one filters the VALUE not the index, basically var.remove(4) will look for the value '4' instead of removing the value at index 4
print(numeri) 
numeri.sort() 
print(numeri) 