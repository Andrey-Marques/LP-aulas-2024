cod1,quant1,preco1 = map(float, input().split())
cod2,quant2,preco2 = map(float, input().split())
total = (preco1*quant1)+(preco2*quant2)
print(f'VALOR A PAGAR: R$ {total:.2f}')

