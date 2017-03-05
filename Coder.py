
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    l= string.ascii_lowercase
    h= string.ascii_uppercase
    t= h+l
    
    l= l*2
    h= h*2
    
    lowV= range(26)
    hiV= range(26)

    i= 0
    j= 0
    while i+shift<26+shift:
        lowV[i]= l[i+shift]
        i+=1

    while j+shift<26+shift:
        hiV[j]= h[j+shift]
        j+=1
    t1= hiV+lowV

    d= {}
    k=0
    while k< 26*2:
        d[t[k]]= t1[k]
        k+=1
    return d
