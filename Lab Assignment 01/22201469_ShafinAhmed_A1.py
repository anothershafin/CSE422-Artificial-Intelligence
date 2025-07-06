# Part 01
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
    print(n,m,a,b,c,d,matrix)
            
run_part1('test_input1.txt')
