import xmltodict
import json
import time

start = time.perf_counter()
for i in range(0,100):
    f = open('../data/XML1.txt', encoding='UTF-8', mode='r')
    json_file = open('../data/JSON1.json', encoding='UTF-8', mode='w')
    xml = f.read()
    f.close()
    dict_xml = xmltodict.parse(xml)
    json_data = json.dumps(dict_xml, ensure_ascii=False, indent=4)
    print(json_data)
    json_file.write(json_data)
    json_file.close()
    f.close()
print((time.perf_counter()-start))

