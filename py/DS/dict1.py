#dict with list
#dict with multiple values
stud ={
    "one" :["id0001", 26, "a"],
    "two" :["id0002", 31, "c"],
    "three" :["id0003", 30, "s"],
    "four" :["id0004", 29, "b"],
}
print (stud)
print (stud["one"])
print (stud["one"][1:])

stud1 ={
    "one" :{"id": "id0001", "age": 26, "grade" :"a"},
    "two" :{"id": "id0002", "age": 31, "grade" :"c"},
    "three" :{"id": "id0003", "age": 30, "grade" :"s"},
    "four" :{"id": "id0004", "age": 29, "grade" :"b"}}

print (stud1)
print (stud1["three"]["age"])
print (stud1["two"]["id"],stud1["two"]["grade"])