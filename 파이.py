res = 0
for i in range(100000000000):
    res += ((-1)**i)*(4/(2*i+1))
    print(res)
