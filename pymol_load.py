import pymol
from pymol import cmd 
import os

pymol.finish_launching()                

def main():
	cmd.load('t1.pdb')

	cmd.select('/t1/PSDO')
	# cmd.color('blue','t1')
	cmd.show('sphere', 't1')
	cmd.rotate ('z', -30, 't1', camera=1)
	cmd.create('t2', 't1')
	# cmd.color('red', 't2')
	cmd.select('/t2/PSDO')
	# cmd.color('yellow', 't2')
	cmd.show('sphere', 't2')
	cmd.translate([52.0769942809, 0, 0], 't2', camera=1)
	cmd.orient('t2')
	cmd.rotate('z', 60, 't2', camera=1)
	cmd.rotate('z', -30 )
	#this angle changes to bring involved pseudo atoms to horizontal positions
	cmd.rotate('y', 4.726, 't2', camera=1)
	cmd.rotate('x', 0.004, 't2', camera=1)
	# because we are rotating only one trimer, the 2 central pseudo atoms will not align. correction commands are:
	cmd.translate([0, -0.0440605685747639, -2.14176156973178], 't2', camera=1)
	cmd.alter('/t2//A', chain='D')
	cmd.alter('/t2//B', chain='E')
	cmd.alter('/t2//C', chain='F')
	cmd.save('2_trimerstest.pdb')
main()