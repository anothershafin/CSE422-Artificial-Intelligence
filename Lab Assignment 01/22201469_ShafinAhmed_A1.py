#22201469 Shafin Ahmed
#The input and output format from the main question has been followed here, not the input pdf files.

# Part 01
import heapq
from collections import deque

def heuristic(j,k):
    return abs(j[0]-k[0])+abs(j[1]-k[1])

def a_star(matrix,start,goal):
    r,c=len(matrix),len(matrix[0])
    visited=set()
    parent={}
    g_n={start:0}
    f_n={start: heuristic(start,goal)}
    heap=[(f_n[start],start)]
    
    moves=[(-1,0,'U'),(1,0,'D'),(0,-1,'L'),(0,1,'R')]
    #Here I have implemented the steps of every move so that I do not have to write again while doing a move
    
    while heap:
        popped=heapq.heappop(heap)
        current=popped[1]
        if current==goal:
            sequence=[]
            while current in parent:
                current,mv=parent[current]
                sequence.append(mv)
            return len(sequence), ''.join(reversed(sequence))
        
        visited.add(current)
        
        for dx, dy, mv in moves:
            nextn=(current[0]+dx,current[1]+dy)
            if 0<=nextn[0]<r and 0<=nextn[1]<c and matrix[nextn[0]][nextn[1]]=='0':
                if nextn in visited:
                    continue
                newg=g_n[current]+1
                if nextn in g_n:
                    previous_cost=g_n[nextn]
                else:
                    previous_cost=float('inf')
#Here I am checking if the node had already been explored before and if it has a lesser g(n)
                if newg<previous_cost:
                    parent[nextn]=(current,mv)
                    g_n[nextn]=newg
                    f_n[nextn]=g_n[nextn]+heuristic(nextn,goal)
                    heapq.heappush(heap, (f_n[nextn],nextn))
                    
    return -1,"-1"

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
                line=line.strip().replace(" ", "")
                matrix.append(list(line))
#As there are two types of matrix given in the main file and input file
#this apporach handles spaced and non spaced matrices both cases
            count+=1
    cost,seq=a_star(matrix,(a,b),(c,d))
    print(cost)
    print(seq)

#As we were instructed the program must read from input text file
#But is the assignment folder we were given a pdf file
#I have created a test file for myself
#and the program runs for any text input; just need to edit the text file name on the run_part1() function


#Part 02

def run_part2(filename):
    with open(filename, 'r') as file2:
        count=0
        heuristics={}
        edges=[]
        for line in file2:
            if count==0:
                v,e=map(int,line.split())
            elif count==1:
                initial,goal=map(int,line.split())
            elif 2<=count<(v+2):
                line=line.split()
                heuristics[int(line[0])]=int(line[1])
            else:
                line=line.split()
                edges.append((int(line[0]),int(line[1])))
            count+=1
    print(v,e,initial,goal,heuristics, edges)



run_part1('test_input1.txt')
run_part2('test_input2.txt')
