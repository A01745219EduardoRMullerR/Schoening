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
	codenumber = bin(randint(0,2**maximum+1))
	codelist = list(codenumber)
	codelist.remove('0')
	codelist.remove('b')
	while len(codelist) < maximum:
		codelist.insert(0, '0')
	for i in range(20):
		code[i+1] = int(codelist[i])
	return code


def schoening(clauses, variables, code):
	boolean_clauses = []
	for clause in clauses:
		boolean_clause = []
		for value in clause:
			x = code.get(abs(value))

			if x == 1:
				if value<0:
					boolean_clause.append(False)
				else:
					boolean_clause.append(True)
			elif x == 0:
				if value<0:
					boolean_clause.append(True)
				else:
					boolean_clause.append(False)
		boolean_clauses.append(boolean_clause)




def main():
	data = readFile()
	clauses, depurado = depurar(data)
	variables = getVariables(depurado)
	n = len(variables)
	code = getCode(n, variables)
	schoening(clauses, variables, code)


main()