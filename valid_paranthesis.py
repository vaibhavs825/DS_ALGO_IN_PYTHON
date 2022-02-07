abc = "asdbcd(cpk<346>) [{125}]"
a = list()
op = ["(","<","[","{"]
cl = [")",">","]","}"]
d = {key:value for key,value in zip(cl,op)}

def func(abc):
    for i in abc:
        if i in op:1
        elif i in cl:
            if a.pop()!=d[i]:
                return -1
    if len(a)!=0:
        return -1
    else:
        return 1

print(func(abc))
