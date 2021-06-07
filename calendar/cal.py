# TODO: Absctract to n selections
def select_subset(elems):
    for a in range(len(elems)):
        for b in range(a+1, len(elems)):
            for c in range(b+1, len(elems)):
                yield [elems[a],elems[b],elems[c]]

def generate_offsets(s):
    for b0 in range(0, s[0]):
        for b1 in range(0, s[1]):
            for b2 in range(0, s[2]):
                yield [(s[0], b0), (s[1], b1), (s[2], b2)]

def histogram(m, b):
    out = set()
    x = 0
    cycle = (m * x) + b
    while cycle < endpoint:
        out.add(cycle)
        x += 1
        cycle = (m * x) + b
    return out

def first_intersection(m1, b1, m2, b2):
    x = 0
    while x < 15:
        x += 1
        a = (m1 * x) + b1
        b = (m2 * x) + b2
        if a == b : return a
    return 0

def lcm(n1, n2, n3):
    out = 1
    while True:
        if out % n1 == 0 and out % n2 == 0 and out % n3 == 0:
            return out

PRIME_FACTORS = [2,2,3,5,7]

endpoint = 1
for x in PRIME_FACTORS:
    endpoint *= x

factors = []
for x in range(2, endpoint):
    if endpoint % x == 0: factors.append(x)
factors = [15,20,21,28,30,35,42]

output = list()
for s in select_subset(factors):
    for funcs in generate_offsets(s):
        h1 = histogram(funcs[0][0], funcs[0][1])
        h2 = histogram(funcs[1][0], funcs[1][1])
        h3 = histogram(funcs[2][0], funcs[2][1])
       
        i1 = h1.intersection(h2)
        i2 = h1.intersection(h3)
        i3 = h2.intersection(h3)
        
        i4 = i1.intersection(i3)
        i1 = i1.difference(i4)
        i2 = i2.difference(i4)
        i3 = i3.difference(i4)

        if len(i1) > 0 and len(i2) > 0 and len(i3) > 0 and len(i4) > 0 and not i1.issubset(i4) and not i2.issubset(i4) and not i3.issubset(i4):
            output.append((i1,i2,i3,i4,funcs))
for o in sorted(output, key=lambda x: next(iter(x[3]))):
    d1 = len(o[0]) - len(o[1])
    d2 = len(o[0]) - len(o[2])
    if (d1 >= 0 and d1 <= 2 and d2 >= 0 and d2 <= 1)\
        or (d1 >= 0 and d1 <= 1 and d2 >= 0 and d2 <= 2)\
        or (d1 <= 0 and d1 >= -2 and d2 <= 0 and d2 >= -1)\
        or (d1 <= 0 and d1 >= -1 and d2 <= 0 and d2 >= -2)\
        or (abs(d1) == 1 and abs(d2) == 1):
        print("%s - %s - %s \t\t\t| %s | %s" % (o[0],o[1],o[2],o[3],o[4]))
