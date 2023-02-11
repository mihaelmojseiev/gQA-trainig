# Задача 1
# Сделать проверку что вводимая строка является корректным IP адрессом

import ipaddress
ip = input('Введи ip: ')

def check_ip(ip):
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        return False
    else:
        return True

print(check_ip(ip))

# или

ip=list(map(int, input('Введи ip: ').split('.')))
print('True' if min(ip) >= 0 and max(ip) <= 255 else 'False')