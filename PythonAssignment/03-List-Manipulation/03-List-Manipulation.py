number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print (number_list)
print(id(number_list))
i = 0
while i < len(number_list):
    if number_list[i] > 50:
        number_list.remove(number_list[i])
        i = 0
    i+=1

print ("List after items greater than 50 are removed")
print (number_list)
print(id(number_list))
