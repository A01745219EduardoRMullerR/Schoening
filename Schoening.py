from random import randint

def readFile():
    file = open('3SAT.txt', 'r')
    lines = file.readlines()
    lines.pop(0)
    lines.pop(0)
    file.close()
    return lines

def depurar(lista):
    list2 = []
    for i in lista:
        a = list(i)
        a.pop(-1)
        if a[-1] == " ":
            a.pop(-1)
        b = "".join(a)
        list2.append(b)
    depurado = []
    for j in list2:
        k = j.strip('0')
        depurado.append(k)
    return depurado


def getVariables(clean_data):
    variables = []
    for element in clean_data:
        h = element.split(' ')
        if '' in h:
            h.remove('')
        for n in h:
            variables.append(int(n))
    return variables


def getCode(n, variables):
    code = {}
    maximum = int(max(variables))
    codenumber = bin(randint(0,2**maximum+1))
    codelist = list(codenumber)
    codelist.remove('0')
    codelist.remove('b')
    while len(codelist) < maximum:
        codelist.insert(0, '0')
    for i in range(20):
        code[i+1] = int(codelist[i])
    return code







def main():
    data = readFile()
    clean_data = depurar(data)
    variables = getVariables(clean_data)
    n = len(variables)
    code = getCode(n, variables)

    
main()