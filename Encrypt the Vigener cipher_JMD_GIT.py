from __future__ import division
from fractions import gcd
import string
import numpy as np
def shift(l1,n1): # for left shift operation
    return l1[n1:] + l1[:n1]
num = dict(zip(string.ascii_lowercase,xrange(0,26)))# for reverse mapping: numbers to letter
num1= dict(zip(xrange(0,26),string.ascii_lowercase))
#A = [0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,0.0236,0.0015,0.01974,0.00074]
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
#    print ''.join(z[v1])
    v1+=1
key=list(key)
v1=0
z1=[[]for x1 in xrange(0,L)]#for char in key:
print L
while v1<L:
#    print 'at 1:',v1
    for char in z[v1]:
        nbr=(num[char]+num[key[v1]])
        nbr=num1[nbr%26]
        z1[v1].append(nbr)
    print ''.join(z1[v1])
    v1+=1
#    print v1
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
    
    
