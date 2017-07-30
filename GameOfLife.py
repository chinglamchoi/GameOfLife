the_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
dc = 0 #dc == alive neighbouring cells next to dead cell
ac = 0 #ac == alive neighbouring cells next to alive cell
m = 1  #m is thelist[X][?]
n = 1  #n is thelist[?][X]
g = m + 1
h = n + 1
j = m - 1
k = n -1
cell = the_list[n][m]

while n > 0 and n < 10: # wrong or not...
    while m > 0 and m < 10: #need to add exception for when cell doesn't have neighbours +
        if cell == 0: # if cell == dead, check neighbours
            if the_list[n][g] == 1: #when code is run: outputs "IndexError: list index out of range"
                dc = dc + 1 
            if the_list[n][j] == 1:
                dc = dc + 1
            if the_list[h][m] == 1:
                dc = dc + 1
            if the_list[h][g] == 1:
                dc = dc + 1
            if the_list[h][j] == 1:
                dc = dc + 1
            if the_list[k][m] == 1:
                dc = dc + 1
            if the_list[k][g] == 1:
                dc = dc + 1
            if the_list[k][j] == 1:
                dc = dc + 1
            if dc == 3: # if == 3 neighbours, revive
                cell = 1
        elif cell == 1: # if cell == alive, check neighbours
            if the_list[n][g] == 1:
                ac = ac + 1 
            if the_list[n][j] == 1:
                ac = ac + 1
            if the_list[h][m] == 1:
                ac = ac + 1
            if the_list[h][g] == 1:
                ac = ac + 1
            if the_list[h][j] == 1:
                ac = ac + 1
            if the_list[k][m] == 1:
                ac = ac + 1
            if the_list[k][g] == 1:
                ac = ac + 1
            if the_list[k][j] == 1:
                ac = ac + 1
            if ac != 2 and ac != 3: # if alive neighbours != both 2 and 3, cell is dead
                cell = 0
        m = m + 1 #checks next value in the_list[n]
    n = n + 1







#might need to use this as function... def niceprint(the_list):
#count = 0
#for i in the_list:
#    print(the_list[count])
#    count = count + 1



        
            
