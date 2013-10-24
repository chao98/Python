#!c:\Program Files (x86)\Python33\python.exe -tt

import sys

def catchException():
	print('>>>001, Inside catchException')
	print('--' * 5)

	while True:
		try:
			x = int(input('Please enter a integer: '))
		except ValueError:
			print('Oops! That was not a valid number, please try again, ')
		else:
			print('What we got is: {0:4d}'.format(x))
			break

	print('--' * 5)

	return

def raiseException():
	print('>>>002, Inside raiseException')
	print('--' * 5)

	try:
		raise Exception('Spam', 'Eggs')
	except Exception as inst:
		print('type of inst: ', type(inst))
		print('args of inst: ', inst.args)
		print('__str__() of inst: ',inst)

	print('--' * 5)
	return

def zeroFault():
	print(' >>003.1, Inside zeroFault')
	x = 1/0

	return

def handleZero():
	print('>>>003, Inside handleZero')
	print('--' * 5)

	try:
		zeroFault()
	except ZeroDivisionError as err:
		print('Type of err: ', type(err))
		print('Args of err: ', err.args)
		print('Handling run-time error: ', err)

	print('--' * 5)
	return

def notHandleException():
	print('>>>004, Inside notHandleException')
	print('--' * 5)

	try:
		raise NameError('Hi there')
	except NameError:
		print('An except flew by, while not handle it')
		raise

	print('--' * 5)
	return

class MyError(Exception):
	def __init__(self, value):
		self.value = value

	def __str__(self):
		return repr(self.value)

def handleMyError():
	print('>>>005, Inside handleMyError')
	print('--' * 5)

	try:
		raise MyError(2 * 2)
	except MyError as me:
		print('My exception occurred, value is: ', me)

	print('--' * 5)
	return

def main():
	catchException()
	print()

	raiseException()
	print()

	handleZero()
	print()

#	notHandleException()
#	print()

	handleMyError()
	print()
	
	return

if __name__ == '__main__':
    main()
