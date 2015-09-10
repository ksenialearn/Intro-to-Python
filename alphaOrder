# PS1 - 3
#Assume s is a string of lower case characters.
#Write a program that prints the longest substring of s in which the letters occur in alphabetical order

s= 'abcdefghijklmnopqrstuvwxyz'
iteration = 0
count = 0
st= s[0]
l2= 0
stLong=''
while iteration < len(s)-1:
    if s[count] <= s[count +1]:
        st= st + s[count +1]
    else:
        l1= len(st)
        if l1>l2:
            stLong= st
            l2= len(stLong)
        st= s[count+1]
    count+= 1    
    iteration+= 1
if len(stLong)< len(st):
    stLong= st
print 'Longest substring in alphabetical order is:', stLong
