sal = float(input())
imp=0
if sal>=0.00 and sal<=2000.00:
    print('Isento')
elif sal>=2000.01 and sal<=3000.00:
    imp=(((sal-2000)*8)/100)
    print(f'{imp:.2f}')
elif sal>=3000.01 and sal<=4500.00:
    imp=(sal*(18/100))
    imp=((1000*8)/100)+(((sal-3000)*18)/100)
    print(f'{imp:.2f}')
elif sal>4500.00:
    imp=((1000*8)/100)+((1500*18)/100)+(((sal-4500)*28)/100)
    print(f'{imp:.2f}')
