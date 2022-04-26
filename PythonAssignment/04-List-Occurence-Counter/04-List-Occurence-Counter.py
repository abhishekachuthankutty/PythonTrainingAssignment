sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
sample_dict = {}
result_list = []
i = 0
for item in sample_list:
    sample_dict[item] = 0
for item in sample_list:
    sample_dict[item]+=1
for item in sample_dict:
    if sample_dict[item] > 1:
        result_list.append(item)

print(result_list) 