arr = [3,3,3,1,4,4,4,5,5,5]
res = 0
i = 0
while i<8: #因为arr中每个数都在8位标识范围之内 统计每一个二进制位
    j = 0
    count = 0
    while j < len(arr):
        count += (arr[j] >> i) & 1 #统计每个数二进制第i位上是1数量之后
        j+=1
    #因为同一个数字出现了三次 那么他们的二进制相同位上1的个数则是3的倍数。
    #%3之后 剩下的1就是只出现一次的数对应位上的1
    #把各个位上的1组合起来 就是那个数
    res |=count % 3 << i
    i+=1
print(res)

