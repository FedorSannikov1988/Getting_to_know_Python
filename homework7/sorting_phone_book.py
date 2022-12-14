'''
data_for_write = [["Фамилия1", "Имя1*", "Отчество1", 89609752504], ["Фамилия2", "Имя2*", "Отчество2", 89609752504], ["Фамилию3", "Имя3*", "Отчество3", 89609752504]]
#flag = "line"
flag = "column"
safe_data_in_phone_directory(data_for_write, flag)
data = loading_data_from_phone_directory()
print_data.print_all_list_in_terminal(data)
'''

'''
data_for_write = [["Р", "Р*", "Р", 20], ["А", "А", "А", 5]]

print(data_for_write[0][0])

def keyFunc(item):
   return item[0][0]

print(data_for_write.sort(key=keyFunc))
'''