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
		print('Usage: insertsort.py inputfile outputfile')
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

#	print('Debug info: length = ', length)
#	print('Debug info: L = ', L)
#	print('='*50)

	for i in range(1, length):

		if L[i] < L[i-1]:
			m = L[i]

			j = i - 1
#			print('Debug info: i = ', i, 'j = ', j)
			while L[j] > m and j >= 0:
				L[j+1] = L[j]
				j = j - 1

			L[j+1] = m

#		print('Debug info: L = ', L, '\n')

	et2 = time.time()
	print('End time2 (insert sorting): ', et2, end = ';\t')
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
