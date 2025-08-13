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
iterations=5

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
        print(f"ch:{chromosome[i]} {chromosome[j]}")
        #calculating centers
        a_centerx=chromosome[i][0]+(components[i][1]/2)
        a_centery=chromosome[i][1]+(components[i][2]/2)
        b_centerx=chromosome[j][0]+(components[j][1]/2)
        b_centery=chromosome[j][1]+(components[j][2]/2)
        
        total+=math.sqrt((a_centerx-b_centerx)**2+(a_centery-b_centery)**2)
        print(f"wd:{total}")
    
    return total

def fitness(chromosome):
    overlap=calc_overlaps(chromosome)
    wiring=calc_wd(chromosome)


population=[generate_chromosome() for y in range(6)]
print(population)

for i in range(iterations):
    for cr in population:
        fitValue=fitness(cr)