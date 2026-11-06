n1=int(input('Digite um valor'))
n2=int(input('Digite outro valor'))
soma=n1+n2
sub=n1-n2
div=n1/n2
mul=n1*n2
#Maneira moderna (.format)
print('A soma entre {} e {} é {}'.format(n1,n2,soma))
print('A subtração entre {} e {} é {}'.format(n1,n2,sub))
print('A divisão entre {} e {} é {}'.format(n1,n2,div))
print('A multiplicação entre {} e {} é {}'.format(n1,n2,mul))
#maneira (%i ou %d,%f,%s)
print('A soma entre %i e %i é: %i'%(n1,n2,soma))
print('A subtração entre %i e %i é: %i'%(n1,n2,sub))
print('A multiplicação entre %i e %i é: %i'%(n1,n2,mul))
print('A divisão entre %i e %i é: %i'%(n1,n2,div))
#maneira (f-string)
print(f'A soma entre o numero {n1} e o numero {n2} é: {soma}')
print(f'A subtração entre o numero {n1} e o numero {n2} é: {sub}')
print(f'A multiplicação entre o numero {n1} e o numero {n2} é: {mul}')
print(f'A divisão entre o numero {n1} e o numero {n2} é: {div}')
























