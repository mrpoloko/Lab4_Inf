from tasks.task2.task2 import printjson, parse
import time

start=time.perf_counter()
for i in range(0,100):
    xml_file = open("../data/XML.txt", encoding='utf-8', mode='r')
    json_file = open("../data/JSON2.json", encoding='utf-8', mode='w')

    xml_file.readline()
    r = xml_file.read()

    printjson(parse(r), 0, json_file)
    xml_file.close()
    json_file.close()

print((time.perf_counter()-start))