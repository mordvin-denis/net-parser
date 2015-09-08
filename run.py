import json
import os
from datetime import datetime
from core import parse_network
from plugins.mock_plugin import MockPlugin


plugins_list = [MockPlugin()]

net_map = parse_network('net_map_' + datetime.now().strftime("%d_%m_%y__%H_%M_%S"), plugins_list)
net_map_json_data = json.dumps(net_map.to_dict())

print(net_map_json_data)

save_path = os.path.abspath('saves/' + net_map.name + '.map')
with open(save_path, 'wb') as fw:
    fw.write(net_map_json_data)