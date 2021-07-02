n=int(input())
p=1
while(n):
	r=n%10
	p*=r
	print(p,'*',r,'=', p*r)
	n=n//10
print(p)