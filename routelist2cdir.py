import ipaddress
from netaddr import IPSet


routes_file = open('routes.txt', 'r')
route_list = []
ipnet_set = IPSet()
for route_line in routes_file.readlines():
    route_entry = route_line.split()
    ipnet_entry = route_entry[0] + '/' + route_entry[1]
    IPNet = ipaddress.ip_network(ipnet_entry)
    route_list = route_list + [str(IPNet)]
    ipnet_set = ipnet_set | IPSet([str(IPNet)])
routes_file.close()

ipnetwk = []
for cidr in ipnet_set.iter_cidrs():
    print(cidr.network,cidr.netmask)
    ipnetwk = ipnetwk + [str(cidr)]

print()
print(route_list)
print()
print(ipnetwk)
print()
print('length route list:', len(route_list), 'length reduced list:', len(ipnetwk))
