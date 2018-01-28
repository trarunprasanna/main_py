#happy birthday
#0123456
a="happy birthday"
print (a.index("birthday"))
print (a.find("birthday"))

b="000000000000sample text00000000000000"
print (b.strip("0"))
#also strip truncate the space after the input Ex: 'arun  ' it truncate the space after arun
print (b.lstrip("0")) #left
print (b.rstrip("0")) #right
print (len(b)) # len calcuate includieng space

c="arun "
d="arun"
print (len(c))
print (len(d))

name=input("what is ur name :").strip()
print (name,len(name))