b=[]
t=('prem', 'rani', 'ravi', 'rani', 'seema', 'prem', 'rani')
for i in (t):
	if t.count(i)>1:
		if i not in b:
			b.append(i)
print(b)
