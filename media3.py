n1,n2,n3,n4 = map(float,input().split())
media = ((n1*2)+(n2*3)+(n3*4)+n4)/(2+3+4+1)
if media>=7.0:
    print(f'Media: {media:.1f}')
    print(f'Aluno aprovado.')
elif media<5.0:
    print(f'Media: {media:.1f}')
    print(f'Aluno reprovado.')
elif media>=5.0 and media<=6.9:
    print(f'Media: {media:.1f}')
    exame = float(input())
    print(f'Aluno em exame.')
    mediaf=(media+exame)/2
    if mediaf>=5.0:
        print(f'Nota do exame: {exame:.1f}')
        print(f'Aluno aprovado.')
        print(f'Media final: {mediaf:.1f}')
    else:
        print(f'Nota do exame: {exame:.1f}')
        print(f'Aluno reprovado.')
        print(f'Media final: {mediaf:.1f}')