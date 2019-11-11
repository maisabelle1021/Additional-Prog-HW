def squaresum(a):
    sum_total =0
    for i in range(1,a+1):
        num = pow(i,2)
        sum_total = sum_total + num
        i+=1
        
    return sum_total