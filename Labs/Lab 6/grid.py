# Grid
# Estimates unknown house values by taking average of neighboring houses
# Gives average and max values of houses in a neighborhood

def create_grid(filename):
    # creates a nested list based on file data
    # filename is type str and is the name of the file that contains the house price values
    file = open(filename,'r')
    data_str = file.read().splitlines()
    data = [int(num_str) for num_str in data_str]
    file.close()
    rows = data[0]
    cols = data[1]
    data_index = 2
    grid = []
    for row_index in range(rows):
        row=[]
        for col_index in range(cols):
            number = data[data_index]
            data_index = data_index + 1
            row.append(number)
        grid.append(row)
    return grid

def display_grid(grid):
    # displays the house price grid to the terminal
    # grid is type list and contains the housing pricing matrix
    for row_index in range(len(grid)):
        print('|  ', end='')
        for col_index in range(len(grid[0])):
            number = round(grid[row_index][col_index])
            print(number, ' |  ',end='')
        print()

def find_neighbors(row_index, col_index, grid):
    # finds the values of all the neighbors of a particular cell in the grid
    # grid is type list and contains the housing pricing matrix
    # row_index is type int and specificies a given row number
    # col_index is type int and specifies a given column number
    neighbors = []
    directions = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    for direction in directions:
        row = row_index + direction[0]
        col = col_index + direction[1]
        if row >= 0 and row < len(grid):
            if col >= 0 and col < len(grid[0]):
                neighbors.append(grid[row][col])
    return neighbors

def fill_gaps(grid):
    # creates a two-dimensional list with all zero cells replaced with the avg  of its neighbors
    # grid is type list and contains the housing pricing matrix
    new_grid = grid.copy()
    for row in range(len(new_grid)):
        for col in range(len(new_grid[0])):
            if new_grid[row][col] == 0:
                neighbors = find_neighbors(row,col,grid)
                avg = sum(neighbors)/len(neighbors)
                new_grid[row][col] = avg
    return new_grid

def find_max(grid):
    # finds and returns the maximum house value in all the cells in the grid
    # grid is type list and contains the housing pricing matrix
    maximum = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] > maximum:
                maximum = grid[row][col]
    return round(maximum)

def find_average(grid):
    # finds and returns the average hosue value in all cells in the grid
    # grid is type list and contains the housing pricing matrix
    total = 0
    for row in range(len(grid)):
        total = total + sum(grid[row])
    avg = total//(len(grid)*len(grid[0]))
    return avg
    
def main():
    # calls programs main functions and displays results
    grid = create_grid('data_2.txt')
    print('This is our grid:')
    display_grid(grid)
    print('\nThis is our newly calculated grid:')
    filled_grid = fill_gaps(grid)
    display_grid(filled_grid)
    print('\nSTATS')
    print('Average housing price in this area is: ' + str(find_average(grid)))
    print('Maximum housing price in this area is: ' + str(find_max(grid)))
    
main()

