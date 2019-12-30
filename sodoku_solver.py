print("Please type \'0\' in blank spaces")
board = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []
]

#below is entering the board
for i in range(1,10):
    item = input("Please enter the {}th row : ".format(i))
    for j in item:
        board[i-1].append(j)


#print board
def print_board (bo) :
    cur_row = 0
    z = 0
    for _ in range(3):
        print("\n---------------------------------------------------",end='')
        for _ in range(3):
            print(" ")
            print("|   ",end='')
            for _ in range(0,len(bo[cur_row]),3):
                print(bo[cur_row][z],bo[cur_row][z+1],bo[cur_row][z+2],'|' ,sep = '   ',end = '    ')
                z+=3
            z = 0
            cur_row +=1
    print("\n---------------------------------------------------")



def find_blank(bo):
    for row in range(0,9):
        for collum in range(0,9):
            if bo[row][collum] == "0":
                bo[row][collum] = "."
                return (row,collum)
            else:
                pass

def count (bo, item):
    count = 0
    for row in bo :
        count += row.count(str(item))
    return count


def valid(location):
    #checking row
    if board[location[0]].count(board[location[0]][location[1]]) > 1:
        return False
    else:
        pass
    
    for row in range(0,9):
        if board[row][location[1]] == board[location[0]][location[1]] and row != location[0]:
            return False  
        else:
            pass
    #checking square
    for cube_row in range(3*(location[0]//3),3*(location[0]//3)+3):
        for cube_collum in range(3*(location[1]//3),3*(location[1]//3)+3):
            if board[cube_row][cube_collum] == board[location[0]][location[1]] and cube_row != location[0] and cube_collum != location[1]:
                return False   
            else:
                pass 
    return True


def solve(bo):
    repeat = True
    num_recs = []
    blanklocs = []
    ind = 0
    solved = False
    blank_quan = count(bo,0)
    for _ in range(0,blank_quan):
        num_recs.append([])
        blanklocs.append(find_blank(bo))
    while not solved :
        while repeat == True:
            for try_num in range(1,10) : 
                if num_recs[ind].count(try_num) == 1 :
                    if num_recs[ind].count(9) == 1:
                        num_recs[ind] = []
                        bo[blanklocs[ind][0]][blanklocs[ind][1]] = "."
                        ind = ind - 1
                        repeat = True
                        break
                    else:
                        continue
                else:
                    bo[blanklocs[ind][0]][blanklocs[ind][1]] = str(try_num)
                    num_recs[ind].append(try_num)
                    if valid(blanklocs[ind]) == True:  
                        if ind == blank_quan-1:
                            repeat = False
                            solved = True
                            break
                        else:
                            repeat = True
                            ind += 1
                            break
                    else:
                        pass
    return bo

print_board(board)

print_board(solve(board))



                

