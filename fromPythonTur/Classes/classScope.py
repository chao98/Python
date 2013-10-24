#!c:\Program Files (x86)\Python33\python.exe -tt

import sys

def scopeTest():
	print('>>> in scopeTest')
	print('==' * 10)

	def doLocal():
		print(' >> in scopeTest -> doLocal')
#		print('--' * 5)
		spam = 'local spam'
#		print('--' * 5)
		return

	def doNonlocal():
		print(' >> in scopeTest -> doNonlocal')
		nonlocal spam
		spam = 'nonlocal spam'
		return

	def doGlobal():
		print(' >> in scopeTest -> doGlobal')
		global spam
		spam = 'global spam'
		return

	spam = 'scopeTest spam'
	doLocal()
	print('After local assignment, spam = ', spam)

	doNonlocal()
	print('After nonlocal assignment, spam = ', spam)

	doGlobal()
	print('After global assignment, spam = ', spam)

	print('==' * 10)
	return

def main():

	scopeTest()
	print('in global scope, spam = ', spam)

	return

if __name__ == '__main__':
    main()
