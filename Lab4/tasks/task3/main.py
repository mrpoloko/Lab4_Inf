from task3 import preParse, parse, printjson
from tasks.task2.task2 import printjson as pj
import time

start=time.perf_counter()
for i in range(0,100):
    xml_file = open("../data/XML1.txt", encoding='utf-8', mode='r')
    json_file = open("../data/JSON3.json", encoding='utf-8', mode='w')

    xml_file.readline()
    r = xml_file.read()

    r = preParse(r)
    printjson(parse(r), 0, json_file)
    xml_file.close()
    json_file.close()
print((time.perf_counter()-start))