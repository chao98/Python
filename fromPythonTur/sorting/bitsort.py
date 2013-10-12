#!c:\Program Files (x86)\Python33\python.exe -tt

import sys
import time

BASE = 16

def max(L):
	m = 0
	for i in range(len(L)):
		if m < L[i]:
			m = L[i]

	return m

def getpos(n):
	lpos = 0
	bpos = 0

	lpos = n // BASE
	bpos = n - lpos * BASE

	return (lpos, bpos)

def setpos(bitL, lpos, bpos):
	baseL = list(range(BASE))
	for i in range(BASE):
		baseL[i] = 2 ** (BASE - i - 1)

	bitL[lpos] = bitL[lpos] | baseL[bpos]

	return

def getsortedL(n, lpos):
	sortedsubL = []
	baseL = list(range(BASE))
	for i in range(BASE):
		baseL[i] = 2 ** (BASE - i - 1)

	for i in range(BASE):
		if (n & baseL[i]) != 0:
			sortedsubL.append(lpos * BASE + i)

	return sortedsubL

def main():
	if len(sys.argv) < 3:
		print('Usage: bitsort.py inputfile outputfile')
		sys.exit(1)
	
	fileopen = open(sys.argv[1], 'r')

	st = time.time()
	print('Start time: ', st)
	
	line = fileopen.read()
	L = line.split(';')
	fileopen.close()
	L.pop()
	for i in range(len(L)):
		L[i] = int(L[i])

	et1 = time.time()
	print('End time1 (reading file, generating list): ', et1, end = ';\t')
	print('Durtime: ', (et1 -st))

	bitL = list(range(max(L) // BASE + 1))

	for i in range(len(bitL)):
		bitL[i] = 0

	for i in range(len(L)):
		(lpos, bpos) = getpos(L[i])
		setpos(bitL, lpos, bpos)

	sortedL = []
	for i in range(len(bitL)):
		sortedL.extend(getsortedL(bitL[i], i))
		
	et2 = time.time()
	print('End time2 (bit sorting): ', et2, end = ';\t')
	print('Durtime: ', (et2 -et1))

	fileopen = open(sys.argv[2], 'w')

	for i in range(len(sortedL)):
		if sortedL[i] != 0:
			fileopen.write(str(sortedL[i]))
			fileopen.write(';')

	fileopen.close()

	et3 = time.time()
	print('End time3 (Writing file): ', et3, end = ';\t')
	print('Durtime: ', (et3 -et2))

	return

if __name__ == '__main__':
    main()
