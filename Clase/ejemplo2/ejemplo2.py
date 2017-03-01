str = '12.3, 12.0, 14.5'
prod, i , buffer = 1, 0, ''
print 'str:=' , str
for j in range(len(str)):
    if str[j] == ',':
        buffer = str[i:j]
        print buffer, i , j
        prod = prod * float(buffer)
        i = j + 1
        buffer = ''
buffer = str[i:len(str)]
print buffer, i , len(str)
prod = prod * float(buffer)
print prod