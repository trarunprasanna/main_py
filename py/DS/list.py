#list

l1=[12,4,12,45,223,7,"a","s",True]
print (l1)
print (type(l1))
print (l1[4])
print (l1[-1])
name = l1[-2]
print (name)
#list[start:end:step]
print (l1[0:3])

l2 = [1,2,3,4,[5,6,7,],8,9,0]
print (l2)
print (l2[4])
print (l2[4][1])# it print the inner list 1 st position
print (l2[4][1:])# it print the inner list 1st position ansd rest


l3=[ [1,2,3], [4,5,6], [7,8,9]]
print (l3)
print (l3[2])
print (l3[2][0])
print (l3[2][0:2:1])