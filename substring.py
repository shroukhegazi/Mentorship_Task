s1 = input("Enter first string :")
s2 = input("Enter second string :") 
arr1 =list(range(26))
arr2 =list(range(26))
counter =0

for i in range(0,26):
    arr1[i]=arr2[i]=0

for i in range(len(s1)):
    arr1[ord(s1[i]) - ord('a')]+=1
    
for i in  range(len(s2)):
    arr2[ord(s2[i]) - ord('a')]+=1

for i in range(0, 26):
    if (arr1[i] > 0 and arr2[i] > 0):
        counter +=1    


if (counter>0):
    print("Yes")
else:
    print("No")








