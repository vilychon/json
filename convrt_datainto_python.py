# write a program to convert json data into python objects?
import json
a='{"Name":"David","class":"5","age":13}'
b=json.loads(a)
print(b)
print("Name:",b["Name"])
print("class:",b["class"])
print("age:",b["age"])
