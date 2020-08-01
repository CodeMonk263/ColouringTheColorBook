class Scan():
    ##Initializes all arrays and variables of class
    def __init__(self,origin,grid):    
        self.origin = origin
        self.grid = grid
        self.set_grid = []
        self.points = []
        self.visited = []
        self.lines = []
        self.count = 0

    ##Initializes the arrays according to the grid on screen
    def initializeArrays(self):                      
        for j in range(len(self.grid.getGrid())):
            self.set_grid.append([])
            self.visited.append([])
            for i in range(len(self.grid.getGrid()[j])):
                curr_pt = self.grid.getGrid()[i][j]
                if (curr_pt.getColor() == (0,0,0)):
                    self.set_grid[j].append(1)
                else:
                    self.set_grid[j].append(0)
                self.visited[j].append(0)

    ## DFS flood fill to detect all point to be coloured
    def dfs(self,x,y):           
        ## x - column
        ## y - row
        if (0 <= x < len(self.set_grid) and 0 <= y < len(self.set_grid[0]) and self.visited[x][y] == 0 and self.set_grid[y][x] == 0):
            self.visited[x][y] = 1
            self.points.append([y,x])
            self.count+=1
            self.dfs(x+1,y)
            self.dfs(x-1,y)
            self.dfs(x,y+1)
            self.dfs(x,y-1)

    ## Sorts the given array according to the given index of sub-array
    def Sort(self,sub_li,index):          
    # reverse = None (Sorts in Ascending order) 
    # key is set to sort using second element of  
    # sublist lambda has been used 
        sub_li.sort(key = lambda x: x[index]) 
        return sub_li 

    ## Main function to return list of lines to be coloured sorted by height and the left and right extreme coordinates
    def main(self):                       
        self.initializeArrays()
        self.dfs(self.origin.col,self.origin.row)
        self.points = self.Sort(self.points,1)
        self.points = self.Sort(self.points,0)
        right, left, height = 0,0,0
        first_pt = True
        for i in range(self.count):
            if (first_pt):
                first_pt = False
                height = self.points[i][0]
                left = self.points[i][1]
                right = self.points[i][1]
            elif (height != self.points[i][0] or right+1 != self.points[i][1]):
                self.lines.append([height,left,right])
                height = self.points[i][0]
                left = self.points[i][1]
                right = self.points[i][1]
            else:
                right+=1

            if (i == self.count-1):
                self.lines.append([height,left,right])

        return self.lines


