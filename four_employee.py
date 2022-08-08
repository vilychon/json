import json
a=["neelam","programer","24","2400",]
b=["komal","trainer","24","20000"]
c=["anuradha","HR","25","40000"]
d=["Abhishek","manager","29","63000"]
e=["name","designation","age","22"]
dic={}
dic1={}
dic2={}
dic3={}
dic4={}
i=0
while i<len(a):
    dic1[e[i]]=a[i]
    dic2[e[i]]=b[i]
    dic3[e[i]]=c[i]
    dic4[e[i]]=d[i]
    i=i+1
dic["emp"]=dic1
dic["emp"]=dic2
dic["emp"]=dic3
dic["emp"]=dic4
with open("meraki8.json","w") as f:
    y=json.dump(dic,f,indent=4)
f.close()
 