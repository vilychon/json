import json
mydict={
    "people":[
        {
            "name":"bob",
            "age":23,
            "weight":78
        },
        {
            "name":"semi",
            "age":26,
            "weight":98
        },
        {
            "name":"ashuni",
            "age":20,
            "weight":72
        },
        {
            "name":"katim",
            "age":56,
            "weight":80
        }
    ]
}
json_string=json.dumps(mydict,indent=2)
with open("mydata.json","w") as f:
    f.write(json_string)