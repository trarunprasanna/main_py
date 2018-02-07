student = {"arun" : 25, "prasanna" : 32, "three" : 3}
print (student)
print (student["arun"])

# add dict value
student["four"] = 4
print (student)

#change a value in dict
student["arun"]=30
print(student["arun"])
print(student)

dict1 = {'ar': 25, 'two': 2}
print (dict1)

#delete a item in dict
del student["four"]
print(student)

#we can convert the dict to list
a= list(student.keys())
print (a)
print(a[0])

#we can print the values only
print (student.values())
print (list(student.values())[1:])
#dict will not maintain order or index , it always maintain the key and values
# each key and value is called an item

print (student.items())

