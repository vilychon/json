# write a program to convert literal objects to string
# import json
# dict={"id":1,"name":"katim","age":22}
# file=open("katim.json","w")
# json.dump(dict,file,indent=3)
# file.close()

import json
dict={"id":1,"name":"katim","age":4}
file=open("katim.json","w")
json.dump(dict,file,indent=2)
file.close()