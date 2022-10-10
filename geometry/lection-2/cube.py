import numpy as np

a = [-1,-1,-1]
b = [1,-1,-1]
c = [1,1,-1]
d = [-1,1,-1]

A = [-1,-1,1]
B = [1,-1,1]
C = [1,1,1]
D = [-1,1,1]




triags = [
        [a,b,c], [a,c,d],# Lower
        [A,B,C], [A,C,D],# Upper
        [a,A,b], [b,B,A],# First
        [a,A,d], [d,D,A],# Sec
        [d,D,c], [c,C,D],# Third
        [c,C,b], [b,B,C],# Fourth
]



f = open('cube.stl', 'w')

f.write('solid TRIANGLE\n')


for triag in triags:
    f.write('  facet normal 0 0 0\n  outer loop\n')
    
    for point in triag:
        f.write(f"   vertex {point[0]} {point[1]} {point[2]}\n")

    f.write('  endloop\n  endfacet\n')
f.write('endsolid\n')


f.close()