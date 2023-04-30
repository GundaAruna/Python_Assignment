s1=input("Enter the string: ")
lower=s1.lower()
l1=[]
for i in lower:
    if i not in l1:
        l1.append(i)
print("uniqueLetters",",".join(l1))
