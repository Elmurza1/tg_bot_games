import json
import math

def calculate_nambers_muitiplicatons(*nambers):
    resalt = math.prod(nambers)
    return resalt

print(calculate_nambers_muitiplicatons(3, 4, 5, 6, ))


def calculate_nambers_muitiplicaton1(*nambers):
    n = 1
    for item in nambers:
        n = n * item
    return n

print(calculate_nambers_muitiplicaton1(5, 3, 8))