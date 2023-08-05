from itertools import combinations

def anagram_checker(a,b):
    ht = dict()

    if len(a) == len(b):
        for i in a:
            if i in ht:
                ht[i] += 1
            else:
                ht[i] = 1
        #print(ht)
        for i in b:
            if i in ht:
                ht[i] -= 1
            else:
                ht[i] = 1
        #print(ht)
        for i in ht:
            if ht[i] != 0:
                return False,None
        return True,"".join(ht)
    else:
        #print('string length does not match, so definitely not an anagram')
        return False,None

lst=['row','a','wor','test','ttes','tset']

grp={}

for s1,s2 in combinations(lst, 2):  
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    x,y=anagram_checker(s1,s2)
    if x:     
        if y in grp:
            if s1 not in grp[y]:
                grp[y].append(s1)
            elif s2 not in grp[y]:
                grp[y].append(s2)
        else:
            grp[y] = [s1,s2]
    #print(s1,s2,y)
print(grp)
