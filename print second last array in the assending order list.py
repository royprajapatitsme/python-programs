ls = [int(i) for i in input("Enter the array :").split()]
ls2 = []

for i in ls:
    if i not in ls2:
        ls2.append(i)

element = max(ls2)
ls2.remove(element)
ls2.sort
out = max(ls2)
print(out)
