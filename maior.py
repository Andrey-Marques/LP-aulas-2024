a,b,c = map(float,input().split())
maiorAB = (a+b+abs(a-b))/2
maior = (maiorAB+c+abs(maiorAB-c))/2
print(f'{int(maior)} eh o maior')