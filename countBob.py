#COUNTING BOBS. PS1  
#Assume s is a string of lower case characters.
#Write a program that prints the number of times the string 'bob' occurs in s

b= 'bob'
count = 0
number = 0
while count< len(s)-2:
    if s[count:count+3] == 'bob':
        number+=1
    count += 1
print 'Number of times bob occurs is:', number
