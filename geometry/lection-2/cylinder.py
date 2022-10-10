from xml.etree.ElementTree import PI
import numpy as np
import math

center=[10,10]

R = 10
N = 6
H = 20
triags = []
 
for i in range(N):
    facet = []

    x = R * math.cos(math.pi * 2 / N * i)+center[0]
    y = R * math.sin(math.pi * 2 / N * i)+center[1]
    z=0
    facet.append([x,y,z])

    x = R * math.cos(math.pi * 2 / N * i)+center[0]
    y = R * math.sin(math.pi * 2 / N * i)+center[1]
    z=H
    facet.append([x,y,z])

    x = R * math.cos(math.pi * 2 / N * (i+1))+center[0]
    y = R * math.sin(math.pi * 2 / N * (i+1))+center[1]
    z=0
    facet.append([x,y,z])
    facet.append([x,y,H])
    facet.append([center[0],center[1],0])
    facet.append([center[0],center[1],H])

    triags.append(facet[:3])
    triags.append([facet[2],facet[3],facet[1]])
    triags.append([facet[1],facet[5],facet[3]])
    triags.append([facet[0],facet[4],facet[2]])
############

print(triags)




f = open('cylinder.stl', 'w')

f.write('solid TRIANGLE\n')


for triag in triags:
    f.write('  facet normal 0 0 0\n  outer loop\n')
    
    for point in triag:
        f.write(f"   vertex {point[0]} {point[1]} {point[2]}\n")

    f.write('  endloop\n  endfacet\n')
f.write('endsolid\n')


f.close()