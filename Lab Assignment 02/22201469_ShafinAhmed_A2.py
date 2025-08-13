import random
import math

components = {
    "ALU": (5, 5),
    "Cache": (7, 4),
    "Control Unit": (4, 4),
    "Register File": (6, 6),
    "Decoder":(5, 3),
    "Floating Unit":(5, 5)
}

totalArea=25
iterations=15

def generate_chromosome():
    return [(random.randint(0,totalArea), random.randint(0,totalArea)) for x in range(len(components))]

print(components)

population=[generate_chromosome() for y in range(6)]
print(population)