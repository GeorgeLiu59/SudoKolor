#Pattern for a valid 3x3 solution
def pattern(r,c): 
    return (3*(r%3)+r//3+c)%9

#Random rows, cols, and numbers
from random import sample
def shuffle(s): 
    return sample(s,len(s)) 

#Generates a random puzzle
def generateBoard():
	rb = range(3) 
	rows  = [ g*3 + r for g in shuffle(rb) for r in shuffle(rb) ] 
	cols  = [ g*3 + c for g in shuffle(rb) for c in shuffle(rb) ]
	nums  = shuffle(range(1,3*3+1))

	board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]

	sq = 81
	em = sq * 3//4
	for p in sample(range(sq),em):
		board[p//9][p%9] = 0

	return board
