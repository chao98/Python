#!c:\Program Files (x86)\Python33\python.exe -tt

import sys
import random
import time

def swap(L, i, j):
	temp = L[j]
	L[j] = L[i]
	L[i] = temp

def partition(L, low, high):
	pivotkey = L[low]

	while(low < high):
		while (low < high) and (L[high] >= pivotkey):
			high = high - 1

		swap(L, low, high)

		while (low < high) and (L[low] <= pivotkey):
			low = low + 1

		swap(L, low, high)

	return low

def qsort(L, low, high):
	pivot = 0

	if low < high:
		pivot = partition(L, low, high)

		qsort(L, low, pivot-1)
		qsort(L, pivot+1, high)


def main():
	if len(sys.argv) < 3:
		print('Usage: quicksort.py inputfile outputfile')
		sys.exit(1)
	
	fileopen = open(sys.argv[1], 'r')

	st = time.time()
	print('Start time: ', st)
	
	line = fileopen.read()
	L = line.split(';')
	fileopen.close()

	et1 = time.time()
	print('End time1 (reading file, generating list): ', et1, end = ';\t')
	print('Durtime: ', (et1 -st))

	length = len(L)

	qsort(L, 0, length-1)

	et2 = time.time()
	print('End time2 (bubble sorting): ', et2, end = ';\t')
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
