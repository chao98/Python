import random
import pprint
import getopt
import sys

cmdline = True
cmdpara = 'o:g:r:c:'
operator = '+-*÷=()'

omsg = 'Oral questions'
gmsg = 'Guess questions'
rmsg = 'Recursion questions'
cmsg = 'Complex recursion questions'

oral = [#'a + b =', 'a - b =', 'a * b =', 
		'a.a + b.b =', 'a.a - b.b =', 
		'a.aa + b.bb =', 'a.aa - b.bb ='
		#'aa + b =', 'aa - b =', 
		'aa * b =', 'aa ÷ b =',
		'aa + bb =', 'aa - bb =',
		'aaa + bbb =', 'aaa + bb =', 'aaa - bb =', 'aaa ÷ b = ']

guess = ['aaa + bbb =', 'aaa - bb =', 'aa * b =', 'aaa * b =',
		 'aaa ÷ b =', 'aa * bb =', 'aaa ÷ bb =', 'aaaa ÷ bb =']

recur = ['aa + bb + cc =', 'aa + bb - cc =', 'aa + bb * cc =', 
		 'aa + bb ÷ c =', 'aa * bb ÷ c =',
		 'aaa + bb + cc =', 'aaa - bb + cc =', 'aaa * bb * cc =', 
		 'aaa ÷ bb ÷ cc =', 'aaa ÷ bb * cc =', 'aaa * bb ÷ cc =']

comrecur = ['aaa - ( bbb - cc ) =', 'aaa ÷ bb - ccc ÷ dd =', 
			'aa * bb + cc * dd =', 'aaa * bb - cc * ddd =']

def getInput(msg, num):

	while True:
		try:
			print('# of %s [default = %d]: ' % (msg, num), end = '')
			temp = input()
			if temp == '':
				break
			else:
				num = int(temp)
				break
		except ValueError as verr:
			pass

	return num

def getCmdInput(numtuple):
	try:
		opts, args = getopt.getopt(sys.argv[1:], cmdpara)
	except getopt.GetoptError as err:
		print('Usage: math -o xx -g xx -r xx -c xx')
		sys.exit()

	oralnum, guessnum, recursionnum, complexrecnum = numtuple

	for o, v in opts:
		if v != '':
			if o == '-o':
				oralnum = int(v)
			elif o == '-g':
				guessnum = int(v)
			elif o == '-r':
				recursionnum = int(v)
			elif o == '-c':
				complexrecnum = int(v)
			else:
				assert False, 'unhandled option'

	return (oralnum, guessnum, recursionnum, complexrecnum)

def getRandomQTemplateList(qtemplate, num):
	qtemplatelist = []
	for i in range(num):
		qtemplatelist.append(random.choice(qtemplate))

	return qtemplatelist

def randGen(opstr):
	if '.' not in opstr:
		l = len(opstr)
		result = random.randint(10**(l-1), 10**l-1)
	else:
		high, low = opstr.split('.')
		l = len(high)
		lowl = len(low)
		result = random.uniform(10**(l-1), 10**l-1)
		result = round(result, lowl)

	return str(result)

def genQ(q):
	oplist = q.split(' ')

	#pprint.pprint(oplist)
	for i, op in enumerate(oplist):
		if op not in operator:
			oplist[i] = randGen(op)

	return ' '.join(oplist)

def genMathQ(qtemplate, num):
	qtmplist = getRandomQTemplateList(qtemplate, num)

	qlist = []
	for q in qtmplist:
		qlist.append(genQ(q))

	return qlist

def qPrint(msg, qlist):
	emptyrow = 6
	inlinesep = '\t\t'

	print('>>> ', msg, ' >>>\n')
	if msg == omsg or msg == gmsg:
		offlinesep = '\n'*2
		column = 4
	elif msg == rmsg:
		offlinesep = '\n'*8
		column = 3
	else:
		offlinesep = '\n'*10
		column = 2		

	for i, q in enumerate(qlist):
		if (i+1) % column != 0:
			print('(%d) %s' % (i+1, q), end = inlinesep)
		else:
			print('(%d) %s' % (i+1, q), end = offlinesep)

	if (i+1) % column != 0:
		print('\n'*2)

	return

def main():
	oralnum, guessnum, recursionnum, complexrecnum = 20, 5, 15, 5

	# Get input to generate questions 
	if cmdline == False:
		oralnum = getInput(omsg, oralnum)
		guessnum = getInput(gmsg, guessnum)
		recursionnum = getInput(rmsg, recursion)
		complexrecnum = getInput(cmsg, complexrec)
	else:
		numtuple = (oralnum, guessnum, recursionnum, complexrecnum)
		oralnum, guessnum, recursionnum, complexrecnum = getCmdInput(numtuple)
	
	#print('oralnum = %d, guessnum = %d, recursion = %d, complexrec = %d' % (oralnum, guessnum, recursion, complexrec))

	qPrint(omsg, genMathQ(oral, oralnum))
	qPrint(gmsg, genMathQ(guess, guessnum))
	qPrint(rmsg, genMathQ(recur, recursionnum))
	qPrint(cmsg, genMathQ(comrecur, complexrecnum))

	return

if __name__ == '__main__':
	main()
