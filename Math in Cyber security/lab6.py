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

def encrypt(k,m):
    num = text_to_nums(m)
    print(num)
    encryptednum = map_add_26(k, num)
    print(encryptednum)
    data = nums_to_text(encryptednum)
    return data
        
def add_inv_26(a):
    if (a == 0):
        return 0
    else:
        return (26-a)

def decrypt(k,m):
    num = text_to_nums(m)
    k_inv = add_inv_26(k)
    decryptednum = map_add_26(k_inv, num)
    data = nums_to_text(decryptednum)
    return(''.join(data))

def append_new(l,n):
    if n in l:
        return l
    else:
        l.append(n)
        return l

def remove_dup(l):
    final = []
    for i in range (len(l)):
        append_new(final, l[i])
    return final

def extend(l):
    final = remove_dup(l)
    for i in range (26):
        append_new(final, i)
    return final

def cycle1(l):
    l = l[-1:] + l[:-1]
    return l

def cycle(l, n):
    l = l[-n:] + l[:-n]
    return l

def mapping(keyword, letter):
    numbers = text_to_nums(keyword)
    no_dup = remove_dup(numbers)
    extended = extend(no_dup)
    map_by = letter_to_num(letter)
    final = cycle(extended, map_by)
    return final

def find_item (l,n):
    return l[n]

def find_index (l,n):
    return l.index(n)

def enc_list(key,l):
    enc_l = []
    for i in range (len(l)):
        enc_l.append(find_item(key,l[i]))
    return enc_l

def dec_list(key,l):
    dec_l = []
    for i in range (len(l)):
        dec_l.append(find_index(key,l[i]))
    return dec_l

def encryptkey(key, letter, message):
    mapped = mapping(key, letter)
    print(mapped)
    nums = text_to_nums(message)
    encrypted = enc_list(mapped, nums)
    return nums_to_text(encrypted)

def decryptkey(key,letter,ciphertext):
    mapped = mapping(key, letter)
    nums = text_to_nums(ciphertext)
    decrypted = dec_list(mapped, nums)
    return nums_to_text(decrypted)
                    
def multiply_mod_26(arr, k):
    numbers = []
    for num in arr:
        numbers.append((num*k)%26)
    print(numbers) 

#'THEESSENCEOFTHEFREEPRESSISTHERELIABLEREASONABLEANDMORALNATUREOFFREEDOMTHECHARECTEROFTHECENSOREDPRESSISTHENONDESCRIPTCONFUSIONOFTYRANNY'
    
    
    
