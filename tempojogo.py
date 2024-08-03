# i,mi,f,mf=map(int,input().split())
# if i>f:
#     fim=(24-i)+f
#     if mi<mf:
#         mins=mf-mi
#         print(f'O JOGO DUROU {fim} HORA(S) E {mins} MINUTO(S)')
#     else:
#         mins=60-(mi-mf)
#         fim-=1
#         print(f'O JOGO DUROU {fim} HORA(S) E {mins} MINUTO(S)')
# elif i<f:
#     fim=(i-f)
#     if (i+mi)==(f+mf):
#         fim = 0
#     if fim<0:
#         fim = fim*(-1)
#     if mi<mf:
#         mins=mf-mi
#         print(f'O JOGO DUROU {fim} HORA(S) E {mins} MINUTO(S)')
#     else:
#         mins=60-(mi-mf)
#         print(f'O JOGO DUROU {fim} HORA(S) E {mins} MINUTO(S)')
# elif i==f:
#     if mi<mf:
#         mins=mf-mi
#         print(f'O JOGO DUROU 0 HORA(S) E {mins} MINUTO(S)')
#     else:
#         print(f'O JOGO DUROU 0 HORA(S) E 0 MINUTO(S)')

i, mi, f, mf = map(int, input().split())

inicio_minutos = i * 60 + mi
fim_minutos = f * 60 + mf

if fim_minutos <= inicio_minutos:
    duracao_minutos = (24 * 60 - inicio_minutos) + fim_minutos
else:
    duracao_minutos = fim_minutos - inicio_minutos

duracao_horas = duracao_minutos // 60
duracao_minutos = duracao_minutos % 60

print(f'O JOGO DUROU {duracao_horas} HORA(S) E {duracao_minutos} MINUTO(S)')