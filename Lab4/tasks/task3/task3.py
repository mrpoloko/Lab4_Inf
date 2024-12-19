
import re

xml_file = open("../data/XML1.txt", encoding='utf-8', mode='r')
json_file = open("../data/JSON1.json", encoding='utf-8', mode='r')

xml_file.readline()
r = xml_file.readline()
def preParse(r):
    r = re.sub(r'<(\w+)([^/]*)/>', r'<\1\2></\1>', r)

    while re.search(r'<(\w+)\s(\w+)="(\w+)"(.*)>',r) is not None:
        r = re.sub(r'<(\w+)\s(\w+)="(\w+)"(.*)>', r'<\1\4>\n<_\2>\3</_\2>',r)
    return r

def withOutKeys(r):
    pattern = re.compile(r'<(\w+)>(.*?)</\1>', re.DOTALL)
    for match in pattern.finditer(r):  # находим сами ключи и содержимое  # ключ
        value = match.group(2).strip()
    return parse(value)

def parse(r) -> dict:

    pattern = re.compile(r'<(\w+)>(.*?)</\1>', re.DOTALL) #проходимся по всему файлу хмл и ищем ключи и содержимое dotall позволяет захватывать символы другой строки
    dict = {}

    for match in pattern.finditer(r): #находим сами ключи и содержимое
        key = match.group(1) #ключ
        value = match.group(2).strip() #содержимое
        if key in dict.keys():
            dict[key] = [dict[key], withOutKeys(value)]
        elif re.search(r'<\w+>', value): # проверяем является ли содержимое новым ключем
            dict[key] = parse(value)
        else:
            dict[key] = value
    return dict

def printjson(json:dict, tabs, json_file):
    flag = 1
    for key in json.keys():
        element = json[key]
        if flag != 1:
            print(',')
            json_file.write(',' + '\n')
        flag = 0
        if isinstance(element, dict):
            print('\t'*tabs+f'"{key}":' + '{')
            json_file.write('\t'*tabs+f'"{key}":' + '{' + '\n')
            printjson(element,tabs+1, json_file)
            print('\n'+'\t'*tabs+'}', end='')
            json_file.write('\n'+'\t'*tabs+'}')
        elif isinstance(element, list):
            flag2 = 1
            print('\t' * tabs + f'"{key}":' + '[{')
            json_file.write('\t' * tabs + f'"{key}":' + '[{' + '\n')
            for elem in element:
                if flag2 != 1:
                    print(',')
                    json_file.write(',' + '\n')
                flag2 = 0
                if isinstance(elem, dict):
                    printjson(elem, tabs + 1, json_file)
                    print('\n' + '\t' * tabs + '}', end='')
                    json_file.write('\n' + '\t' * tabs + '}')
                else:
                    print('\t' * tabs + f'"{key}":' + f'"{element}"', end='')
                    json_file.write('\t' * tabs + f'"{key}":' + f'"{element}"')
            print(']', end='')
            json_file.write(']')
        else:
            print('\t'*tabs+f'"{key}":' + f'"{element}"', end='')
            json_file.write('\t'*tabs+f'"{key}":' + f'"{element}"')
