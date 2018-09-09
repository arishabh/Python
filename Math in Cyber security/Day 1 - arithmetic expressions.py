# Comments are lines which are not executed.
# Any text following a '#' will be treated as a comment.

##def hello():
##  print('hello!')
##
##def add_two(x):
##  return x + 2
##
##def multiply(x, y):
##  return x * y

##def sound_off():
##  for i in range(0,10):
##    print(i)
##
##def twos_to(n):
##  i = 0
##  while (i < n):
##    print(i)
##    i = i + 2
##
##def fact(n):
##  result = 1
##  for k in range(1,n + 1):
##    result = k * result
##  return result

##def alternative_fact(n):
##  result = 1
##  for k in range(1, n):
##    result = k * result
##  return k * result

#------------------------------------------------------------------------------#

def eqn1_left(n):
    total = 0;
    for a in range (1, 2*n, 2):
        number = a **2
        total = total + number
    print(total)
    return total
def eqn1_right(n):
    total = (n*(4*(n**2) - 1))/3
    print(total)
    return total

def eqn2_left(n):
    total = 0;
    for a in range (2, 2*n+1, 2):
        number = a
        total = total + number
    print(total)
    return total
def eqn2_right(n):
    total = n*(n+1)
    print(total)
    return total

def eqn3_left(n):
    total = 0;
    for a in range (1, n+1):
        number = a**3
        total = total + number
    print(total)
    return total
def eqn3_right(n):
    total = ((n*(n+1))/2)**2
    print(total)
    return total

def eqn4_left(n):
    total = 0;
    for a in range (2, 3*n, 3):
        number = a
        total = total + number
    print(total)
    return total
def eqn4_right(n):
    total = (n*(3*n + 1))/2
    print(total)
    return total

def check_eqn1(n):
  return eqn1_left(n) == eqn1_right(n)

def check_eqn2(n):
  return eqn2_left(n) == eqn2_right(n)

def check_eqn3(n):
  return eqn3_left(n) == eqn3_right(n)

def check_eqn4(n):
  return eqn4_left(n) == eqn4_right(n)
    
