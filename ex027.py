nome = input('Digite seu nome completo:').strip()
dividido = nome.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(dividido [0]))
print('Seu último nome é {}'.format(dividido[len(dividido)-1]))
