p1,c1,p2,c2 = map(int,input().split())
es = p1*c1
di = p2*c2
if es == di:
    print(0)
elif es>di:
    print(-1)
elif(es<di):
    print(1)