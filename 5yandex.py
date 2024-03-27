def n_p(n, p):
    a = '0123456789'
    ans = ''
    while n > 0 :
        ans = a[n%p] + ans
        n //=p
    return ans
#https://education.yandex.ru/ege/variants/7e480ec2-3b8f-4261-83ac-f01cee1cca75/task/5
def f(n):
    t = n_p(n, 3)
    t += n_p((t.count('2')), 3)
    t += n_p((t.count('1')), 3)
    t += n_p((t.count('0')), 3)
    return int(t, 3)
print(f(5))

    
