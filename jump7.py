a=0
while a<100:
	a+=1
	if a%7==0:
		continue
	elif a//10==7 or a%10==7:
		continue
	else:
		print(a)
		print('\n')

