import numpy as np

for i in range(250):
	b=[]
	a=np.loadtxt('cs_state%d.txt'%i)
	b.append(a[23])
	b.append(a[37])
	b.append(a[51])
	b.append(a[62])
	b.append(a[80])
	b.append(a[98])
	b.append(a[108])
	b.append(a[120])	
	b.append(a[134])
	b.append(a[151])
	b.append(a[166])
	b.append(a[180])
	b.append(a[195])
	b.append(a[208])
	b.append(a[225])
	b.append(a[7])
	b.append(a[24])
	b.append(a[38])
	b.append(a[52])
	b.append(a[63])
	b.append(a[82])
	b.append(a[99])
	b.append(a[109])
	b.append(a[121])
	b.append(a[135])
	b.append(a[152])
	b.append(a[167])
	b.append(a[181])
	b.append(a[196])
	b.append(a[209])
	b.append(a[226])
	np.savetxt('cs/cs_%d.txt'%i,b)
