from cell import Cell
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self._x1 = x1
        self._y1 =y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []

      
        self._create_cells()
        

    def _create_cells(self):
     
   # cell logic for this would be x1, x1 + cell_sizex1, ect w y
        for i in range (self._num_cols):
            topcol = []
            for j in range (self._num_rows):
                topcol.append(Cell(self._win))
            self._cells.append(topcol)

        for i in range(self._num_cols):
            for j in range (self._num_rows):
                self._draw_cell(i,j)
    

        
        # make a list of columns for num cols
        # for every row, append a cell to the nested list 
        #upon completion, loop through completed matrix and use self._draw_cell

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        
        x1 = self._x1 + i * self._cell_size_x
        x2 = x1 + self._cell_size_x

        y1 = self._y1 + j * self._cell_size_y
        y2 = y1 + self._cell_size_y

        self._cells[i][j].draw(x1,y1,x2,y2)
        self._animate()


    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)
