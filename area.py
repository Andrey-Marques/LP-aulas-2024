a,b,c = map(float,input().split())
trian_r = (a*c)/2
print(f'TRIANGULO: {trian_r:.3f}')
#área do circulo
pi = 3.14159
circ = pi * (c*c)
print(f'CIRCULO: {circ:.3f}')
#area do trapézio
trape = (a+b)*c/2
print(f'TRAPEZIO: {trape:.3f}')
#area do quadrado
quad = b*b
print(f'QUADRADO: {quad:.3f}')
#area do retângulo
ret = a*b
print(f'RETANGULO: {ret:.3f}')