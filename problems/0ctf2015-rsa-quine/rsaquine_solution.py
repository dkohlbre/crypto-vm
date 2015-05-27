import socket
import telnetlib
from subprocess import Popen, PIPE
from fractions import gcd


def recv_until(s, string):
    buf = ""
    while not buf.endswith(string):
        r = s.recv(1)
        buf += r
        if len(r) == 0:
            print "remote server terminated connection: '%s'" % buf
            raise socket.error
    return buf[:-len(string)]


def interact(s):
    t = telnetlib.Telnet()
    t.sock = s
    t.interact()
    exit()


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a / b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


def chinese_remainder(n, a):
    lena = len(a)
    p = i = prod = 1; sm = 0
    for i in range(lena): prod *= n[i]
    for i in range(lena):
        p = prod / n[i]
        sm += a[i] * mul_inv(p, n[i]) * p
    return sm % prod

s = socket.create_connection(("202.112.26.105", "55537"))


for h in range(1, 31):
    recv_until(s, "N = ")
    n = int(recv_until(s, "\n"))

    recv_until(s, "e = ")
    e = int(recv_until(s, "\n"))

    recv_until(s, "Total ")
    cnt = int(recv_until(s, " "))

    print "Round %d: e = %d, N = %d, total: %d" % (h, e, n, cnt)

    quines = set([0, 1, -1 % n])

    factors = []
    output = Popen(["./msieve", "-v", str(n)], stdout=PIPE).communicate()[0]
    for line in output.split("\n"):
        if "factor:" in line:
            factors.append(int(line.split("factor: ")[1]))
    p, q = factors

    mod_p = [0] + [(i+1)*(p-1)/gcd(e-1, p-1) for i in range(gcd(e-1, p-1))]
    mod_q = [0] + [(i+1)*(q-1)/gcd(e-1, q-1) for i in range(gcd(e-1, q-1))]

    print mod_p
    print mod_q

    for g in xrange(3, 1000, 2):
        for mp in mod_p:
            for mq in mod_q:
                quine = chinese_remainder([p, q], [pow(g, mp, p), pow(g, mq, q)])
                quines.add(quine)

        for mp in mod_p:
            quine = chinese_remainder([p, q], [pow(g, mp, p), 0])
            quines.add(quine)

        for mq in mod_q:
            quine = chinese_remainder([p, q], [0, pow(g, mq, q)])
            quines.add(quine)

    print quines, len(quines)
    for i, quine in enumerate(quines):
        s.send(str(quine).replace("L", "")+"\n")
        print s.recv(100)
        if i == 199:
            break

interact(s)
