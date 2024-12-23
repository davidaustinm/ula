x = 0.2

s = "0."

t = 0.5
N = 64
for i in range(N):
    if x > t:
        x -= t
        s = s + "1"
    else:
        s = s + "0"
    t /= 2.0

print s

r = 0
t = 1.0
s = s[2:]
while len(s) > 0:
    c = s[0]
    s = s[1:]
    t /= 2.0
    if c == "0":
        continue
    else:
        r += t

print r
        


