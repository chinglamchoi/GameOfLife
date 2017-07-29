the_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
dc = 0 #dc == alive neighbouring cells next to dead cell
ac = 0 #ac == alive neighbouring cells next to alive cell
m = 0  #m is thelist[X][?]
n = 0  #n is thelist[?][X]
# unecessary: noofn = len(the_list) #checks no. of arrays in list
# unecessary: noofm = len(the_list[0]) # checks the no. of values in each array


for i in range(12): # wrong or not...
    for j in range(12): #need to add exception for when cell doesn't have neighbours +
        if the_list[n][m] == 0: # if cell == dead, check neighbours
            if the_list[n][m+1] == 1: #when code is run: outputs "IndexError: list index out of range"
                dc = dc + 1 
            if the_list[n][m-1] == 1:
                dc = dc + 1
            if the_list[n+1][m] == 1:
                dc = dc + 1
            if the_list[n+1][m+1] == 1:
                dc = dc + 1
            if the_list[n+1][m-1] == 1:
                dc = dc + 1
            if the_list[n-1][m] == 1:
                dc = dc + 1
            if the_list[n-1][m+1] == 1:
                dc = dc + 1
            if the_list[n-1][m-1] == 1:
                dc = dc + 1
                if dc == 3: # if == 3 neighbours, revive
                    the_list[n][m] = 1
        elif the_list[n][m] == 1: # if cell == alive, check neighbours
            if the_list[n][m+1] == 1:
                ac = ac + 1 
            if the_list[n][m-1] == 1:
                ac = ac + 1
            if the_list[n+1][m] == 1:
                ac = ac + 1
            if the_list[n+1][m+1] == 1:
                ac = ac + 1
            if the_list[n+1][m-1] == 1:
                ac = ac + 1
            if the_list[n-1][m] == 1:
                ac = ac + 1
            if the_list[n-1][m+1] == 1:
                ac = ac + 1
            if the_list[n-1][m-1] == 1:
                ac = ac + 1
                if ac != 2 and ac != 3: # if alive neighbours != both 2 and 3, cell is dead
                    the_list[n][m] = 0
            m = m + 1 #checks next value in the_list[n]
        n = n + 1







#might need to use this as function... def niceprint(the_list):
#count = 0
#for i in the_list:
#    print(the_list[count])
#    count = count + 1



        
            
