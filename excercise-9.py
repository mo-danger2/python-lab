def occurrences(str, word):
      
    a = str.split(" ")

    count = 0
    for i in range(0, len(a)):
          
      
        if (word == a[i]):
           count = count + 1
             
    return count       

result1= occurrences('fleep floop', 'e')
print(result1)

result2= occurrences('fleep floop', 'p')  
print(result2)

