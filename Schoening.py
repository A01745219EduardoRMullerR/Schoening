from random import randint


def readFile():
    file = open('3SAT.txt', 'r')
    lines = file.readlines()
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
    depurado_2 = []
    for string in depurado:
        x = string.split(' ')

        if '' in x:
            x.remove('')

        clauses_int = []
        for a in x:
            y = int(a)
            clauses_int.append(y)
        depurado_2.append(clauses_int)
    return depurado_2, depurado


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
    codenumber = bin(randint(0, 2 ** maximum + 1))
    codelist = list(codenumber)
    codelist.remove('0')
    codelist.remove('b')
    while len(codelist) < maximum:
        codelist.insert(0, '0')
    for i in range(20):
        code[i + 1] = int(codelist[i])
    return code


def schoening(code, clauses):
    randomClausePosition = randint(0, len(clauses) - 1)
    randomClause = clauses[randomClausePosition]
    randomVariablePosition = randint(0, 2)
    randomVariable = randomClause[randomVariablePosition]
    randomVariable = abs(randomVariable)
    variableValue = code[randomVariable]

    if variableValue == 0:
        code[randomVariable] = 1
    else:
        code[randomVariable] = 0
    return code


def k_sat_instance(clauses, code):
    clauseList = []
    for clause in clauses:
        x = clause[0]
        y = clause[1]
        z = clause[2]

        xAbs = abs(x)
        yAbs = abs(y)
        zAbs = abs(z)

        xVal = code.get(xAbs)
        yVal = code.get(yAbs)
        zVal = code.get(zAbs)

        if xVal == 0:
            x *= -1
        if yVal == 0:
            y *= -1
        if zVal == 0:
            z *= -1

        x, y, z = x / xAbs, y / yAbs, z / zAbs

        if (x + y + z) < -2:
            clauseList.append(clause)
    return clauseList


def main():
    data = readFile()
    clauses, depurado = depurar(data)
    variables = getVariables(depurado)
    n = len(variables)
    code = getCode(n, variables)
    for n in range(0, (3 * len(variables))):
        negativeClauses = k_sat_instance(clauses, code)
        if len(negativeClauses) == 0:
            key = []
            for n in code:
                key.append(code[n])
            print("La clave que satisface el problema es: " + str(key))
            break
        code = schoening(code, negativeClauses)



main()
