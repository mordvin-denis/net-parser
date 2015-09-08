from net_map.netmap import create_preconf_net_map


def parse_network(name, plugins_list):
    net_map = create_preconf_net_map(name)

    for plugin in plugins_list:
        plugin.run(net_map)

    return net_map
