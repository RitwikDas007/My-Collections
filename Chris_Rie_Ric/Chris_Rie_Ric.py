print('\n Only non-zero component of christoffel symbols, Riemann tensors, Ricci tensors and Ricci scalar will be shown here.')
print('\n Input format must be like, ds**2 = A(dx**2) + B(dy**2) + .......\n')
print(' Here, A & B are the Metric components and x & y are the coordinates.\n')
print(" For Mathematical functions don't use numpy, just write the function e.g.")
print('\n\t Sine ---->> sin(x)')
print('\t Cosine ---->> cos(x)')
print('\t Tangent ---->> tan(x)')
print('\n Write other trigonomeric functions in terms of these functions.')
print('\n\t Logarithmic ---->> log(x)')
print('\t Exponential ---->> exp(x)')

import numpy as np
from sympy import *
from sympy.abc import *

d = int(input('\n Enter the numbers of the coordinates ---->> '))
print('\n Please define the coordinates :\n')

coor = []

for i in range(d) :
	e = input(' {0:g}-th element ---->> '.format(i))
	coor.append(e)

flag = input("\n Is the metric tensor diagonal ? Press 'y' for Yes and Press 'n' for No\t")
print('\n Please enter the components\n')

g = np.zeros((d,d),dtype = 'O')

if flag == 'n' :
	for i in range(d) :
		for j in range(d) :
			g[i][j] = input(' {0:g}{1:g}-th element ---->> '.format(i,j))

elif flag == 'y' :
	for i in range(d) :
		g[i][i] = input(' {0:g}{1:g}-th element ---->> '.format(i,i))


g = Matrix(g)
g_contra = g.inv()

print('\n')

def CS(i,j,k) :
	chri = 0
	for dummy in range(d) :
		val = (g_contra[i,dummy])*((diff(g[k,dummy], coor[j]) + diff(g[j,dummy], coor[k]) - diff(g[j,k], coor[dummy]))/2)
		chri = chri + val
	return chri

print('\n The Christoffel symbols are :\n')

for i in range(d) : 
	for j in range(d) :
		for k in range(d) :
			if not CS(i,j,k) == 0 :
				print('\t \u0393_({0:d},{1:d}{2:d}) = '.format(i,j,k), simplify((CS(i,j,k))))

print('\n')

def Riemann(i,j,k,m) :
	rie1 = 0
	rie2 = 0
	val = diff(CS(i,j,m), coor[k]) - diff(CS(i,j,k), coor[m])
	for dummy1 in range(d) :
		val1 = CS(i,dummy1,k)*CS(dummy1,j,m)
		rie1 = rie1 + val1
	for dummy2 in range(d) :
		val2 = CS(i,dummy2,m)*CS(dummy2,j,k)
		rie2 = rie2 + val2
	return val + rie1 - rie2

print(' The mixed Riemann tensors are :\n')

for i in range(d) : 
	for j in range(d) :
		for k in range(d) :
			for m in range(d) :
				if not Riemann(i,j,k,m) == 0 :
					print('\t R_({0:d},{1:d}{2:d}{3:d}) = '.format(i,j,k,m), simplify((Riemann(i,j,k,m))))

print('\n')

def Riemann_cov(i,j,k,m) :
	rie_cov = 0
	for dummy in range(d) :
		val_rie_cov = (g[i,dummy])*(Riemann(dummy,j,k,m))
		rie_cov = rie_cov + val_rie_cov
	return rie_cov

print(' The covarient form of Riemann tensors are :\n')

for i in range(d) : 
	for j in range(d) :
		for k in range(d) :
			for m in range(d) :
				if not Riemann_cov(i,j,k,m) == 0 :
					print('\t R_({0:d}{1:d}{2:d}{3:d}) = '.format(i,j,k,m), simplify((Riemann_cov(i,j,k,m))))

print('\n')

def Ricci(i,j) :
	ric = 0
	for dummy1 in range(d) :
		for dummy2 in range(d) :
			val_ric = (g_contra[dummy1,dummy2]) * (Riemann_cov(dummy1,i,dummy2,j))
			ric = ric + val_ric
	return ric

print(' The Ricci tensors are :\n')

for i in range(d) : 
	for j in range(d) :
		if not Ricci(i,j) == 0 :
			print('\t R_({0:d}{1:d}) = '.format(i,j), simplify(Ricci(i,j)))

print('\n')

R = 0
for dummy1 in range(d) :
	for dummy2 in range(d) :
		Ricci_sca = (g_contra[dummy1,dummy2]) * (Ricci(dummy1,dummy2))
		R = Ricci_sca + R

print('\n Ricci scalar : ', simplify(R),'\n')

