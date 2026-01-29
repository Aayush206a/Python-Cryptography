def matrix(key):


    key = ''.join(dict.fromkeys(key.upper().replace('J','I').replace(' ','')))

    alpha = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    key += ''.join(c for c in alpha if c not in key)

    return [list(key[i:i+5]) for i in range(0,25,5)]


def pos(m,c):

    for i in range(5):

        for j in range(5):

            if m[i][j]==c: return i,j


def prep(t):

    t=t.upper().replace('J','I').replace(' ','')

    r,i="",0

    while i<len(t):

        r+=t[i]

        if i+1<len(t) and t[i]==t[i+1]: r+='X'

        else:

            if i+1<len(t): r+=t[i+1]; i+=1

        i+=1

    return r+'X' if len(r)%2 else r


def playfair(t,key,enc=True):

    m,res=matrix(key),""

    t=prep(t) if enc else t.upper()

    for i in range(0,len(t),2):

        r1,c1=pos(m,t[i]); r2,c2=pos(m,t[i+1])

        if r1==r2:

            res+=m[r1][(c1+(1 if enc else -1))%5]+m[r2][(c2+(1 if enc else -1))%5]

        elif c1==c2:

            res+=m[(r1+(1 if enc else -1))%5][c1]+m[(r2+(1 if enc else -1))%5][c2]

        else:

            res+=m[r1][c2]+m[r2][c1]

    return res


c=input("1:Encrypt 2:Decrypt: ")

k=input("Key: ")

t=input("Text: ")

print(playfair(t,k,c=='1'))