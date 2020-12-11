
#1/usr/bin/python

def DecimalToBinary(n):
	if n > 1:
		DecimalToBinary(n / 2)
	print n % 2,

def DecimalToOctal(n):
	if n < 1:
		print n, 'o',
	else:
		DecimalToOctal(n / 8)
		print n % 8,

def DecimalToHex(n):
	if (n < 1):
		print n,'x',
	else:
		DecimalToHex(n / 16)
		x = (n % 16)
		if(x < 10):
			print x,
		if(x == 10):
			print 'A',
		if(x == 11):
			print 'B',
		if(x == 12):
			print 'c',
		if(x == 13):
			print 'D',
		if(x == 14):
			print 'E',
		if(x == 15):
			print 'F',

if __name__ == '__main__':
	num = int(raw_input('enter number to be formatted '))

	print 'Decimal Value: ',num,

	print '  Binary Value: ',
	DecimalToBinary(num)

	print '  Octal Value: ',
	DecimalToOctal(num)

	print '  Hex Value: ',
	DecimalToHex(num)
