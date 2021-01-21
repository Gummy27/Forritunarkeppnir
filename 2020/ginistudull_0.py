import numpy as np
'''
def gini(x):
    mad = np.abs(np.subtract.outer(x, x)).mean()
    rmad = mad/np.mean(x)
    g = 0.5 * rmad
    return g
'''

n = int(input())

studlar = []
for x in range(n):
    studlar.append(float(input()))

a = np.array(studlar)
print(gini(a))