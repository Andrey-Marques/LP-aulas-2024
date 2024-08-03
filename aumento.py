sal = float(input())
if sal<=400.00:
    reaju=sal*(15/100)
    saln=sal+reaju
    por=15
elif sal>=400.01 and sal<=800.00:
    reaju=sal*(12/100)
    saln=sal+reaju
    por=12
elif sal>=800.01 and sal<=1200.00:
    reaju=sal*(10/100)
    saln=sal+reaju
    por=10
elif sal>=1200.01 and sal<=2000.00:
    reaju=sal*(7/100)
    saln=sal+reaju
    por=7
elif sal>2000.00:
    reaju=sal*(4/100)
    saln=sal+reaju
    por=4
print(f'Novo salario: {saln:.2f}')
print(f'Reajuste ganho: {reaju:.2f}')
print(f'Em percentual: {int(por:.2f)} %')