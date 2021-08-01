import sys
from .scr.core import *
from .scr.read import *

sys.path.append('/home/maruachi/temp/interpolation')

if len(sys.argv) == 1:
	print("head tail1 tail2 N tag")
	sys.exit()

scf_head = sys.argv[1]
scf_tail1 = sys.argv[2]
scf_tail2 = sys.argv[3]
N = int(sys.argv[4])
tag = sys.argv[5]

nat, head, spes, p1, p2 = read(scf_head, scf_tail1, scf_tail2).getValues()
interpolation(p1, p2, N, tag, nat, head, spes)
