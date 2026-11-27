a = [1,2,3,4,5,6,45,312,1,5,7,2,5]
b = []
for i in a:
    c = 0
    #d = 0
    while c==0:
        d = 0
        if i == a[d]:
            c+=1
        else:
            print('нет')
            d+=1
    if c == 0:
        b.append(i)
print(b)