from netaddr import IPNetwork
from net_map.net_object import create_preconf_net_object, NetObjectType, FilterAction, FilterTable
from net_map.netmap import create_preconf_net_map
from net_map.reachability import ReachabilityController
from net_map.subnet import create_preconf_subnet


net_map = create_preconf_net_map('Test map')

sub_net_1 = create_preconf_subnet(net_map)
sub_net_1.name = 'sub_net_1'
net_map.subnets.append(sub_net_1)

sub_net_2 = create_preconf_subnet(net_map)
sub_net_2.name = 'sub_net_2'
net_map.subnets.append(sub_net_2)

sub_net_3 = create_preconf_subnet(net_map)
sub_net_3.name = 'sub_net_3'
net_map.subnets.append(sub_net_3)

sub_net_4 = create_preconf_subnet(net_map)
sub_net_4.name = 'sub_net_4'
net_map.subnets.append(sub_net_4)

host_11 = create_preconf_net_object(net_obj_type=NetObjectType.host, subnet=sub_net_1, is_filter=True)
host_11.name = 'host_11'
host_11.interfaces[0].cidr = IPNetwork('10.1.1.10/24')
host_11.interfaces[0].gateway = IPNetwork('10.1.1.20/24')

host_11.add_service()
host_11.services[0].port = 999
host_11.services[0].interfaces = host_11.interfaces

host_11.add_filter_rule()
#host_11.add_filter_rule(dst_port=7777)
sub_net_1.net_objects.append(host_11)

host_12 = create_preconf_net_object(net_obj_type=NetObjectType.host, subnet=sub_net_1)
host_12.name = 'host_12'
host_12.interfaces[0].cidr = IPNetwork('10.1.1.11/24')
host_12.interfaces[0].gateway = IPNetwork('10.1.1.20/24')
sub_net_1.net_objects.append(host_12)

#service = Service(name='TEST', port=777, interfaces=)
host_12.add_service()
host_12.add_service()
host_12.add_service()
host_12.services[0].port = 777
host_12.services[0].interfaces = host_12.interfaces
host_12.services[1].port = 888
host_12.services[1].interfaces = host_12.interfaces
host_12.services[2].port = 999
host_12.services[2].interfaces = host_12.interfaces

switch_11 = create_preconf_net_object(net_obj_type=NetObjectType.switch, subnet=sub_net_1, is_filter=True)
switch_11.name = 'switch_11'
switch_11.add_filter_rule(action=FilterAction.DENY, dst_port=888)
switch_11.add_filter_rule(src='10.3.1.10', action=FilterAction.DENY, dst_port=999)
switch_11.add_filter_rule(dst='10.1.1.11', action=FilterAction.DENY, dst_port=999)
sub_net_1.net_objects.append(switch_11)

switch_12 = create_preconf_net_object(net_obj_type=NetObjectType.switch, subnet=sub_net_1, is_filter=True)
switch_12.name = 'switch_12'
switch_12.add_filter_rule()
sub_net_1.net_objects.append(switch_12)

router_1 = create_preconf_net_object(NetObjectType.router, subnet=net_map.subnets[0])
router_1.name = 'router_1'
router_1.interfaces[0].cidr = IPNetwork('10.1.1.20/24')
router_1.interfaces[1].cidr = IPNetwork('10.1.2.20/24')
net_map.routers.append(router_1)

rule_list = ['-n 10.1.1.0/24 -g 10.1.1.20/24',
             '-n 10.1.2.0/24 -g 10.1.2.20/24',
             '-n 10.0.0.0/8 -g 10.1.2.30/24']

router_1.set_routing_table('\n'.join(rule_list))

router_2 = create_preconf_net_object(NetObjectType.router, subnet=net_map.subnets[0])
router_2.name = 'router_2'
router_2.interfaces[0].cidr = IPNetwork('10.1.1.21/24')

rule_list = ['-n 10.1.1.0/24 -g 10.1.1.21/24']
router_2.set_routing_table('\n'.join(rule_list))

net_map.routers.append(router_2)

router_3 = create_preconf_net_object(NetObjectType.router, subnet=net_map.subnets[0])
router_3.name = 'router_3'
router_3.interfaces[0].cidr = IPNetwork('10.4.1.20/24')
router_3.interfaces[1].cidr = IPNetwork('10.3.1.20/24')
router_3.interfaces[2].cidr = IPNetwork('10.1.2.30/24')
net_map.routers.append(router_3)

rule_list = ['-n 10.4.1.0/24 -g 10.4.1.20/24',
             '-n 10.3.1.0/24 -g 10.3.1.22/24',
             '-n 10.1.2.0/24 -g 10.1.2.30/24',
             '-n 10.1.1.0/24 -g 10.1.2.20/24']

router_3.set_routing_table('\n'.join(rule_list))

router_4 = create_preconf_net_object(NetObjectType.router, subnet=net_map.subnets[0])
router_4.name = 'router_4'
router_4.interfaces[0].cidr = IPNetwork('10.3.1.23/24')
router_4.interfaces[1].cidr = IPNetwork('10.3.1.22/24')
net_map.routers.append(router_4)

rule_list = ['-n 10.0.0.0/8 -g 10.3.1.20/24',
             '-n 10.3.1.0/24 -g 10.3.1.23/24']

router_4.set_routing_table('\n'.join(rule_list))

host_21 = create_preconf_net_object(net_obj_type=NetObjectType.host, subnet=sub_net_2, is_filter=True)
host_21.name = 'host_21'
host_21.interfaces[0].cidr = IPNetwork('10.1.2.10/24')
host_21.interfaces[0].gateway = IPNetwork('10.1.2.20/24')
host_21.add_filter_rule()
sub_net_2.net_objects.append(host_21)

host_22 = create_preconf_net_object(net_obj_type=NetObjectType.host, subnet=sub_net_2, is_filter=True)
host_22.name = 'host_22'
host_22.interfaces[0].cidr = IPNetwork('10.1.2.30/24')
host_22.interfaces[0].gateway = IPNetwork('10.1.2.20/24')
host_22.add_filter_rule()
sub_net_2.net_objects.append(host_22)

host_31 = create_preconf_net_object(net_obj_type=NetObjectType.host, subnet=sub_net_3, is_filter=True)
host_31.name = 'host_31'
host_31.interfaces[0].cidr = IPNetwork('10.3.1.10/24')
host_31.interfaces[0].gateway = IPNetwork('10.3.1.23/24')
host_31.add_filter_rule()
sub_net_3.net_objects.append(host_31)

switch_21 = create_preconf_net_object(net_obj_type=NetObjectType.switch, subnet=sub_net_2, is_filter=True)
switch_21.name = 'switch_21'
switch_21.add_filter_rule()
sub_net_2.net_objects.append(switch_21)

switch_22 = create_preconf_net_object(net_obj_type=NetObjectType.switch, subnet=sub_net_2, is_filter=True)
switch_22.name = 'switch_22'
switch_22.add_filter_rule()
sub_net_2.net_objects.append(switch_22)

host_41 = create_preconf_net_object(net_obj_type=NetObjectType.host, subnet=sub_net_4, is_filter=True)
host_41.name = 'host_41'
host_41.interfaces[0].cidr = IPNetwork('10.4.1.10/24')
host_41.interfaces[0].gateway = IPNetwork('10.4.1.20/24')
host_41.add_filter_rule()
sub_net_4.net_objects.append(host_41)

host_42 = create_preconf_net_object(net_obj_type=NetObjectType.host, subnet=sub_net_4, is_filter=True)
host_42.name = 'host_42'
host_42.interfaces[0].cidr = IPNetwork('10.4.1.42/24')

host_42.add_filter_rule(action=FilterAction.DENY, src_port=777, table_type=FilterTable.INPUT)
host_42.add_filter_rule(action=FilterAction.DENY, dst_port=888, table_type=FilterTable.INPUT)
host_42.add_filter_rule(src='10.4.1.43', action=FilterAction.DENY, dst_port=999, table_type=FilterTable.INPUT)
host_42.add_filter_rule()

sub_net_4.net_objects.append(host_42)
host_42.add_service()
host_42.services[0].port = 777
host_42.services[0].interfaces = host_42.interfaces
host_42.add_service()
host_42.services[1].port = 888
host_42.services[1].interfaces = host_42.interfaces
host_42.add_service()
host_42.services[2].port = 999
host_42.services[2].interfaces = host_42.interfaces

host_43 = create_preconf_net_object(net_obj_type=NetObjectType.host, subnet=sub_net_4, is_filter=True)
host_43.name = 'host_43'
host_43.interfaces[0].cidr = IPNetwork('10.4.1.43/24')
host_43.add_filter_rule()
sub_net_4.net_objects.append(host_43)
host_43.add_service()
host_43.services[0].port = 777
host_43.services[0].interfaces = host_43.interfaces
host_43.add_service()
host_43.services[1].port = 888
host_43.services[1].interfaces = host_43.interfaces
host_43.add_service()
host_43.services[2].port = 999
host_43.services[2].interfaces = host_43.interfaces

switch_41 = create_preconf_net_object(net_obj_type=NetObjectType.switch, subnet=sub_net_4, is_filter=True)
switch_41.name = 'switch_41'
switch_41.add_filter_rule()
sub_net_4.net_objects.append(switch_41)

switch_12.connect(switch_11)
switch_12.connect(router_2)
switch_11.connect(router_1)
switch_21.connect(switch_22)
host_11.connect(switch_11)
host_12.connect(switch_11)
host_21.connect(switch_21)
host_31.connect(router_4)
host_41.connect(switch_41)
host_42.connect(host_43)
router_1.connect(switch_21)
router_3.connect(switch_41)
router_3.connect(router_4)
router_3.connect(switch_22)

controller = ReachabilityController(net_map)

print 'host_11 -> host_12 777 - True', controller.has_access(host_11, host_12, dst_service=host_12.services[0])
print 'host_11 -> host_12 888 - False', controller.has_access(host_11, host_12, dst_service=host_12.services[1])
print 'host_11 -> host_31 - True', controller.has_access(host_11, host_31)
print 'host_11 -> host_41 - True', controller.has_access(host_11, host_41)
print 'host_11 -> host_22 - False', controller.has_access(host_11, host_22)
print 'host_31 -> host_12 999 - False', controller.has_access(host_31, host_12, dst_service=host_12.services[2])
print 'host_31 -> host_11 999 - False', controller.has_access(host_31, host_11, dst_service=host_11.services[0])

print 'host_41 -> host_12 999 - False', controller.has_access(host_41, host_12, dst_service=host_12.services[2])
print 'host_41 -> host_11 999 - True', controller.has_access(host_41, host_11, dst_service=host_11.services[0])

print 'host_31 -> host_12 777 - True', controller.has_access(host_31, host_12, dst_service=host_12.services[0])
print 'host_21 -> host_12 999 - False', controller.has_access(host_21, host_12, dst_service=host_12.services[2])
print 'host_21 -> host_11 999 - True', controller.has_access(host_21, host_11, dst_service=host_11.services[0])

print 'host_43 777 -> host_42 - False', controller.has_access(host_43, host_42, src_service=host_43.services[0])
print 'host_43 888 -> host_42 - True', controller.has_access(host_43, host_42, src_service=host_43.services[1])
print 'host_43 -> host_42 888 - False', controller.has_access(host_43, host_42, dst_service=host_42.services[1])
print 'host_43 -> host_42 999 - False', controller.has_access(host_43, host_42, dst_service=host_42.services[2])

#pprint(net_map.to_dict())

controller.calculate()
print controller.get_reachable_services(host_11)