from __future__ import division
from fractions import gcd
import string
import numpy as np
def shift(l1,n1): # for left shift operation
    return l1[n1:] + l1[:n1]
num = dict(zip(string.ascii_lowercase,xrange(0,26)))# for reverse mapping: numbers to letter
num1= dict(zip(xrange(0,26),string.ascii_lowercase))
a1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
a=raw_input('Please enter your plain text:').lower()
key=raw_input('Enter the encryption key:').lower()
L=len(key)
#####################    dividing in L(max d) parts     ##########################
z=[[]for x1 in xrange(0,L)]
v1=0
while v1<L:
    for i2 in xrange(v1,len(a),L):
        z[v1].append(a[i2])
    v1+=1
key=list(key)
v1=0
z1=[[]for x1 in xrange(0,L)]#for char in key:
while v1<L:
    for char in z[v1]:
        nbr=(num[char]+num[key[v1]])
        nbr=num1[nbr%26]
        z1[v1].append(nbr)
    v1+=1
###################### recovering the L parts into deciphered form ################
v1=0
var=0
D1=[]
vv=int(len(a)/L)
while var<vv:
    while v1<L:
        D1.append(z1[v1][var])
        v1+=1
    var+=1
    v1=0
v1=0
while v1<(len(a)%L):
    D1.append(z1[v1][var])
    v1+=1
print '\n'+'Your encrypted Text the key',''.join(key),'is:'
print ''.join(str(elm) for elm in D1)
    
    
