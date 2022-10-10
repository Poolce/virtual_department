from xml.etree.ElementTree import PI
import numpy as np
import math

center=[10,10]

R = 10
N = 100
H = 20
triags = []
for j in range(N):
    for i in range(0,N,2):
        facet = []

        
        x = R * math.sin(math.pi * 2 / N * (i))*math.cos(math.pi * 2 / N * (j))
        y = R * math.sin(math.pi * 2 / N * (i))*math.sin(math.pi * 2 / N * (j))
        z=R * math.cos(math.pi * 2 / N * i)
        facet.append([x,y,z])

        x = R * math.sin(math.pi * 2 / N * i)*math.cos(math.pi * 2 / N * (j+1))
        y = R * math.sin(math.pi * 2 / N * i)*math.sin(math.pi * 2 / N * (j+1))
        z=R * math.cos(math.pi * 2 / N * i)
        facet.append([x,y,z])

        x = R * math.sin(math.pi * 2 / N * (i+1))*math.cos(math.pi * 2 / N * j)
        y = R * math.sin(math.pi * 2 / N * (i+1))*math.sin(math.pi * 2 / N * j)
        z=R * math.cos(math.pi * 2 / N * (i+1))
        facet.append([x,y,z])

        x = R * math.sin(math.pi * 2 / N * (i+1))*math.cos(math.pi * 2 / N * (j+1))
        y = R * math.sin(math.pi * 2 / N * (i+1))*math.sin(math.pi * 2 / N * (j+1))
        z=R * math.cos(math.pi * 2 / N * (i+1))
        facet.append([x,y,z])

        triags.append(facet[:3])
        triags.append([facet[2],facet[3],facet[1]])
############

#print(triags)




f = open('sphere.stl', 'w')

f.write('solid TRIANGLE\n')


for triag in triags:
    f.write('  facet normal 0 0 0\n  outer loop\n')
    
    for point in triag:
        f.write(f"   vertex {point[0]} {point[1]} {point[2]}\n")

    f.write('  endloop\n  endfacet\n')
f.write('endsolid\n')


f.close()