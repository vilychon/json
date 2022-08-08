import json
a={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}
s=sorted(a.keys())
e={}
for i in s:
    for k in a:
        if k==i:
            e[i]=a[k]
f=open("meraki4.json","w")
y=json.dump(e,f,indent=2)
f.close()
