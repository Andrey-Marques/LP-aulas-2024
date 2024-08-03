valor = int(input())
valor2 = valor
c100,c50,c20,c10,c5,c2,c1 = 0,0,0,0,0,0,0
if valor>0 & valor < 1000000: 
    while valor >= 100:
        valor -= 100 
        c100 += 1
    while valor >= 50:
        valor -= 50
        c50 += 1 
    while valor >= 20:
        valor -= 20
        c20 += 1
    while valor >= 10:
        valor -= 10
        c10 += 1
    while valor >= 5:
        valor -= 5
        c5 += 1
    while valor >= 2:
        valor -= 2
        c2 += 1
    while valor >= 1:
        valor -= 1
        c1 += 1
print(valor2)
print(f'{c100} nota(s) de R$ 100,00')
print(f'{c50} nota(s) de R$ 50,00')
print(f'{c20} nota(s) de R$ 20,00')
print(f'{c10} nota(s) de R$ 10,00')
print(f'{c5} nota(s) de R$ 5,00')
print(f'{c2} nota(s) de R$ 2,00')
print(f'{c1} nota(s) de R$ 1,00')