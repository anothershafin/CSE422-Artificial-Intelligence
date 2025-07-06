# Part 01
import heapq
def heuristic(j,k):
    return abs(j[0]-k[0])+abs(j[1]-k[1])

def a_star(matrix,start,goal):
    r,c=len(matrix),len(matrix[0])
    visited=set()
    parent={}
    g_n={start:0}
    f_n={start: heuristic(start,goal)}
    

def run_part1(filename):
    with open(filename, 'r') as file1:
        count=0
        matrix=[]
        for line in file1:
            if count==0:
                n,m=map(int,line.split())
            elif count==1:
                a,b=map(int,line.split())
            elif count==2:
                c,d=map(int,line.split())
            else:
                matrix+=[list(line.split())]
            count+=1
    cost,seq=a_star(matrix,(a,b),(c,d))
    print(cost)
    print(seq)

#As we were instructed the program must read from input text file
#But is the assignment folder we were given a pdf file
#I have created a test file for myself
#and the program runs for any text input; just need to edit the text file name on the run_part1() function            
run_part1('test_input1.txt')
