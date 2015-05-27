#!/opt/sage-6.2-x86_64-Linux/sage -python

import sys
sys.path.insert(1, "/usr/lib/python2.7/dist-packages")
import pexpect
from pexpect import fdpexpect

from sage.all import *

DEBUG = False

def get_primes(N):
    primes = []
    for f,c in factor(N):
        primes.extend([f]*c)
    return primes

manual_quines = lambda p, e: [i for i in range(p) if pow(i,e,p)==i]


def get_quines_for_prime(p, e):
    k = e-1
    order = gcd(p-1,k % (p-1))
    g = GF(p).multiplicative_generator()
    kth_primitive_root= int(pow(g, (p-1)/order, n))
    roots =  more_roots(kth_primitive_root, p, k)
    return roots.union(set([0]))

def more_roots(r, p, k):
    roots = set([r])
    cur = r
    while True:
        cur = (cur * r) % p
        if cur in roots:
            break
        roots.add(cur)
    return roots

def get_quines(N, e, nq):
    """return a set of nq numbers q with
    q**e = q (mod N)."""
    print "factoring N (%d bits)" % floor(log(N,2))
    p,q = get_primes(N)
    print "gen_quines p"
    p_quines = get_quines_for_prime(p, e)
    print "gen_quines q"
    q_quines = get_quines_for_prime(q, e)
    print "combine"
    quines = set()
    for rp in p_quines:
        for rq in q_quines:
            try:
                r = CRT([rp, rq], [p,q])
            except Exception, e:
                print [rp,rq], [p,q]
                raise e

            #quines.update(more_roots(r, N, e-1))
            quines.add(r)
            assert pow(r,e,N) == r
            if len(quines) == nq:
                break
        if len(quines) == nq:
            break
    print "generated %d quines" % len(quines)
    return quines


import socket
#sys.path.append("/usr/local/lib/python2.7/dist-packages")
#import pexpect.fdpexpect

def main():
    qs = get_quines(N=50429, e=13567, nq = 10277)
    assert len(qs) == 10277

    s = socket.socket()
    s.connect(("202.112.26.105", 55537))
    c = pexpect.fdpexpect.fdspawn(s)
    m = c.expect("([0-9]+) Rounds")
    rounds = int(c.match.groups()[0])
    print "%d rounds" % rounds

    for i in xrange(rounds):
        print
        print "==== Round (%u/%u) ===" % (i+1, rounds)
        print
        c.expect("N = ([0-9]+)")
        N = int(c.match.groups()[0])
        c.expect("e = ([0-9]+)")
        e = int(c.match.groups()[0])
        c.expect("Total ([0-9]+) quine numbers")
        nq = int(c.match.groups()[0])
        print "N = ", N
        print "e = ", e
        print "%d quines total" % nq
        if nq > 200:
            nq = 200
        print "%d quines required" % nq
        qs = get_quines(N, e, nq)
        assert len(qs) >= nq
        for i, q in enumerate(list(qs)[:nq]):
            s.send("%d\n" % q)
            if DEBUG:
                res = c.expect(["Good Quine", "Bad Number", "Do not cheat"])
                assert res == 0

    c.expect("N = ([0-9]+)")
    N = int(c.match.groups()[0])
    c.expect("e = ([0-9]+)")
    e = int(c.match.groups()[0])
    c.expect("Flag = ([0-9]+)")
    flag = int(c.match.groups()[0])
    print "FLAG", N, e, flag


if __name__ == '__main__':
    main()

