import numpy as np

def makeSCF(p, filename, nat, head, spes):
	with open(filename, 'w') as f:
		for line in head:
			f.write(line)
		f.write("ATOMIC_POSITIONS (crystal)\n")
		for i in range(nat):
			f.write(spes[i])
			for c in p[i]:
				f.write("   " + str(c))
			f.write("\n")

def interpolation(p1, p2, N, tag, nat, head, spes):
	dis = p2 - p1
	q = dis/(N+1)
	for i in range(N+2):
		makeSCF(p1+q*i, tag+str(i)+ ".in", nat, head, spes)
		makeSCF(p1-q*i, "_"+tag+str(i)+ ".in", nat, head, spes)
