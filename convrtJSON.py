# import json

# # some JSON:
# x =  '{ "name":"John", "age":30, "city":"New York"}'

# # parse x:
# y = json.loads(x)

# # the result is a Python dictionary:
# print(y["age"]) 

import json
json1='{"platform":"nokia","ip":"1.2.3.4"}'
dict1=json.loads(json1)
print(type(dict1))