def n_to_p(n, p):
    ar = '012345678'
    num = ''
    while n > 0:
        num = ar[n % p]+num
        n = n//p
    
    return num
        
        
def cng(n):
    n = str(n)
    if int(n[0])%4 == 0:
        n[0] = '9'
    elif int(n[0])%2 == 0:
        n[0] = '3'
        
    if n[0]=='9' and n_to_p(n, 8)[-1]=='4':
        return True
    else:
        return False
        
s = 0
for  k in range(1000, 9999):
    if cng(k):
        s += 1
        
print(s)        

    
    