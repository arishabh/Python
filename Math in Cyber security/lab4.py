from __future__ import print_function
if (__name__ == '__main__'):
  import doctest
  doctest.testmod(optionflags= doctest.NORMALIZE_WHITESPACE)
  
def ext_eud(a, b):
    qs = [0,0]
    rs = [a,b]
    xs = [1,0]
    ys = [0,1]
    while (rs[-1] != 0):
        q = rs[-2] // rs[-1]
        r = rs[-2] % rs[-1]
        x = xs[-2] - (q*xs[-1])
        y = ys[-2] - (q*ys[-1])
        qs.append(q)
        rs.append(r)
        xs.append(x)
        ys.append(y)
    return(qs, rs, xs, ys)

def ext_eud_display(a, b):
    qs = [0,0]
    rs = [a,b]
    xs = [1,0]
    ys = [0,1]
    while (rs[-1] != 0):
        q = rs[-2] // rs[-1]
        r = rs[-2] % rs[-1]
        x = xs[-2] - (q*xs[-1])
        y = ys[-2] - (q*ys[-1])
        qs.append(q)
        rs.append(r)
        xs.append(x)
        ys.append(y)
    print('gcd({0},{1})={2}={3}*{0}={4}*{1}'.format(a,b,rs[-2],xs[-2],ys[-2]))

def filter_multiple(n, l):
    return filter(doesnt_divide, l)

def sieve(n):
    res = []
    l = range
    
    
