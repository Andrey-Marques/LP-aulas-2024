entrada = int(input())
segundos = 0
minutos = 0
horas = 0
for i in range(0, entrada):
    segundos += 1 
    if segundos == 60:
        minutos += 1
        segundos = 0
    elif minutos == 60:
        horas += 1
        minutos = 0
print(f'{horas}:{minutos}:{segundos}')
