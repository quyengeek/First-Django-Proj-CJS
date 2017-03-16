for x in range(30, 301):
	if (x%7==0) and (x%13==0):
		print('a-z')
	elif (x%7==0):
		print('abc')
	elif (x%13==0):
		print ('xyz')
	else:
		print (x)
