#!c:\Program Files (x86)\Python33\python.exe -tt

import sys
import random
import time

def main():
	if len(sys.argv) < 3:
		print('Usage: randgen.py num filename')
		sys.exit(1)

	loopend = int(sys.argv[1])
	low = 999999
	high = 10000000
	if (high - low) <= loopend:
		print('Unable to generate none-repeatable random numbers')
		sys.exit(1)

	randset = set()
	
	st = time.time()
	print('Start time: ', st)

	i = 0
	while len(randset) < loopend:
		m = random.randrange(low, high)
		i = i + 1
		if m != 0:
			randset.add(m)

	print('# of generation: ', i, '; % = ', (i - loopend) / loopend * 100)
	et1 = time.time()
	print('End time1 (Gen', loopend, 'random data): ', et1, end = ';\t')
	print('Durtime: ', (et1 -st))

	file = open(sys.argv[2], 'w')

	i = 0
	while i < len(randset):
		file.write(str(randset.pop()))
		file.write(';')
		i = i + 1

	file.close()

	et2 = time.time()
	print('End time2 (Write', loopend, 'random data into file): ', et2, end = ';\t')
	print('Durtime: ', (et2 -et1))

	return

if __name__ == '__main__':
    main()
