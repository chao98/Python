import random

opers = '+-*=()[]÷'
quetemplist = [ 'aaa ÷ bb =', 'aaaa ÷ bb =', 'aaaa ÷ bbb =',
				'aaaaa ÷ bb =', 'aaaaa ÷ bbb ='
				#'(aaa - bb) ÷ cc ='
				]

def findDivisor(n, m):
	divisors = []

	for i in range(2, n//2):
		if n % i == 0:
			divisors.append(i)

	if len(divisors) == 0:
		return -1
	else:
		d = []
		for v in divisors:
			if len(str(v)) == m:
				d.append(v)

		return -1 if len(d) == 0 else random.choice(d)

def parseQ(qStr):
	oplist = qStr.split()

	for i, op in enumerate(oplist):
		if i == 0:
			oplist[i] = str(genRandInt(len(op)))
		elif op not in opers and oplist[i-1] == '÷':
			divisor = findDivisor(int(oplist[i-2]), len(op))
			if divisor != -1:
				oplist[i] = str(divisor)
			else:
				return 'find Primer number'

	return ' '.join(oplist)

def genRandInt(l):

	return random.randint(10**(l-1), 10**l-1)

def genRandQeslist(qtmplist, n):
	qlist = []
	for i in range(n):
		qlist.append(random.choice(qtmplist))

	return qlist

def main():
	n = 20
	qlist = genRandQeslist(quetemplist, n)
	#print(qlist)

	#l, m = 3, 2
	#for i in range(n):
	#	divided = genRandInt(l)
	#	divisor = findDivisor(divided, m)
	#	if divisor != -1:
	#		print('%d ÷ %d = ' % (divided, divisor))

	for q in qlist:
		print(parseQ(q))

	return

if __name__ == '__main__':
	main()

