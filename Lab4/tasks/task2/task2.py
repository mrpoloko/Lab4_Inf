import re


def checkXML(string):
    begin = string.count(r'<.*>') - string.count(r'<.*\\>')
    end = string.count(r'<\.*>')
    return begin != end

def parse(r) -> dict:

    pattern = re.compile(r'<(\w+)>(.*?)</\1>', re.DOTALL) #проходимся по всему файлу хмл и ищем ключи и содержимое dotall позволяет захватывать символы другой строки
    dict = {}

    for match in pattern.finditer(r): #находим сами ключи и содержимое
        key = match.group(1) #ключ
        value = match.group(2).strip() #содержимое
        if re.search(r'<\w+>', value): # проверяем является ли содержимое новым ключем
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
        else:
            print('\t'*tabs+f'"{key}":' + f'"{element}"', end='')
            json_file.write('\t'*tabs+f'"{key}":' + f'"{element}"')

