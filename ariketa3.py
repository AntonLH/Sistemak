import random 
num = random.randrange(1,100)
bool=True
while bool!=False:
	num2= input('introduce num')
	if num2>num:
		print('txikiagoa')
	elif num2<num:
		print('handiagoa')
	else:
		print('oso ondo')
		bool=False

