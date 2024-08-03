valor = float(input())
c100,c50,c20,c10,c5,c2,m1,m50,m25,m10,m5,m01 = 0,0,0,0,0,0,0,0,0,0,0,1
if valor >= 0.00 and valor <= 1000000.00: 
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
    #-----------moedas------------------
    while valor >= 1:
        valor -= 1
        m1 += +1
    while valor >= 0.50:
        valor -= 0.50
        m50 += +1 
    while valor >= 0.25:
        valor -= 0.25
        m25 += +1
    while valor >= 0.10:
        valor -= 0.10
        m10 += +1
    while valor >= 0.05:
        valor -= 0.05
        m5 += +1
    while valor >= 0.01:
        valor -= 0.01
        m01 += 1
print('NOTAS:')
print(f'{c100} nota(s) de R$ 100.00')
print(f'{c50} nota(s) de R$ 50.00')
print(f'{c20} nota(s) de R$ 20.00')
print(f'{c10} nota(s) de R$ 10.00')
print(f'{c5} nota(s) de R$ 5.00')
print(f'{c2} nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{m1} moeda(s) de R$ 1.00')
print(f'{m50} moeda(s) de R$ 0.50')
print(f'{m25} moeda(s) de R$ 0.25')
print(f'{m10} moeda(s) de R$ 0.10')
print(f'{m5} moeda(s) de R$ 0.05')
print(f'{m01} moeda(s) de R$ 0.01') 