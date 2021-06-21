s = "huL{SEp^H6?!"
def sxor(s1,s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))
for v10 in range(len(s)):
    x = ""
    for i in range(len(s)):
        x += chr((7 * i + v10) % 126)
    print(sxor(x,s))
