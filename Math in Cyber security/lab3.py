from __future__ import print_function

if (__name__ == '__main__'):
  import doctest
  doctest.testmod()


def remainder(a, b, q):
    r = a - (b * q)
    print ("Remainder is: ",r)
    
