import time


def xmltojson(string):
    array = string.replace('<', '\n"').replace('>', '":\n').replace('\t', '').split('\n')
    for i in range(len(array)):
        if ' ' in array[i]:
            if array[i][0] == ' ':
                array[i] = ''

    while '' in array:
        array.remove('')
    i = 0
    # print(array)
    while i < len(array):
        if array[i][1] == '/':
            array[i] = '}'
        elif array[i][len(array[i]) - 1] == ':':
            match array[i + 1][len(array[i + 1]) - 1]:
                case ':':
                    array[i] += ' {'
                case _:
                    array[i] += '"' + array[i + 1] + '"'
                    del array[i + 1:i + 3]
        i += 1

    for i in range(len(array) - 1):
        if array[i + 1][0] != '}' and array[i][-1] != '{':
            array[i] += ','
    return array

def printjson(array):
    sdvig = 0
    for i in range(len(array)):
        if '}' in array[i]:
            sdvig -= 1
        print('\t' * sdvig + array[i])
        w.write('\t' * sdvig + array[i] + '\n')
        if array[i][-1] == '{':
            sdvig += 1

start=time.perf_counter()
for i in range(0,100):
    r = open('../data/XML.txt', encoding='utf-8', mode='r')
    w = open('../data/JSON.json', encoding='utf-8', mode='w')
    r.readline()
    string = r.read()

    array = xmltojson(string)

    printjson(array)
    r.close()
    w.close()
print((time.perf_counter()-start))