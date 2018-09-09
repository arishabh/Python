def gcd(divident, divisor):
    r = 1
    while (r != 0):
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
            while (r >= divisor):
                r = divident - divisor
                divident = r
            r = r * count * count1
            
        #print ("Remainder is: ",r)
        divident = divisor
        divisor = r
    print("The gcd is: ",divident)
