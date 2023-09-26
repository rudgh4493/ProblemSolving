def product(a, b, n):
    if n == 1: 
        return a * b
    
    k = n//2
    ah = a >> k
    al=a - (ah<<k)
    bh =b >> k
    bl=b - (bh<<k)

    m1 = product(ah, bh, k)
    m2 = product(ah + al, bh + bl, k)
    m3 = product(al, bl, k)

    return (m1 << n) + ((m2-m1-m3)<<k) +m3
    
print(product(10,12,4))
