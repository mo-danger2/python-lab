def largest(l):
    myMax = l[0]
    for num in l:
        if myMax < num:
            myMax = num
    return myMax

result1 = largest([1, 2, 3, 4, 0])
print(result1)
result2 = largest([10, 4, 2, 231, 91, 54])
print(result2)