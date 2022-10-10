import numpy as np

f = open('triangle.stl', 'w')

f.write('solid TRIANGLE\n')

f.write('  facet normal 0 0 0\n  outer loop\n')
f.write('   vertex -0.7 0 0\n')
f.write('   vertex 0 1 0\n')
f.write('   vertex 0.7 0 0\n')
f.write('  endloop\n  endfacet\n')

f.write('endsolid')


f.close()