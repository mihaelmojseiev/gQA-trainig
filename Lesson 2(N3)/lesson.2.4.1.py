"""
 Lesson 4.1
 Используя подготовленную строку nat, получить новую строку, в которой в имени интерфейса вместо FastEthernet написано GigabitEthernet. Полученную новую строку вывести на стандартный поток вывода (stdout) с помощью print.
 Ограничение: Все задания надо выполнять используя только пройденные темы.
 nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"

"""
nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
new_string = nat.replace('FastEthernet', 'GigabitEthernet')
print(new_string)

# sor

#nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
#print(nat.replace('FastEthernet', 'GigabitEthernet'))