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
	print(depurado_2)
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


#def schoening(clean_data, variables, code):



def main():
	data = readFile()
	clean_data, depurado = depurar(data)
	variables = getVariables(depurado)
	n = len(variables)
	code = getCode(n, variables)
	#schoening(clean_data, variables, code)


main()