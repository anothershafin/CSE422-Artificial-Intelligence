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

totalArea=25
iterations=15

def generate_chromosome():
    return [(random.randint(0,totalArea), random.randint(0,totalArea)) for x in range(len(components))]

def calc_overlaps(chromosome):
    count = 0
    for i in range(len(chromosome)):
        for j in range(i+1, len(chromosome)):
            print(chromosome[i],chromosome[j])
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
    print(f"count={count}")      
    return count

def fitness(chromosome):
    overlap=calc_overlaps(chromosome)


population=[generate_chromosome() for y in range(6)]
print(population)

for i in range(iterations):
    for cr in population:
        fitValue=fitness(cr)