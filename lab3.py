import copy
a=[[0.000001,1,3],[2,0.000004,6],[3,6,7]]
a1=copy.deepcopy(a)
b=[5,11,23]
b1=copy.deepcopy(b)


n=len(a)
tolerance=10**(-8)
zero_pivot=10**(-6)

for i in range(0,n):
	for j in range(i+1,n):
		c=float(a[j][i])/a[i][i]
		for k in range(0,n):
			a[j][k]=a[j][k]-c*a[i][k]
		b[j]=b[j]-c*b[i]

x=[0]*n
i=n-1
while(i>=0):
	lhs=0
	for j in range(i,n):
		lhs=lhs+a[i][j]*x[j]
	x[i]=float(b[i]-lhs)/a[i][i]
	i=i-1
print x
#Checking:

for i in range(0,n):
	sum1=0
	for j in range(0,n):
		sum1=sum1+a1[i][j]*x[j]
	print sum1-b1[i]
	if (abs(sum1-b1[i])<=tolerance) :
		print 'Correct'
	else: print 'wrong'
