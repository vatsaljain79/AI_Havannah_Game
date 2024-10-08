import time
import math
import random
import numpy as np
from helper import *

def check_my_win(board: np.array, move: Tuple[int, int], player_num: int, path:List[Tuple[int, int]]=None) -> Tuple[bool, Union[str, None]]:
    board = (board == player_num)
    if check_ring(board, move):
        return True, "ring"
    
    win, way = check_fork_and_bridge(board, move)
    if win:
        return True, way
    return False, None
        
def is_really_alkene(x,x1,y1,board):
    l=set(get_neighbours(len(board),x)).intersection(get_neighbours(len(board),(x1,y1)))
    for i in l:
        if board[i[0]][i[1]]!=0:
            return False
    return True

def is_adjacent(move,pnum,board):
        neighbours=get_neighbours(len(board),move)
        h=[]
        for i in neighbours:
            # h.extend(get_neighbours(len(board),i))
            if board[i[0]][i[1]]==pnum:
                return True
        # for i in h:
        #     if board[i[0]][i[1]]==pnum:
        #         return True
        return False
def alkene_detection(move,board,player):
    x=move
    c=[]
    d=[]
    if(x[1]==(len(board)-1)//2):
        if is_valid(x[0]-1,x[1]-2,len(board)) and board[x[0]-1][x[1]-2] in [player,3-player] and is_really_alkene(x,x[0]-1,x[1]-2,board):
            if((board[x[0]-1][x[1]-2])==player):
                c.append((x[0]-1,x[1]-2))
            else:
                d.append((x[0]-1,x[1]-2))
        if is_valid(x[0]-1,x[1]+2,len(board)) and board[x[0]-1][x[1]+2] in [player,3-player] and is_really_alkene(x,x[0]-1,x[1]+2,board):
            if((board[x[0]-1][x[1]+2])==player):
                c.append((x[0]-1,x[1]+2))
            else:
                d.append((x[0]-1,x[1]+2))
        if is_valid(x[0]-2,x[1]-1,len(board)) and board[x[0]-2][x[1]-1] in [player,3-player] and is_really_alkene(x,x[0]-2,x[1]-1,board):
            if((board[x[0]-2][x[1]-1])==player):
                c.append((x[0]-2,x[1]-1))
            else:
                d.append((x[0]-2,x[1]-1))
        if is_valid(x[0]-2,x[1]+1,len(board)) and board[x[0]-2][x[1]+1] in [player,3-player] and is_really_alkene(x,x[0]-2,x[1]+1,board):
            if((board[x[0]-2][x[1]+1])==player):
                c.append((x[0]-2,x[1]+1))
            else:
                d.append((x[0]-2,x[1]+1))
        if is_valid(x[0]+1,x[1]-1,len(board)) and board[x[0]+1][x[1]-1] in [player,3-player] and is_really_alkene(x,x[0]+1,x[1]-1,board):
            if((board[x[0]+1][x[1]-1])==player):
                c.append((x[0]+1,x[1]-1))
            else:
                d.append((x[0]+1,x[1]-1))
        if is_valid(x[0]+1,x[1]+1,len(board)) and board[x[0]+1][x[1]+1] in [player,3-player] and is_really_alkene(x,x[0]+1,x[1]+1,board):
            if((board[x[0]+1][x[1]+1])==player):
                c.append((x[0]+1,x[1]+1))
            else:
                d.append((x[0]+1,x[1]+1))
    elif(x[1]==((len(board)-1)//2)-1):
        if is_valid(x[0]-1,x[1]-2,len(board)) and board[x[0]-1][x[1]-2] in [player,3-player] and is_really_alkene(x,x[0]-1,x[1]-2,board):
            if((board[x[0]-1][x[1]-2])==player):
                c.append((x[0]-1,x[1]-2))
            else:
                d.append((x[0]-1,x[1]-2))
        if is_valid(x[0],x[1]+2,len(board)) and board[x[0]][x[1]+2] in [player,3-player] and is_really_alkene(x,x[0],x[1]+2,board):
            if((board[x[0]][x[1]+2])==player):
                c.append((x[0],x[1]+2))
            else:
                d.append((x[0],x[1]+2))
        if is_valid(x[0]-1,x[1]+1,len(board)) and board[x[0]-1][x[1]+1] in [player,3-player] and is_really_alkene(x,x[0]-1,x[1]+1,board):
            if((board[x[0]-1][x[1]+1])==player):
                c.append((x[0]-1,x[1]+1))
            else:
                d.append((x[0]-1,x[1]+1))
        if is_valid(x[0]+2,x[1]+1,len(board)) and board[x[0]+2][x[1]+1] in [player,3-player] and is_really_alkene(x,x[0]+2,x[1]+1,board):
            if((board[x[0]+2][x[1]+1])==player):
                c.append((x[0]+2,x[1]+1))
            else:
                d.append((x[0]+2,x[1]+1))
        if is_valid(x[0]+1,x[1]-1,len(board)) and board[x[0]+1][x[1]-1] in [player,3-player] and is_really_alkene(x,x[0]+1,x[1]-1,board):
            if((board[x[0]+1][x[1]-1])==player):
                c.append((x[0]+1,x[1]-1))
            else:
                d.append((x[0]+1,x[1]-1))
        if is_valid(x[0]-2,x[1]-1,len(board)) and board[x[0]-2][x[1]-1] in [player,3-player] and is_really_alkene(x,x[0]-2,x[1]-1,board):
            if((board[x[0]-2][x[1]-1])==player):
                c.append((x[0]-2,x[1]-1))
            else:
                d.append((x[0]-2,x[1]-1))
    elif(x[1]==((len(board)-1)//2)+1):
        if is_valid(x[0]-1,x[1]-1,len(board)) and board[x[0]-1][x[1]-1] in [player,3-player] and is_really_alkene(x,x[0]-1,x[1]-1,board):
            if((board[x[0]-1][x[1]-1])==player):
                c.append((x[0]-1,x[1]-1))
            else:
                d.append((x[0]-1,x[1]-1))
        if is_valid(x[0]-1,x[1]+2,len(board)) and board[x[0]-1][x[1]+2] in [player,3-player] and is_really_alkene(x,x[0]-1,x[1]+2,board):
            if((board[x[0]-1][x[1]+2])==player):
                c.append((x[0]-1,x[1]+2))
            else:
                d.append((x[0]-1,x[1]+2))
        if is_valid(x[0]+2,x[1]-1,len(board)) and board[x[0]+2][x[1]-1] in [player,3-player] and is_really_alkene(x,x[0]+2,x[1]-1,board):
            if((board[x[0]+2][x[1]-1])==player):
                c.append((x[0]+2,x[1]-1))
            else:
                d.append((x[0]+2,x[1]-1))
        if is_valid(x[0]-2,x[1]+1,len(board)) and board[x[0]-2][x[1]+1] in [player,3-player] and is_really_alkene(x,x[0]-2,x[1]+1,board):
            if((board[x[0]-2][x[1]+1])==player):
                c.append((x[0]-2,x[1]+1))
            else:
                d.append((x[0]-2,x[1]+1))
        if is_valid(x[0],x[1]-2,len(board)) and board[x[0]][x[1]-2] in [player,3-player] and is_really_alkene(x,x[0],x[1]-2,board):
            if((board[x[0]][x[1]-2])==player):
                c.append((x[0],x[1]-2))
            else:
                d.append((x[0],x[1]-2))
        if is_valid(x[0]+1,x[1]+1,len(board)) and board[x[0]+1][x[1]+1] in [player,3-player] and is_really_alkene(x,x[0]+1,x[1]+1,board):
            if((board[x[0]+1][x[1]+1])==player):
                c.append((x[0]+1,x[1]+1))
            else:
                d.append((x[0]+1,x[1]+1))
    elif(x[1]>((len(board)-1)//2)+1):
        if is_valid(x[0]-1,x[1]-1,len(board)) and board[x[0]-1][x[1]-1] in [player,3-player] and is_really_alkene(x,x[0]-1,x[1]-1,board):
            if((board[x[0]-1][x[1]-1])==player):
                c.append((x[0]-1,x[1]-1))
            else:
                d.append((x[0]-1,x[1]-1))
        if is_valid(x[0]-1,x[1]+2,len(board)) and board[x[0]-1][x[1]+2] in [player,3-player] and is_really_alkene(x,x[0]-1,x[1]+2,board):
            if((board[x[0]-1][x[1]+2])==player):
                c.append((x[0]-1,x[1]+2))
            else:
                d.append((x[0]-1,x[1]+2))
        if is_valid(x[0]+2,x[1]-1,len(board)) and board[x[0]+2][x[1]-1] in [player,3-player] and is_really_alkene(x,x[0]+2,x[1]-1,board):
            if((board[x[0]+2][x[1]-1])==player):
                c.append((x[0]+2,x[1]-1))
            else:
                d.append((x[0]+2,x[1]-1))
        if is_valid(x[0]-2,x[1]+1,len(board)) and board[x[0]-2][x[1]+1] in [player,3-player] and is_really_alkene(x,x[0]-2,x[1]+1,board):
            if((board[x[0]-2][x[1]+1])==player):
                c.append((x[0]-2,x[1]+1))
            else:
                d.append((x[0]-2,x[1]+1))
        if is_valid(x[0]+1,x[1]-2,len(board)) and board[x[0]+1][x[1]-2] in [player,3-player] and is_really_alkene(x,x[0]+1,x[1]-2,board):
            if((board[x[0]+1][x[1]-2])==player):
                c.append((x[0]+1,x[1]-2))
            else:
                d.append((x[0]+1,x[1]-2))
        if is_valid(x[0]+1,x[1]+1,len(board)) and board[x[0]+1][x[1]+1] in [player,3-player] and is_really_alkene(x,x[0]+1,x[1]+1,board):
            if((board[x[0]+1][x[1]+1])==player):
                c.append((x[0]+1,x[1]+1))
            else:
                d.append((x[0]+1,x[1]+1))
    elif(x[1]<((len(board)-1)//2)-1):
        if is_valid(x[0]-1,x[1]-2,len(board)) and board[x[0]-1][x[1]-2] in [player,3-player] and is_really_alkene(x,x[0]-1,x[1]-2,board):
            if((board[x[0]-1][x[1]-2])==player):
                c.append((x[0]-1,x[1]-2))
            else:
                d.append((x[0]-1,x[1]-2))
        if is_valid(x[0]+1,x[1]+2,len(board)) and board[x[0]+1][x[1]+2] in [player,3-player] and is_really_alkene(x,x[0]+1,x[1]+2,board):
            if((board[x[0]+1][x[1]+2])==player):
                c.append((x[0]+1,x[1]+2))
            else:
                d.append((x[0]+1,x[1]+2))                
        if is_valid(x[0]-1,x[1]+1,len(board)) and board[x[0]-1][x[1]+1] in [player,3-player] and is_really_alkene(x,x[0]-1,x[1]+1,board):
            if((board[x[0]-1][x[1]+1])==player):
                c.append((x[0]-1,x[1]+1))
            else:
                d.append((x[0]-1,x[1]+1))
        if is_valid(x[0]+2,x[1]+1,len(board)) and board[x[0]+2][x[1]+1] in [player,3-player] and is_really_alkene(x,x[0]+2,x[1]+1,board):
            if((board[x[0]+2][x[1]+1])==player):
                c.append((x[0]+2,x[1]+1))
            else:
                d.append((x[0]+2,x[1]+1))
        if is_valid(x[0]+1,x[1]-1,len(board)) and board[x[0]+1][x[1]-1] in [player,3-player] and is_really_alkene(x,x[0]+1,x[1]-1,board):
            if((board[x[0]+1][x[1]-1])==player):
                c.append((x[0]+1,x[1]-1))
            else:
                d.append((x[0]+1,x[1]-1))
        if is_valid(x[0]-2,x[1]-1,len(board)) and board[x[0]-2][x[1]-1] in [player,3-player] and is_really_alkene(x,x[0]-2,x[1]-1,board):
            if((board[x[0]-2][x[1]-1])==player):
                c.append((x[0]-2,x[1]-1))
            else:
                d.append((x[0]-2,x[1]-1))
    f=c.copy()
    if(len(c)==0):
        if(len(d)==0):
            c=0
        elif(len(d)==1):
            c=0
        elif(len(d)==2):
            m1=d[0]
            m2=d[1]
            l=set(get_neighbours(len(board),m2)).intersection(get_neighbours(len(board),m1))
            if(len(l)==0):
                c=1.8700828
            else:
                c=0
        else:
            c=1.8700828
    elif(len(c)==1):
        if(len(d)==0):
            c=1
        elif(len(d)==1):
            c=1.5  
        elif(len(d)==2):
            m1=d[0]
            m2=d[1]
            l=set(get_neighbours(len(board),m2)).intersection(get_neighbours(len(board),m1))
            if(len(l)==0):
                c=1.8700828
            else:
                c=1.5
        else:
            c=1.8700828
    elif(len(c)==2):
        m1=c[0]
        m2=c[1]
        l=set(get_neighbours(len(board),m2)).intersection(get_neighbours(len(board),m1))
        if(len(l)==0):
            c=1.8700828
        else:
            if(len(d)==0):
                c=1
            elif(len(d)==1):
                c=1.5  
            elif(len(d)==2):
                m1=d[0]
                m2=d[1]
                l=set(get_neighbours(len(board),m2)).intersection(get_neighbours(len(board),m1))
                if(len(l)==0):
                    c=1.8700828
                else:
                    c=1.5
            else:
                c=1.8700828
    else:
        c=1.8700828
    check_list=[]
    if(c==1.8700828 and len(f)>=2):
        for i in f:
            l=set(get_neighbours(len(board),move)).intersection(get_neighbours(len(board),i))
            l=tuple(l)
            check_list.append(l)
    return c,check_list

def alkene_detection_todo(move,board,player):
    x=move
    c=[]
    d=[]
    if(x[1]==(len(board)-1)//2):
        if is_valid(x[0]-1,x[1]-2,len(board)) and board[x[0]-1][x[1]-2] in [player,3-player]:
            if(board[x[0]-1][x[1]-2]==player):
                c.append((x[0]-1,x[1]-2))
            else:
                d.append((x[0]-1,x[1]-2))
        if is_valid(x[0]-1,x[1]+2,len(board)) and board[x[0]-1][x[1]+2] in [player,3-player]:
            if(board[x[0]-1][x[1]+2]==player):
                c.append((x[0]-1,x[1]+2))
            else:
                d.append((x[0]-1,x[1]+2))
        if is_valid(x[0]-2,x[1]-1,len(board)) and board[x[0]-2][x[1]-1] in [player,3-player]:
            if(board[x[0]-2][x[1]-1]==player):
                c.append((x[0]-2,x[1]-1))
            else:
                d.append((x[0]-2,x[1]-1))
        if is_valid(x[0]-2,x[1]+1,len(board)) and board[x[0]-2][x[1]+1] in [player,3-player]:
            if(board[x[0]-2][x[1]+1]==player):
                c.append((x[0]-2,x[1]+1))
            else:
                d.append((x[0]-2,x[1]+1))
        if is_valid(x[0]+1,x[1]-1,len(board)) and board[x[0]+1][x[1]-1] in [player,3-player]:
            if(board[x[0]+1][x[1]-1]==player):
                c.append((x[0]+1,x[1]-1))
            else:
                d.append((x[0]+1,x[1]-1))
        if is_valid(x[0]+1,x[1]+1,len(board)) and board[x[0]+1][x[1]+1] in [player,3-player]:
            if(board[x[0]+1][x[1]+1]==player):
                c.append((x[0]+1,x[1]+1))
            else:
                d.append((x[0]+1,x[1]+1))
    elif(x[1]==((len(board)-1)//2)-1):
        if is_valid(x[0]-1,x[1]-2,len(board)) and board[x[0]-1][x[1]-2] in [player,3-player]:
            if(board[x[0]-1][x[1]-2]==player):
                c.append((x[0]-1,x[1]-2))
            else:
                d.append((x[0]-1,x[1]-2))
        if is_valid(x[0],x[1]+2,len(board)) and board[x[0]][x[1]+2] in [player,3-player]:
            if(board[x[0]][x[1]+2]==player):
                c.append((x[0],x[1]+2))
            else:
                d.append((x[0],x[1]+2))
        if is_valid(x[0]-1,x[1]+1,len(board)) and board[x[0]-1][x[1]+1] in [player,3-player]:
            if(board[x[0]-1][x[1]+1]==player):
                c.append((x[0]-1,x[1]+1))
            else:
                d.append((x[0]-1,x[1]+1))
        if is_valid(x[0]+2,x[1]+1,len(board)) and board[x[0]+2][x[1]+1] in [player,3-player]:
            if(board[x[0]+2][x[1]+1]==player):
                c.append((x[0]+2,x[1]+1))
            else:
                d.append((x[0]+2,x[1]+1))
        if is_valid(x[0]+1,x[1]-1,len(board)) and board[x[0]+1][x[1]-1] in [player,3-player]:
            if(board[x[0]+1][x[1]-1]==player):
                c.append((x[0]+1,x[1]-1))
            else:
                d.append((x[0]+1,x[1]-1))
        if is_valid(x[0]-2,x[1]-1,len(board)) and board[x[0]-2][x[1]-1] in [player,3-player]:
            if(board[x[0]-2][x[1]-1]==player):
                c.append((x[0]-2,x[1]-1))
            else:
                d.append((x[0]-2,x[1]-1))
    elif(x[1]==((len(board)-1)//2)+1):
        if is_valid(x[0]-1,x[1]-1,len(board)) and board[x[0]-1][x[1]-1] in [player,3-player]:
            if(board[x[0]-1][x[1]-1]==player):
                c.append((x[0]-1,x[1]-1))
            else:
                d.append((x[0]-1,x[1]-1))
        if is_valid(x[0]-1,x[1]+2,len(board)) and board[x[0]-1][x[1]+2] in [player,3-player]:
            if(board[x[0]-1][x[1]+2]==player):
                c.append((x[0]-1,x[1]+2))
            else:
                d.append((x[0]-1,x[1]+2))
        if is_valid(x[0]+2,x[1]-1,len(board)) and board[x[0]+2][x[1]-1] in [player,3-player]:
            if(board[x[0]+2][x[1]-1]==player):
                c.append((x[0]+2,x[1]-1))
            else:
                d.append((x[0]+2,x[1]-1))
        if is_valid(x[0]-2,x[1]+1,len(board)) and board[x[0]-2][x[1]+1] in [player,3-player]:
            if(board[x[0]-2][x[1]+1]==player):
                c.append((x[0]-2,x[1]+1))
            else:
                d.append((x[0]-2,x[1]+1))
        if is_valid(x[0],x[1]-2,len(board)) and board[x[0]][x[1]-2] in [player,3-player]:
            if(board[x[0]][x[1]-2]==player):
                c.append((x[0],x[1]-2))
            else:
                d.append((x[0],x[1]-2))
        if is_valid(x[0]+1,x[1]+1,len(board)) and board[x[0]+1][x[1]+1] in [player,3-player]:
            if(board[x[0]+1][x[1]+1]==player):
                c.append((x[0]+1,x[1]+1))
            else:
                d.append((x[0]+1,x[1]+1))
    elif(x[1]>((len(board)-1)//2)+1):
        if is_valid(x[0]-1,x[1]-1,len(board)) and board[x[0]-1][x[1]-1] in [player,3-player]:
            if(board[x[0]-1][x[1]-1]==player):
                c.append((x[0]-1,x[1]-1))
            else:
                d.append((x[0]-1,x[1]-1))
        if is_valid(x[0]-1,x[1]+2,len(board)) and board[x[0]-1][x[1]+2] in [player,3-player]:
            if(board[x[0]-1][x[1]+2]==player):
                c.append((x[0]-1,x[1]+2))
            else:
                d.append((x[0]-1,x[1]+2))
        if is_valid(x[0]+2,x[1]-1,len(board)) and board[x[0]+2][x[1]-1] in [player,3-player]:
            if(board[x[0]+2][x[1]-1]==player):
                c.append((x[0]+2,x[1]-1))
            else:
                d.append((x[0]+2,x[1]-1))
        if is_valid(x[0]-2,x[1]+1,len(board)) and board[x[0]-2][x[1]+1] in [player,3-player]:
            if(board[x[0]-2][x[1]+1]==player):
                c.append((x[0]-2,x[1]+1))
            else:
                d.append((x[0]-2,x[1]+1))
        if is_valid(x[0]+1,x[1]-2,len(board)) and board[x[0]+1][x[1]-2] in [player,3-player]:
            if(board[x[0]+1][x[1]-2]==player):
                c.append((x[0]+1,x[1]-2))
            else:
                d.append((x[0]+1,x[1]-2))
        if is_valid(x[0]+1,x[1]+1,len(board)) and board[x[0]+1][x[1]+1] in [player,3-player]:
            if(board[x[0]+1][x[1]+1]==player):
                c.append((x[0]+1,x[1]+1))
            else:
                d.append((x[0]+1,x[1]+1))
    elif(x[1]<((len(board)-1)//2)-1):
        # print(board[0][0])
        # print(board[2][4])
        if is_valid(x[0]-1,x[1]-2,len(board)) and board[x[0]-1][x[1]-2] in [player,3-player]:
            if(board[x[0]-1][x[1]-2]==player):
                c.append((x[0]-1,x[1]-2))
            else:
                d.append((x[0]-1,x[1]-2))
        if is_valid(x[0]+1,x[1]+2,len(board)) and board[x[0]+1][x[1]+2] in [player,3-player]:
            if(board[x[0]+1][x[1]+2]==player):
                c.append((x[0]+1,x[1]+2))
            else:
                d.append((x[0]+1,x[1]+2))                
        if is_valid(x[0]-1,x[1]+1,len(board)) and board[x[0]-1][x[1]+1] in [player,3-player]:
            if(board[x[0]-1][x[1]+1]==player):
                c.append((x[0]-1,x[1]+1))
            else:
                d.append((x[0]-1,x[1]+1))
        if is_valid(x[0]+2,x[1]+1,len(board)) and board[x[0]+2][x[1]+1] in [player,3-player]:
            if(board[x[0]+2][x[1]+1]==player):
                c.append((x[0]+2,x[1]+1))
            else:
                d.append((x[0]+2,x[1]+1))
        if is_valid(x[0]+1,x[1]-1,len(board)) and board[x[0]+1][x[1]-1] in [player,3-player]:
            if(board[x[0]+1][x[1]-1]==player):
                c.append((x[0]+1,x[1]-1))
            else:
                d.append((x[0]+1,x[1]-1))
        if is_valid(x[0]-2,x[1]-1,len(board)) and board[x[0]-2][x[1]-1] in [player,3-player]:
            if(board[x[0]-2][x[1]-1]==player):
                c.append((x[0]-2,x[1]-1))
            else:
                d.append((x[0]-2,x[1]-1))
    # if(move==(1,2)):
    #     print(c,d)
    f=c.copy()
    if(len(c)==0):
        if(len(d)==0):
            c=0
        elif(len(d)==1):
            c=0
        elif(len(d)==2):
            m1=d[0]
            m2=d[1]
            l=set(get_neighbours(len(board),m2)).intersection(get_neighbours(len(board),m1))
            if(len(l)==0):
                c=1.8700828
            else:
                c=0
        else:
            c=1.8700828
    elif(len(c)==1):
        if(len(d)==0):
            c=1
        elif(len(d)==1):
            c=1.5  
        elif(len(d)==2):
            m1=d[0]
            m2=d[1]
            l=set(get_neighbours(len(board),m2)).intersection(get_neighbours(len(board),m1))
            if(len(l)==0):
                c=1.8700828
            else:
                c=1.5
        else:
            c=1.8700828
    elif(len(c)==2):
        m1=c[0]
        m2=c[1]
        l=set(get_neighbours(len(board),m2)).intersection(get_neighbours(len(board),m1))
        if(len(l)==0):
            c=1.8700828
        else:
            if(len(d)==0):
                c=1
            elif(len(d)==1):
                c=1.5  
            elif(len(d)==2):
                m1=d[0]
                m2=d[1]
                l=set(get_neighbours(len(board),m2)).intersection(get_neighbours(len(board),m1))
                if(len(l)==0):
                    c=1.8700828
                else:
                    c=1.5
            else:
                c=1.8700828
    else:
        c=1.8700828
    check_list=[]
    if(c==1.8700828 and len(f)>=2):
        for i in f:
            l=set(get_neighbours(len(board),move)).intersection(get_neighbours(len(board),i))
            l=tuple(l)
            check_list.append(l)
    return c,check_list

def get_my_valid_actions(board: np.array, player: int = None) -> List[Tuple[int, int]]:
    '''
    Returns all the valid actions in the provided state `board`
    
    # Parameters
    `board (numpy array)`: Game board

    # Returns
    List[Tuple[int]]: List of valid actions, coordinates of the valid moves
    '''
    valid_moves = np.argwhere(board == 0)
    n_val_moves=[]
    for x in valid_moves:
        x=tuple(x)
        if get_corner(x,len(board))!=-1:
            n_val_moves.append(x)
        elif get_edge(x,len(board))!=-1:
            n_val_moves.append(x)
        elif is_adjacent(x,player,board) or is_adjacent(x,3-player,board):
            n_val_moves.append(x)
        elif alkene_detection(x,board,player)[0]:
            n_val_moves.append(x)

          
    # valid_moves = [tuple(move) for move in valid_moves]
    return n_val_moves

class Node:
    def __init__(self, state, parent=None):
        self.state = state  
        self.parent = parent
        self.children = []
        self.wins = 0
        self.visits = 0
        self.player = None
        self.move=None
        self.children_left=set()
        


class AIPlayer:


    def __init__(self, player_number: int, timer):
        """
        Initialize the AIPlayer Agent

        Parameters:
        player_number (int): Current player number, num==1 starts the game
        timer: Timer object used to fetch the remaining time for any player
        """
        self.player_number = player_number
        self.type = 'ai'
        self.player_string = 'Player {}: ai'.format(player_number)
        self.timer = timer
        self.counter=0
        self.prev_board = None
        
    def get_corner_alkenes(self,corner,board_size):
        if corner[0]==0 and corner[1]==0:
            return [(1,2),(2,1)]
        elif corner[0]==board_size-1 and corner[1]==0:
            return [(board_size-2,1),(board_size,2)]
        elif corner[0]==0 and corner[1]==board_size-1:
            return [(1,board_size-2),(1,board_size)]
        elif corner[0]==2*board_size-2 and corner[1]==board_size-1:
            return [(corner[0]-2,corner[1]+1),(corner[0]-2,corner[1]-1)]
        elif corner[0]==0 and corner[1]==2*board_size-2:
            return [(corner[0]+1,corner[1]-2),(corner[0]+2,corner[1]-1)]
        elif corner[0]==board_size-1 and corner[1]==2*board_size-2:
            return [(corner[0]-1,corner[1]-1),(corner[0]+1,corner[1]-2)]
        
    def get_move(self, state: np.array) -> Tuple[int, int]:
        """
        Given the current state of the board, return the next move.

        Parameters:
        state: Tuple[np.array] - A numpy array containing the state of the board.

        Returns:
        Tuple[int, int]: action (coordinates of a board cell)
        """
        if(self.counter==0):
            self.counter+=1
            a=get_all_corners(len(state))
            if(state[a[0]]==0):
                self.prev_board=state.copy()
                self.prev_board[a[0][0]][a[0][1]]=self.player_number
                return a[0]
            else:
                self.prev_board=state.copy()
                self.prev_board[a[1][0]][a[1][1]]=self.player_number
                return a[1]

        root=Node(state)
        root.player=self.player_number
        a=set(get_valid_actions(state))
        other_player=3-self.player_number
        new_state=state.copy()
        for move in a:
            new_state[move[0]][move[1]]=self.player_number
            # print(new_state)
            if check_my_win(new_state, move, self.player_number)[0]:
                self.prev_board=state.copy()
                self.prev_board[move[0]][move[1]]=self.player_number
                return move
            new_state[move[0]][move[1]]=0
        
        for move in a:
            new_state[move[0]][move[1]]=other_player
            if check_my_win(new_state, move, other_player)[0]:
                self.prev_board=state.copy()
                self.prev_board[move[0]][move[1]]=self.player_number
                return move
            new_state[move[0]][move[1]]=0
        moves=a.copy()
        for move in a:
            new_state[move[0]][move[1]]=self.player_number
            moves.remove(move)
            f=0
            for move2 in moves:
                new_state[move2[0]][move2[1]]=self.player_number
                if check_my_win(new_state, move2, self.player_number)[0]:
                    f+=1
                    if f==2:
                        self.prev_board=state.copy()
                        self.prev_board[move[0]][move[1]]=self.player_number
                        return move
                new_state[move2[0]][move2[1]]=0 
            new_state[move[0]][move[1]]=0
            moves.add(move)
        for move in a:
            new_state[move[0]][move[1]]=3-self.player_number
            moves.remove(move)
            f=0
            for move2 in moves:
                new_state[move2[0]][move2[1]]=3-self.player_number
                if check_my_win(new_state, move2, 3-self.player_number)[0]:
                    f+=1
                    if f==2:
                        self.prev_board=state.copy()
                        self.prev_board[move[0]][move[1]]=self.player_number
                        return move
                new_state[move2[0]][move2[1]]=0 
            new_state[move[0]][move[1]]=0
            moves.add(move)
        board_size=(len(state)+1)//2
        corners=get_all_corners(len(state))
        d_my={}
        g_my={}
        d={}
        g={}
        for i in corners:
            l=self.get_corner_alkenes(i,board_size)
            l1=[]
            for j in l:
                if is_really_alkene(i,j[0],j[1],state):
                    l1.append(j)
            l=l1
            for j in l:
                if state[j[0]][j[1]]==3-self.player_number:
                    if j in g:
                        g[j].append(i)
                    else:
                        g[j]=[i]
                if state[j[0]][j[1]]==self.player_number:
                    if j in g_my:
                        g_my[j].append(i)
                    else:
                        g_my[j]=[i]
            if state[i[0]][i[1]]==3-self.player_number:
                for j in l:
                    if state[j[0]][j[1]]==0:
                        if j in d:
                            d[j]+=1
                        else:
                            d[j]=1
            if state[i[0]][i[1]]==self.player_number:
                for j in l:
                    if state[j[0]][j[1]]==0:
                        if j in d_my:
                            d_my[j]+=1
                        else:
                            d_my[j]=1
        if board_size==4:
            for i in d_my:
                if d_my[i]==2:
                    self.prev_board=state.copy()
                    self.prev_board[i[0]][i[1]]=self.player_number
                    # print("BELLO")
                    return i
            for i in g_my:
                if len(g_my[i])==2:
                    if state[g_my[i][0][0]][g_my[i][0][1]]==0 and state[g_my[i][1][0]][g_my[i][1][1]]==self.player_number:
                        self.prev_board=state.copy()
                        self.prev_board[g_my[i][0][0]][g_my[i][0][1]]=self.player_number
                        # print("BELLO2")
                        return g_my[i][0]
                    elif state[g_my[i][1][0]][g_my[i][1][1]]==0 and state[g_my[i][0][0]][g_my[i][0][1]]==self.player_number:
                        self.prev_board=state.copy()
                        self.prev_board[g_my[i][1][0]][g_my[i][1][1]]=self.player_number
                        # print("BELLO3")
                        return g_my[i][1]
            for i in d:
                if d[i]==2:
                    self.prev_board=state.copy()
                    self.prev_board[i[0]][i[1]]=self.player_number
                    # print("BELLO")
                    return i
            for i in g:
                if len(g[i])==2:
                    if state[g[i][0][0]][g[i][0][1]]==0 and state[g[i][1][0]][g[i][1][1]]==3-self.player_number:
                        self.prev_board=state.copy()
                        self.prev_board[g[i][0][0]][g[i][0][1]]=self.player_number
                        # print("BELLO2")
                        return g[i][0]
                    elif state[g[i][1][0]][g[i][1][1]]==0 and state[g[i][0][0]][g[i][0][1]]==3-self.player_number:
                        self.prev_board=state.copy()
                        self.prev_board[g[i][1][0]][g[i][1][1]]=self.player_number
                        # print("BELLO3")
                        return g[i][1]
        # print('halautututut')
        # t=time.time()
        if isinstance(self.prev_board, np.ndarray):
            # print('hi1i1i1')
            for i in range(len(state)):
                for j in range(len(state[0])):
                    if state[i][j]==3-self.player_number and  self.prev_board[i][j]==0:
                        # print(i,j,'hellooeoeoeoeoeoeoeoeoe')
                        for neigh in get_neighbours(len(state), (i, j)):
                            if state[neigh[0]][neigh[1]]==self.player_number:
                            # print(neigh)
                                c,f=alkene_detection_todo(neigh,self.prev_board,self.player_number)
                                # print(c,f)
                                if c==1.8700828:
                                    for k in f:
                                        if k[0]==(i,j) and state[k[1][0]][k[1][1]]==0:
                                            self.prev_board=state.copy()
                                            self.prev_board[k[1][0]][k[1][1]]=self.player_number
                                            # print('time',time.time()-t)
                                            return k[1]
                                        elif k[1]==(i,j) and state[k[0][0]][k[0][1]]==0:
                                            self.prev_board=state.copy()
                                            self.prev_board[k[0][0]][k[0][1]]=self.player_number
                                            # print('time',time.time()-t)
                                            return k[0]
                        
        

                                

        root.children_left=get_my_valid_actions(state,self.player_number)
        # for i in root.children_left:
        #     print(*i,'hi')
        for i in range(325):
            node=root
            while len(node.children_left)==0 and node.children :
                node=self.select(node)
            # print(node.state)
            node=self.expand(node)
            if not node:
                continue
            # print(node.state)
            win=0
            for j in range(3):
                winner=self.rollout(node)
                if(winner==self.player_number):
                    win+=1
                # print(winner)
            loss=3-win
            tot_win=win-loss
            self.backpropagate(node, winner,tot_win)
            # print(root.children[0].visits,root.children[0].wins)
        # print(len(root.children))
        # for i in root.children:
        #     print(i.move,i.visits,i.wins)
        best_node=None
        best_val=-float("inf")
        g=[]
        for i in root.children:
            c=self.ucb1(i,0.1)
            if(c>best_val):
                best_val=c
                best_node=i
        #     if get_corner(i.move,len(state))!=-1 or get_edge(i.move,len(state))!=-1 or self.is_adjacent(i.move,3-self.player_number,state) or self.is_adjacent2(x,3-self.player_number,state):
        #         g.append(i)
        #         if i.visits>best_val:
        #             best_val=i.visits
        #             best_node=i
        #         elif i.visits==best_val:
        #             if i.wins>best_node.wins:
        #                 best_node=i
        new_state=state.copy()
        l=[]
        # for i in g:
        #         print(i.move,i.visits,i.wins)
        #         if i.visits==best_node.visits and i.wins==best_node.wins:
        #             new_state[i.move[0]][i.move[1]]=self.player_number
        #             if check_my_win(new_state, i.move, self.player_number)[0]:
        #                 return i.move
        #             new_state[i.move[0]][i.move[1]]=3-self.player_number
        #             if check_my_win(new_state, i.move, 3-self.player_number)[0]:
        #                 return i.move
        #             new_state[i.move[0]][i.move[1]]=0
        #             l.append(i.move)
                
                    

        # if len(l)>0:
        #     return random.choice(l)
        self.prev_board=state.copy()
        self.prev_board[best_node.move[0]][best_node.move[1]]=self.player_number
        return best_node.move
    

    def ucb1(self,child, exploration_factor=1.75):
        """
        Calculate the UCB1 value for a node.
        """
        if child.visits == 0:
            return float('inf')  
        win_rate = child.wins / child.visits
        exploration_term = exploration_factor * np.sqrt(np.log(child.parent.visits) / child.visits)
        c=alkene_detection(child.move,child.state,self.player_number)[0]
        d=get_corner(child.move,len(child.state))
        e=get_edge(child.move,len(child.state))
        if(d!=-1):
            win_rate+=(abs(win_rate))*(0.6 if win_rate<0 else 0.3)
        if(e!=-1):
            win_rate+=(abs(win_rate))*(0.2 if win_rate<0 else 0.1)
        win_rate+=c*c*(abs(win_rate))*(0.4 if win_rate<0 else 0.15)
        return win_rate + exploration_term
    
    def select(self,node):
        """
        Select the best node based on UCB1.
        """
        return max(node.children, key=lambda child: self.ucb1(child))

    def expand(self,node):
        """
        Expand the current node by generating a new child for an unexplored move.
        """
        available_moves = node.children_left
        if available_moves:
            move = available_moves.pop()
            new_state = node.state.copy()
            new_state[move[0]][move[1]]=node.player
            child_node = Node(state=new_state, parent=node)
            child_node.player = 3-node.player
            child_node.move=move
            a=set(get_my_valid_actions(new_state,self.player_number))
            child_node.children_left=a
            node.children.append(child_node)
            return child_node
        return None
    
    def rollout(self, node):
        """
        Simulate a random game starting from the current node's state.
        """
        current_state = node.state.copy()
        current_player = node.player
        a=get_my_valid_actions(current_state,self.player_number)
        moves=set(a)
        while moves:
            move=random.choice(tuple(moves))
            current_state[move[0]][move[1]] = current_player
            t1=get_neighbours(len(current_state),move)
            for x in t1:
                if(current_state[x[0]][x[1]]==0):
                    moves.add(x)
            x=move
            board=current_state
            if(x[1]==(len(board)-1)//2):
                if is_valid(x[0]-1,x[1]-2,len(board)) and board[x[0]-1][x[1]-2]==0 and is_really_alkene(x,x[0]-1,x[1]-2,board):
                    moves.add((x[0]-1,x[1]-2))
                if is_valid(x[0]-1,x[1]+2,len(board)) and board[x[0]-1][x[1]+2]==0 and is_really_alkene(x,x[0]-1,x[1]+2,board):
                    moves.add((x[0]-1,x[1]+2))
                if is_valid(x[0]-2,x[1]-1,len(board)) and board[x[0]-2][x[1]-1]==0 and is_really_alkene(x,x[0]-2,x[1]-1,board):
                    moves.add((x[0]-2,x[1]-1))
                if is_valid(x[0]-2,x[1]+1,len(board)) and board[x[0]-2][x[1]+1]==0 and is_really_alkene(x,x[0]-2,x[1]+1,board):
                    moves.add((x[0]-2,x[1]+1))
                if is_valid(x[0]+1,x[1]-1,len(board)) and board[x[0]+1][x[1]-1]==0 and is_really_alkene(x,x[0]+1,x[1]-1,board):
                    moves.add((x[0]+1,x[1]-1))
                if is_valid(x[0]+1,x[1]+1,len(board)) and board[x[0]+1][x[1]+1]==0 and is_really_alkene(x,x[0]+1,x[1]+1,board):
                    moves.add((x[0]+1,x[1]+1))
            elif(x[1]==((len(board)-1)//2)-1):
                if is_valid(x[0]-1,x[1]-2,len(board)) and board[x[0]-1][x[1]-2]==0 and is_really_alkene(x,x[0]-1,x[1]-2,board):
                    moves.add((x[0]-1,x[1]-2))
                if is_valid(x[0],x[1]+2,len(board)) and board[x[0]][x[1]+2]==0 and is_really_alkene(x,x[0],x[1]+2,board):
                    moves.add((x[0],x[1]+2))
                if is_valid(x[0]-1,x[1]+1,len(board)) and board[x[0]-1][x[1]+1]==0 and is_really_alkene(x,x[0]-1,x[1]+1,board):
                    moves.add((x[0]-1,x[1]+1))
                if is_valid(x[0]+2,x[1]+1,len(board)) and board[x[0]+2][x[1]+1]==0 and is_really_alkene(x,x[0]+2,x[1]+1,board):
                    moves.add((x[0]+2,x[1]+1))
                if is_valid(x[0]+1,x[1]-1,len(board)) and board[x[0]+1][x[1]-1]==0 and is_really_alkene(x,x[0]+1,x[1]-1,board):
                    moves.add((x[0]+1,x[1]-1))
                if is_valid(x[0]-2,x[1]-1,len(board)) and board[x[0]-2][x[1]-1]==0 and is_really_alkene(x,x[0]-2,x[1]-1,board):
                    moves.add((x[0]-2,x[1]-1))
            elif(x[1]==((len(board)-1)//2)+1):
                if is_valid(x[0]-1,x[1]-1,len(board)) and board[x[0]-1][x[1]-1]==0 and is_really_alkene(x,x[0]-1,x[1]-1,board):
                    moves.add((x[0]-1,x[1]-1))
                if is_valid(x[0]-1,x[1]+2,len(board)) and board[x[0]-1][x[1]+2]==0 and is_really_alkene(x,x[0]-1,x[1]+2,board):
                    moves.add((x[0]-1,x[1]+2))
                if is_valid(x[0]+2,x[1]-1,len(board)) and board[x[0]+2][x[1]-1]==0 and is_really_alkene(x,x[0]+2,x[1]-1,board):
                    moves.add((x[0]+2,x[1]-1))
                if is_valid(x[0]-2,x[1]+1,len(board)) and board[x[0]-2][x[1]+1]==0 and is_really_alkene(x,x[0]-2,x[1]+1,board):
                    moves.add((x[0]-2,x[1]+1))
                if is_valid(x[0],x[1]-2,len(board)) and board[x[0]][x[1]-2]==0 and is_really_alkene(x,x[0],x[1]-2,board):
                    moves.add((x[0],x[1]-2))
                if is_valid(x[0]+1,x[1]+1,len(board)) and board[x[0]+1][x[1]+1]==0 and is_really_alkene(x,x[0]+1,x[1]+1,board):
                    moves.add((x[0]+1,x[1]+1))
            elif(x[1]>((len(board)-1)//2)+1):
                if is_valid(x[0]-1,x[1]-1,len(board)) and board[x[0]-1][x[1]-1]==0 and is_really_alkene(x,x[0]-1,x[1]-1,board):
                    moves.add((x[0]-1,x[1]-1))
                if is_valid(x[0]-1,x[1]+2,len(board)) and board[x[0]-1][x[1]+2]==0 and is_really_alkene(x,x[0]-1,x[1]+2,board):
                    moves.add((x[0]-1,x[1]+2))
                if is_valid(x[0]+2,x[1]-1,len(board)) and board[x[0]+2][x[1]-1]==0 and is_really_alkene(x,x[0]+2,x[1]-1,board):
                    moves.add((x[0]+2,x[1]-1))
                if is_valid(x[0]-2,x[1]+1,len(board)) and board[x[0]-2][x[1]+1]==0 and is_really_alkene(x,x[0]-2,x[1]+1,board):
                    moves.add((x[0]-2,x[1]+1))
                if is_valid(x[0]+1,x[1]-2,len(board)) and board[x[0]+1][x[1]-2]==0 and is_really_alkene(x,x[0]+1,x[1]-2,board):
                    moves.add((x[0]+1,x[1]-2))
                if is_valid(x[0]+1,x[1]+1,len(board)) and board[x[0]+1][x[1]+1]==0 and is_really_alkene(x,x[0]+1,x[1]+1,board):
                    moves.add((x[0]+1,x[1]+1))
            elif(x[1]<((len(board)-1)//2)-1):
                if is_valid(x[0]-1,x[1]-2,len(board)) and board[x[0]-1][x[1]-2]==0 and is_really_alkene(x,x[0]-1,x[1]-2,board):
                    moves.add((x[0]-1,x[1]-2))
                if is_valid(x[0]+1,x[1]+2,len(board)) and board[x[0]+1][x[1]+2]==0 and is_really_alkene(x,x[0]+1,x[1]+2,board):
                    moves.add((x[0]+1,x[1]+2))
                if is_valid(x[0]-1,x[1]+1,len(board)) and board[x[0]-1][x[1]+1]==0 and is_really_alkene(x,x[0]-1,x[1]+1,board):
                    moves.add((x[0]-1,x[1]+1))
                if is_valid(x[0]+2,x[1]+1,len(board)) and board[x[0]+2][x[1]+1]==0 and is_really_alkene(x,x[0]+2,x[1]+1,board):
                    moves.add((x[0]+2,x[1]+1))
                if is_valid(x[0]+1,x[1]-1,len(board)) and board[x[0]+1][x[1]-1]==0 and is_really_alkene(x,x[0]+1,x[1]-1,board):
                    moves.add((x[0]+1,x[1]-1))
                if is_valid(x[0]-2,x[1]-1,len(board)) and board[x[0]-2][x[1]-1]==0 and is_really_alkene(x,x[0]-2,x[1]-1,board):
                    moves.add((x[0]-2,x[1]-1))
            if check_my_win(current_state, move, current_player)[0]:
                return current_player  # Return winner if found
            current_player = 3 - current_player  
            moves.remove(move)
              # Alternate player turns
        return 0  # Return draw or no winner if moves are exhausted

    def backpropagate(self, node, winner,tot_win):
        """
        Propagate the result of the simulation up to the root node.
        """
        while node is not None:
            node.visits += 3
            node.wins += tot_win
            node = node.parent



    