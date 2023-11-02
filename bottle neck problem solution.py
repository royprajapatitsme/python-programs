ls =[int(i) for i in input("Enter the radius of bottle :").split()]
ls2 = []

for i in ls:
    val = ls.count(i)
    ls2.append(val)

print(max(ls2))
