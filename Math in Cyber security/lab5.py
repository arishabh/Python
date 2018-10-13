def letter_to_num(c):
    if (ord(c)>= ord('A') & ord(c)<= ord('Z')):
        return (ord(c) - 65)
    if (c == ' '):
        return 54
    else:
        return (ord(c) - 75)

def num_to_letter(n):
    return (chr(n+65))

def text_to_nums(m):
    num = []
    for i in range (len(m)):
        num.append(letter_to_num(m[i]))
    return (num)

def nums_to_text(l):
    letter = []
    for i in range (len(l)):
        letter.append(num_to_letter(l[i]))
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
    print (encryptednum)
    data = nums_to_text(encryptednum)
    return data
        
def add_inv_26(a):
    if (a == 0):
        return 0
    else:
        return (26-a)

def multiply_mod_26(arr, k):
    numbers = []
    for num in arr:
        numbers.append((num*k)%26)
    print(numbers) 

def decrypt(k,m):
    num = text_to_nums(m)
    print(num)
    k_inv = add_inv_26(k)
    print(k_inv)
    decryptednum = map_add_26(k_inv, num)
    print (decryptednum)
    data = nums_to_text(decryptednum)
    print (data)
    return(''.join(data))
           


    
    
        
