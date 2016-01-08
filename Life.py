import Tkinter
import time

top=Tkinter.Tk()
C=Tkinter.Canvas(top,height=500,width=500)
C.pack()

def create_board(width,height):
    return [[False] * width for _ in range(height)]


def add_point(x,y,board):
    board[x][y] = True
    return board

def print_grid(board):
    for row in board:
        for col in row:
            if col:
                print 'X',
            else:
                print '_',
        print ''
    print ''

def draw_grid(board):
    C.delete("all")
    x = 0
    for row in board:
        y = 0
        for col in row:
            if col:
                C.create_rectangle(x,y,x+10,y+10,fill="black")
            y += 10
        x += 10


def in_board(x,y,board):
    return 0 <= x < len(board) and 0 <= y < len(board[x])

def check_neighbors(x,y,board):
    neighbor = 0
    xcount = x-1
    while xcount <= x+1:
        ycount = y-1
        while ycount <= y+1:
            if xcount == x and ycount == y:
                ycount += 1
                continue
            if in_board(xcount,ycount,board) and board[xcount][ycount]:
                neighbor += 1
            ycount += 1
        xcount += 1
    return neighbor

def next_evolve(board):
    new_board = [[False]*len(board) for _ in board[0]]
    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] and 2 <= check_neighbors(x,y,board) <= 3:
                new_board[x][y] = True
            elif not board[x][y] and check_neighbors(x,y,board) == 3:
                new_board[x][y] = True
    return new_board

def empty(board):
    for row in board:
        for col in row:
            if col:
                return False
    return True


board = create_board(100,100)
board = add_point(2,0,board)
board = add_point(2,1,board)
board = add_point(2,2,board)
board = add_point(1,2,board)
board = add_point(0,1,board)

board = add_point(20,20,board)
board = add_point(21,20,board)
board = add_point(20,21,board)
board = add_point(21,21,board)




for i in range(1000):
    #print_grid(board)
    draw_grid(board)
    board = next_evolve(board)
    time.sleep(.05)
    top.update()
    if empty(board):
        break
top.mainloop()
