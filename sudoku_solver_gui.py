from tkinter import *
from sudoku_board import SudokuBoard
import time

root = Tk()
root.title("Sudoku Solver with Graph Coloring")
root.geometry("324x400")

errLabel = Label(root, text = "", fg = "red")
errLabel.grid(row = 15, column = 1, columnspan = 10, pady = 5)

solvedLabel = Label(root, text = "", fg = "green")
solvedLabel.grid(row = 15, column = 1, columnspan = 10, pady = 5)

cells = {}

def ValidateInput(inp):
    out = (inp.isdigit() or inp == "") and len(inp)< 2
    return out

reg = root.register(ValidateInput)

def drawSmallGrid(row, column, bgcolor):
    for i in range(3):
        for j in range(3):
            e = Entry(root, width = 5, bg = bgcolor, justify = "center", validate = "key", validatecommand = (reg,"%P"))
            
            e.grid(row = row+i+1, column = column + j + 1, sticky = "nsew", padx = 1, pady = 1, ipady = 5)
            
            cells[(row+i+1, column+j+1)] = e

def drawBigGrid():
    color = "#dae2f5"
    
    for rowNo in range (1,10,3):
        for colNo in range(0,9,3):
            drawSmallGrid(rowNo, colNo, color) 
            if (color == "#dae2f5"):
                color = "#f5eeda"
            else: 
                color = "#dae2f5"
                
def clearValues():
    errLabel.configure(text = "")
    solvedLabel.configure(text = "")
    
    for row in range(2,11):
        for col in range(1,10):
            cell = cells[(row,col)]
            cell.delete(0,"end")
        
def solveBoard():
    board = []
    errLabel.configure(text = "")
    solvedLabel.configure(text = "")
    for row in range(2,11):
        rows = []
        for col in range(1,10):
            val = cells[(row,col)].get()
            if val == "":
                rows.append(0)
            else: 
                rows.append(int(val))
    
        board.append(rows)
        
    s = SudokuBoard(board)
    
    start = time.time()
    s.solveGraphColoring(m=9)
    end = time.time()
    
    solvedLabel.configure(text = f"Operation took {str(round(end-start,4))} sec")
                
    for row in range(2,11):
        for col in range(1,10):
            cells[(row,col)].insert("end", s.board[row-2][col-1])
    
btn = Button(root, command = solveBoard, text = "Solve", width = 10)
btn.grid(row = 20, column = 1, columnspan = 5, pady = 20)

btn = Button(root, command = clearValues, text = "Clear", width = 10)
btn.grid(row = 20, column = 5, columnspan = 5, pady = 20)

drawBigGrid()
root.mainloop()
