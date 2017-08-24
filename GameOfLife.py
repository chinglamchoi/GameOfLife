the_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

the_other_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
dc = 0
ac = 0
m = 1
n = 1
count = 0
count2 = 0
count3 = 0
for i in the_list:
    print(the_list[count2])
    count2 = count2 + 1
print("")
    
while True:
    count = 0
    count3 = 0
    for n in range(1,10):
        k = n - 1
        h = n + 1
        for m in range(1,10):
            dc = 0
            ac = 0
            g = m + 1
            j = m - 1
            cell = the_list[n][m]
            if the_list[n][m] == 0:
                if the_list[n][g] == 1:
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
                if dc == 3:
                    the_other_list[n][m] = 1
                else:
                    the_other_list[n][m] = 0
            if the_list[n][m] == 1:
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
                if ac != 2 and ac != 3:
                    the_other_list[n][m] = 0
                else:
                    the_other_list[n][m] = 1

    for i in the_other_list:
        print(the_other_list[count])
        count = count + 1
    print("")
    for x in range(len(the_other_list)):
        for y in range(len(the_other_list)):
            the_list[x][y] = the_other_list[x][y]
    #the_list = the_other_list
    #for i in the_list:
     #   print(the_list[count3])
      #  count3 = count3 + 1
       # print("")
