entrada = int(input())
anos = 0
mes = 0
dias = 0
while entrada >= 365:
    entrada -= 365
    anos += 1 
while entrada >= 30:
    entrada -= 30
    mes += 1
    if entrada < 30:
        dias = entrada
print(f'{anos} ano (s)')
print(f'{mes} mes (es)')
print(f'{dias} dia (s)') 