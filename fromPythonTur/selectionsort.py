#!c:\Program Files (x86)\Python33\python.exe -tt

import sys
import random
import time

def swap(L, i, j):
	temp = L[j]
	L[j] = L[i]
	L[i] = temp

def main():
	if len(sys.argv) < 3:
		print('Usage: selectionsort.py inputfile outputfile')
		sys.exit(1)
	
	fileopen = open(sys.argv[1], 'r')

	st = time.time()
	print('Start time: ', st)
	
	line = fileopen.read()
	L = line.split(';')
	fileopen.close()
	L.pop()

	et1 = time.time()
	print('End time1 (reading file, generating list): ', et1, end = ';\t')
	print('Durtime: ', (et1 -st))

	length = len(L)

	for i in range(length):
		mark = i

		for j in range(i+1, length):
			if (L[mark] > L[j]):
				mark = j

		if mark != i:
			swap(L, i, mark)
		
	et2 = time.time()
	print('End time2 (selection sorting): ', et2, end = ';\t')
	print('Durtime: ', (et2 -et1))

	fileopen = open(sys.argv[2], 'w')

	for i in range(length):
		fileopen.write(L[i])
		fileopen.write(';')

	fileopen.close()

	et3 = time.time()
	print('End time3 (Writing file): ', et3, end = ';\t')
	print('Durtime: ', (et3 -et2))

	return

if __name__ == '__main__':
    main()
