import copy
def main():
	a,b=input_module()
	a1,b1,n,pivot_zero,tol1,tol2,tol3,converge=setup(a,b)
	consistent=True	
	if (converge==True):
		x=work1(n,a1,b1)

	else:
		x=work(n,a,b,pivot_zero)
		if (x[0]=='x'):
			consistent=False
			tolerances=[]
			output(x,tolerances,converge,consistent)
			return 0
			
	tolerances=analysis(n,a1,b1,x,tol1,tol2,tol3)
	output(x,tolerances,converge,consistent)

def input_module():
	a=[]
	b=[]

	#first line must have no. of equations
	# each of the next n lines must have rows of matrix a
	# next n lines must have values of marix b
	input1=open('input','r')
	n=int(input1.readline())
	
	for i in range(0,n):
		a.append([])
		string=input1.readline()
		a[i]=[float(x) for x in string.split()]
	for i in range(0,n):
		string=input1.readline()
		b.append(float(string))
	input1.close()

	return (a,b)
	
	
def setup(a,b):
	a1=copy.deepcopy(a)
	b1=copy.deepcopy(b)
	n=len(a)
	pivot_zero=10**(-6)    #for pivot element
	tol1=10**(-8)
	tol2=10**(-4)
	tol3=10**(-2)

	#Check if the iterative method will diverge or converge
	converge=True
	flag=0
	for i in range(0,n):
		flag2=0
		for j in range(0,n):
			if (a[i][i]<a[i][j]):	
				flag=1
				break
			if(a[i][i]>a[i][j]):
				flag2=1
				
		if (flag==1):
			converge=False
			break
		if (flag2==0):
			converge=False
			break
	
	return (a1,b1,n,pivot_zero,tol1,tol2,tol3,converge)

def work(n,a,b,pivot_zero):

	#triangulisation of matix
	
	for i in range(0,n):
		
		#finding max pivot element
		maximum=a[i][i]
		max_index=i
		for index in range(i,n):
			if (a[index][i]>maximum):
				max_index=index
				maximum=a[index][i]
		#max found
		
		#reordering equations for a good pivot term
		if (max_index!=i):
			for i1 in range(i,n):
				temp1=a[max_index][i1]	
				a[max_index][i1]=a[i][i1]
				a[i][i1]=temp1
			
			temp2= b[max_index]
			b[max_index]=b[i]
			b[i]=temp2
					
		#reordering done
		
		for j in range(i+1,n):
			c=float(a[j][i])/a[i][i]
			for k in range(i,n):
				a[j][k]=a[j][k]-c*a[i][k]
			b[j]=b[j]-c*b[i]

	#triangularization done
	determinant=1
	for i in range(0,n):
		determinant=determinant*a[i][i]
	if (determinant<=10**(-16)):
		return ['x']
	#back substitution
	x=[0]*n
	i=n-1
	while(i>=0):
		lhs=0
		for j in range(i,n):
			lhs=lhs+a[i][j]*x[j]
		x[i]=float(b[i]-lhs)/a[i][i]
		i=i-1
	return x

#guass sidel method

def work1(n,a,b):
	iterations=25
	x1=[0]*n
	for iterations in range(0,iterations):
		big=0
		for i in range(0,n):
			sum1=0
			for j in range(0,n):
				if (j!=i): sum1=sum1+a[i][j]*x1[j]
			temp=float(b[i]-sum1)/a[i][i]
			relerror=abs(float((x1[i]-temp))/temp)
			if (relerror>big): big=relerror
			x1[i]=temp	
	return x1	
	
	

def analysis(n,a1,b1,x,tol1,tol2,tol3):
	tolerances=[]
	for i in range(0,n):
		sum1=0
		for j in range(0,n):
			sum1=sum1+a1[i][j]*x[j]
		r=abs(float(sum1-b1[i])/sum1)
		if (r<=tol1): tolerances.append(tol1)
		elif (r<=tol2): tolerances.append(tol2)
		elif (r<=tol3): tolerances.append(tol3)
		else: tolerances.append('Bad result')
	return tolerances


def output(x,tolerances,converge,consistent):
	output=open('output','w')
	if (consistent==True):
		if (converge==True): output.write('Gauss Sidel Iteration Used\n')
		else: output.write('Gauss Elimination used\n')
		output.write('x\n\n')
		for i in range(0,len(x)):
			output.write(str(x[i])+'\n')
		output.write('\n\nTolerances\n\n')
		for i in range(0,len(x)):
			output.write(str(tolerances[i])+'\n')
	output.close()
	
main()	
