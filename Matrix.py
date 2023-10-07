import numpy as np

m = int(input('Enter row number of A matrix\t'))
n = int(input('Enter column number of A matrix\t'))

p = int(input('Enter row number of B matrix\t'))
q = int(input('Enter column number of B matrix\t'))

a = np.zeros((m,n))
b = np.zeros((p,q))
c = []
d = []
e = []
flag1 = 0
flag2 = 0

print('Enter values for A matrix \n')

for i in range(m):
	for j in range(n):
		a[i][j] = float(input('Enter {0:d}{1:d}-th element\t'.format(i,j)))

print('\nEnter values for B matrix \n')

for i in range(p):
	for j in range(q):
		b[i][j] = float(input('Enter {0:d}{1:d}-th element\t'.format(i,j)))

print('\nA = \n',a)
print('\nB = \n',b)

for i in range(m) :
	for j in range(q) :
		if m == p and n == q :
			flag1 = 1
			Add = a[i][j] + b[i][j]
			c.append(Add)
		for k in range(p) :
			if n == p :
				flag2 = 1	
				Mul = a[i][k] * b[k][j]
				d.append(Mul)
		e.append(sum(d))
		d.clear()

if flag1 == 1 :
	x = np.array(c)
	x.resize(m,n)
	print('\nAddition = \n',x)
else :
	print('\nAddition is not possible')


if flag2 == 1 :
	y = np.array(e)
	y.resize(m,q)
	print('\nMultiplication (AB) = \n',y)
else :
	print('\nMultiplication is not possible')

