s = 'murcielago'
b = 0
n = 0
x = 0
f = 0
g = 0
letraa = 'a'
letrae = 'e'
letrai = 'i'
letrao = 'o'
letrau = 'u'
for i in range (len(s)):
    if s[i]==letraa:
        b+=1
for i in range(len(s)):
    if s[i]==letrae:
        n+=1
for i in range(len(s)):
    if s[i]==letrai:
        x+=1
for i in range(len(s)):
    if s[i]==letrao:
        f+=1
for i in range(len(s)):
    if s[i]==letrau:
        g+=1
print(b, n, x, f, g) 

