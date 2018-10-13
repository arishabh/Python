if (__name__ == '__main__'):
  import doctest
  doctest.testmod(optionflags= doctest.NORMALIZE_WHITESPACE)
  
def text_to_nums(m):
    num = []
    for i in range (len(m)):
        num.append(ord(m[i]) - 65)
    return (num)

def nums_to_text(l):
    letter = []
    for i in range (len(l)):
        letter.append(chr(l[i]+65))
    return (''.join(letter))

def add_26(a,b):
    return ((a+b)%26)

def map_add_26(k,l):
    encarr = []
    for i in range (len(l)):
        encarr.append(add_26(k, l[i]))
    return (encarr)
        
def add_inv_26(a):
    if (a == 0):
        return 0
    else:
        return (26-a)

def multiply_mod_26(arr, k):
    numbers = []
    for num in arr:
        numbers.append((num*k)%26)
    return numbers

def add_enc(m,k):
    num = text_to_nums(m)
    encryptednum = map_add_26(k, num)
    data = nums_to_text(encryptednum)
    return data

def add_dec(m,k):
    num = text_to_nums(m)
    k_inv = add_inv_26(k)
    decryptednum = map_add_26(k_inv, num)
    data = nums_to_text(decryptednum)
    return(''.join(data))

def add_count(l, n):
    l[n] += 1
    return l

def get_frequency(text):
    freq = [0]*26
    num = text_to_nums(text)
    for number in num:
        add_count(freq, number)
    return freq

def get_largest_index(l):
    return l.index(max(l))

def crack_additive(text):
    frequency = get_frequency(text)
    largest = get_largest_index(frequency)
    return (largest - 4)%26

def mul_inv(n):
  for i in range(1, 26):
    if (i*n%26==1):
      return i
    
def mul_enc(text, key):
    nums = text_to_nums(text)
    mult = multiply_mod_26(nums, key)
    encrypted = nums_to_text(mult)
    return encrypted

def mul_dec(text, key):
    nums = text_to_nums(text)
    mult = multiply_mod_26(nums, mul_inv(key))
    decrypted = nums_to_text(mult)
    return decrypted
    
def affine_enc(text, s, r):
    add = add_enc(text, r)
    encrypted = mul_enc(add, s)
    return encrypted

def affine_dec(text, s, r):
    mult = mul_dec(text, s)
    decrypted = add_dec(mult, r)
    return decrypted

def get_second_largest_index(l):
    l.remove(max(l))
    return l.index(max(l))

def solve(x, y):
    inv = mul_inv(15)
    s = (inv*((y-x)%26))%26
    r = (((mul_inv(s)*x)%26)-4)%26
    return s, r
    
def crack_affine(text):
    freq = get_frequency(text)
    x = get_largest_index(freq)
    y = get_second_largest_index(freq)
    return solve(x, y)
           
