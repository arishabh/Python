def div (divident, divisor):
    count = 1
    count1 = 1
    if (divisor < 0):
        divisor = -1 * divisor
        count = -1
        
    if (divident < 0):
        divident = -1 * divident
        count1 = -1
    if (divisor == 0):
        print("DivisionByZero error!")
        
    else:
        r = divident
        q = 0
        while (r >= divisor):
            r = divident - divisor
            q = q + 1
            divident = r
        q = q * count * count1
        r = r * count * count1 

    print ("The the Quotient is: ",q)
    print ("Remainder is: ",r)
