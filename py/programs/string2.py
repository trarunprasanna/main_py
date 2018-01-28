name="arunprasanna"
print (name[0])
print (len(name))
#variablename [start:end:step]
print (name[4:8:1])
print (name[4:])
print (name[4::2])
print (name[:2])
print (name[::-1])#it reverse the string

print (name[-2])
#index
print (name[name.index("pra"):name.index("sa")])

mail="arunprasanna@gmail.com"
ven= (mail[mail.index("@"):mail.index(".")])
print (ven[1::])