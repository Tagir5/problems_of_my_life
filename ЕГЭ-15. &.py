def n_p(n, p):
    a = '0123456789'
    ans = ''
    while n > 0:
        ans = a[n%p] + ans
        n //=p
    return ans

def summa(st):
    a = [int(x) for x in st]
    return sum(a)

#solution to problem four (ЕГЭ-15. &)

for a in range(45, 66):
    chek = True
    for x in range(600):
        if ((x & 30 != 0) <= (x & 10 != 0)) or (x & a != 0) <= (x & 10 == 0) and (x & a == 0) and (x & 21 != 0):
           chek = False
        if not(chek):
            break
    if chek: print(a)
        
