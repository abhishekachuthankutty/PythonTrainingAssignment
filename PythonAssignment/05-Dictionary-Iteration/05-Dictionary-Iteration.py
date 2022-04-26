ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
print(ascii_dict)
for item in list(ascii_dict):
    temp = ascii_dict[item]
    ascii_dict[item] = item
    ascii_dict[temp] = ascii_dict.pop(item)
print (ascii_dict)

