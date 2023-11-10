from generator import generateBoard
from sudoku_board import SudokuBoard

timeList = []

for i in range(10000):
    
    bd = generateBoard()
    
    s = SudokuBoard(bd)
        
    s.solveGraphColoring()
    
    timeList.append(s.solveTime)
    print(f"Time Taken for {i+1}: {str(s.solveTime)}")
    
    del s
    
