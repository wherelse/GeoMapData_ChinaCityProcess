import json
import os

# 读取省/自治区/直辖市边界数据
with open('.\china.json', 'rb') as f:
    china_area = json.load(f)

# 保留直辖市边界数据
china_citys = {'features': []}
for area in china_area['features']:
    # print(china_area['features'].index(area),area['properties']['name'])
    if (area['properties']['name'] == '北京市' or
        area['properties']['name'] == '天津市' or
        area['properties']['name'] == '上海市' or
        area['properties']['name'] == '重庆市' or
        area['properties']['name'] == '香港特别行政区' or
        area['properties']['name'] == '澳门特别行政区' or
            area['properties']['name'] == ''):
        china_citys['features'].append(area)

# 合入各地级市边界数据
for item in os.scandir('.\province'):
    if (item.name == '110000.json' or
        item.name == '120000.json' or
        item.name == '500000.json' or
        item.name == '310000.json' or
        item.name == '810000.json' or
            item.name == '820000.json'):  # 排除北京上海天津重庆香港澳门
        continue
    else:
        with open(item, 'rb') as file:
            province = json.load(file)
        for area in province['features']:
            china_citys['features'].append(area)

with open('china_city.json', 'w', encoding="utf8") as json_file:
    json.dump(china_citys, json_file, ensure_ascii=False)
