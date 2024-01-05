enc_flag = [110, 102, 118, 102, 115, 114, 118, 130, 103, 104, 92, 80, 98, 108, 63, 63, 65, 112, 113, 144]

arr = [] 

for i,j in enumerate(enc_flag):
    arr.append(chr(j))

print(enc_flag)

print(arr)

print(*arr)

s = ''.join(arr)

print(s)

print(len(arr))

flag = 'nfvfsrvgh\Pbl??Apq'

ord_arr = []

for i in flag:
    ord_arr.append(ord(i))

print(flag)
print(ord_arr)