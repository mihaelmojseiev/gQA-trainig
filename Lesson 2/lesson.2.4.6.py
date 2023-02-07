"""
 Lesson 4.6
 Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
 Prefix                10.0.24.0/24
 AD/Metric             110/41
 Next-Hop              10.0.13.3
 Last update           3d18h
 Outbound Interface    FastEthernet0/0
 Ограничение: Все задания надо выполнять используя только пройденные темы.
 ospf_route = "       10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"


"""
ospf_route = "       10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
mid = ospf_route.replace("via","").replace("[","").replace("]","").replace(",","").split()
print(" Prefix",mid[0].rjust(28, " "),'\n',"AD/Metric",mid[1].rjust(19, " "),'\n',"Next-Hop",mid[2].rjust(23, " "),'\n',"Last update",mid[3].rjust(16, " "),'\n',"Outbound Interface",mid[4].rjust(19, " "))


