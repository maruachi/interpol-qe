import re
import numpy as np

class read:
	def __init__(self, fhead, ftail1, ftail2):
		self.fhead = fhead
		self.nat = self.read_atm()
		self.head = self.read_head()
		self.spes = self.read_spes(ftail1)
		self.atoms1 = self.read_tail(ftail1)
		self.atoms2 = self.read_tail(ftail2)

	def read_atm(self):
		with open(self.fhead, 'r') as f:
			for line in f:
				if "nat" in line:
					return int(re.search("[0-9]+", line).group())

	def read_head(self):
		with open(self.fhead, 'r') as f:
			return f.readlines()
		
	def read_tail(self, filename):
		atoms = []
		with open(filename, 'r') as f:
			for line in f:
				if "ATOMIC_POSITIONS" in line:
					for _ in range(self.nat):
						line = f.readline()
						tmp = re.findall("[+-]?[0-9]+\.[0-9]+", line)
						atoms.append([float(x) for x in tmp])
		return atoms

	def read_spes(self, filename):
		spes = []
		with open(filename, 'r') as f:
			for line in f:
				if "ATOMIC_POSITIONS" in line:
					for _ in range(self.nat):
						line = f.readline()
						spe = re.match("[A-Za-z]+", line).group()
						spes.append(spe)
		return spes
	
	def getValues(self):
		return self.nat, self.head, self.spes, np.array(self.atoms1), np.array(self.atoms2)
	
def printAtoms(p):
	for x in p:
		print(x)
	print()
