
#Use cases : str = "aabcd", "abcdef", "aabbccdd"
string = "aabc"
arr = [0]*26
arr2=[]
dist=0
for j in range(0,len(string)):
  count=0
  for h in range(0,len(arr2)):
    if string[j]==arr2[h]:
      count+=1
  if count==0:
    arr2.append(string[j])
    dist+=1
    for k in range(0,dist):
      arr[k]+=len(string)-j
arr3=[]
arr4=[0]*26
dist=0
for t in range(0,len(string)):
  count=0
  j=len(string)-t-1
  for h in range(0,len(arr3)):
    if string[j]==arr3[h]:
      count+=1
  if count==0:
    arr3.append(string[j])
    dist+=1
    for k in range(0,dist):
      arr4[k]+=len(string)-j
print (arr)
print(arr4)





'''

why arr2 is zero ??
arr2 to store distinct values

arr = [ 0, 0, 0 ...] 26 times. 

Then for the first iteration it will not enter the second loop 
first value is distinct loop me nahi jane ka jaroorat
ok, so we skip that loop and go to if condition and add the value jaroorath

since we have len ==4 so for this particular case we will iterate over 0,1,2,3  not 4. 

lets evalute the case when we have j=0

is it correct for j=0 ?? yes

so, after incresing the count we do nothing ? wo add karna Bacha hai
It looks like we are standing at a place and we haev list of vaiables to match. So we are just iterating over it and if match found we increase. 

What about using IN operator instead of For ??
IN for loop hi use karta na?But the code looks easy to understand. 
Haan wo hai. 
Code readability is also important
Interview me lekin better hota kya functions use karna? I think is as far a you communicate the purpose of using a particular pre defined function and knows how it works. 
It should be fine.
wahi. Matlab exact pata hona jaroori hai. IN ka hm sure nahi
But in terms of efficieny may be better hoga. Memory management bhi better ho saktha hai 
Haan wo hai
Going for dinnr 

arr = [4]
arr2= ['a']


Iterating over  [ 0,1,2,3]:
j=0 
  count = 0
  arr2= ['a']
  dist = 1

  iter over [0]
    arr[0]= 4

j=1

  count =0 

  iter over [0]:
    string[1] = a
    arr2 [ 0] = a
    so, count =1 

'''