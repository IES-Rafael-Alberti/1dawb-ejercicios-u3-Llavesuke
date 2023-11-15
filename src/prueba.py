sample = '1,2,3,4,5,6,7,8,9'


str_list = sample.split(',')

for i in range(len(str_list)):
    str_list[i] = int(str_list[i])

print(str_list)