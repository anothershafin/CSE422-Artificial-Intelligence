import random
import math

components = [
    ("ALU", 5, 5),
    ("Cache", 7, 4),
    ("Control Unit", 4, 4),
    ("Register File", 6, 6),
    ("Decoder", 5, 3),
    ("Floating Unit", 5, 5)
]

connections = [
    (3, 0), (2, 0), (0, 1),
    (3, 5), (1, 4), (4, 5)
]

totalArea=25
iterations=1
ch_count=6

para1=1000
para2=2
para3=1


def generate_chromosome():
    return [(random.randint(0,totalArea), random.randint(0,totalArea)) for x in range(len(components))]

def calc_overlaps(chromosome):
    count = 0
    for i in range(len(chromosome)):
        for j in range(i+1, len(chromosome)):
            #counting bottom left index of the two components
            aleftx=chromosome[i][0]
            alefty=chromosome[i][1]
            bleftx=chromosome[j][0]
            blefty=chromosome[j][1]
            #counting right margin and height margin
            aright=aleftx+components[i][1]
            aup=alefty+components[i][2]
            bright=bleftx+components[j][1]
            bup=blefty+components[j][2]

            if not (aright<=bleftx) or (aleftx>=bright) or (aup<=blefty) or (alefty>=bup):
                count+=1    
    return count

def calc_wd(chromosome):
    total=0
    for i,j in connections:
        #calculating centers
        a_centerx=chromosome[i][0]+(components[i][1]/2)
        a_centery=chromosome[i][1]+(components[i][2]/2)
        b_centerx=chromosome[j][0]+(components[j][1]/2)
        b_centery=chromosome[j][1]+(components[j][2]/2)
        
        total+=math.sqrt((a_centerx-b_centerx)**2+(a_centery-b_centery)**2)

    return total

def calc_ba(chromosome):
    x_vals=[x for x,y in chromosome]
    y_vals=[y for x,y in chromosome]
    max_x=max(x+components[i][1] for i, (x,y) in enumerate(chromosome))
    min_x=min(x_vals)
    max_y=max(y+components[i][2] for i, (x,y) in enumerate(chromosome))
    min_y=min(y_vals)
    return (max_x-min_x)*(max_y-min_y)

def fitness(chromosome):
    overlap=calc_overlaps(chromosome)
    wiring=calc_wd(chromosome)
    area=calc_ba(chromosome)
    return -(para1*overlap+para2*wiring+para3*area)

def crossover(parent1,parent2):
    point=random.randint(1, 5)
    child1=parent1[:point]+parent2[point:]
    child2=parent2[:point]+parent1[point:]
    return child1,child2

def mutate(chromosome):
    r_index=random.randint(0,5)
    chromosome[r_index]=(random.randint(0,totalArea), random.randint(0,totalArea))
    return chromosome


population=[generate_chromosome() for y in range(6)]
print(population)

for i in range(iterations):
    fitValue=[]
    for cr in population:
        fitValue+=[fitness(cr)]
    #generating new list like (chromosome, fitness) in descending order
    new_population=sorted(zip(population,fitValue), key=lambda x:x[1], reverse=True)
    #select one elitge chromosome each iteration
    elite_cr=[new_population[0][0]]
    #select the least two fittest:
    least=[new_population[-1][0],new_population[-2][0]]
    #remove the least fittest:
    for z in least:
        for a in range(len(population)):
            if population[a]==z:
                fitValue.pop(a)
        population.remove(z)
        #removed two least fit chromosomes as well as their fitness value
    #select two best fit parents for crossover:
    p1,p2=random.choices(population,weights=[f+50000 for f in fitValue], k=2)
    c1,c2=crossover(p1,p2)
    print(c1,c2)
    c1=mutate(c1)
    c2=mutate(c2)
    print(c1,c2)

    

        