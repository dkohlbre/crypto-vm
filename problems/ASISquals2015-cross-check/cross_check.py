#!/usr/bin/python

import gmpy
import random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Cipher import PKCS1_OAEP
import base64
from fractions import gcd
from Crypto import Random


flag = '[censored]'

P = []
Q = []
D = []
N = []
pubKey = []
privKey = []
Enc = []

p = random.randint(1 << 510, 1 << 511)
q = random.randint(1 << 510, 1 << 511)

for i in range(0, 3):
    p = gmpy.next_prime(p)
    q = gmpy.next_prime(q)
    P.append(p)
    Q.append(q)


for i in range(0, 3):
    N.append(P[i] * Q[2 - i])
    print N[i]
    D.append(long(gmpy.invert(long(65537), (P[i] - 1) * (Q[2 - i] - 1))))
    privKey.append(RSA.construct((long(N[i]), long(65537), long(D[i]), long(P[i]), long(Q[2 - i]))))
    pubKey.append(RSA.construct((long(N[i]), long(65537))))
    print pubKey[i].exportKey()
    key = PKCS1_v1_5.new(pubKey[i])
    Enc.append(base64.b64encode(key.encrypt(flag[19 * i : 19 * (i + 1)])))
    print Enc[i]
