from random import randint

# 01 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi
# o maior e o menor peso lidos.

maior = 0
menor = 10000

for i in range(0,5):
    p = int(input('Digite o peso: '))
    if p > maior:
        maior = p
    if p < menor:
        menor = p
    
print(maior)
print(menor)

# 02 - Crie um programa que pergunte ao usuário um número inteiro e faça a 
# tabuada desse número.

n = int(input('Digite o número desejado para a tabuada: '))

for c in range(0, 11):
    total = c * n
    print(f'{c} x {n} = {total}')

# 03 - Crie um programa que leia o ano de nascimento de sete pessoas. No final, 
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

ano = 0
maior = 0
menor = 0

for ano in range(0, 7):
    nascimento = int(input('Digite o ano de nascimento: '))
    idade = 2021 - nascimento
    if idade < 18:
        menor += 1
    if idade > 18:
        maior += 1
print(f'{maior} pessoas são maior de idade e {menor} são menores de idade')

# 04 - Desenvolva um programa que leia seis números inteiros e mostre a soma 
# apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o. 
# Mostre também quantos valores pares foram digitados.

par = 0
num = 0

for n in range(0, 6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        par +=1
        num += num
print(f'Foram digitados {par} números pares e a some deles é {num}')


# 01 - Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso. (utilizar while sem break)

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
opcao = ''


while opcao != 5:
    opcao = int(input('''
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
'''))  
    if opcao == 1:
        print(n1 + n2)
        
    elif opcao == 2:
        print(n1 * n2)
        
    elif opcao == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
        elif n2 > n1:
            print(f'{n2} é maior que {n1}')
        else:
            print(f'Os números são iguais')
            
    elif opcao == 4:
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
    
print('Fim do Programa')


# 02 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada 
# pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
# No final, mostre:
# A) Quantas pessoas têm mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres têm menos de 20 anos.

maiorIdade = 0
homem = 0
mulher = 0
sair = ''

while sair != 'N':
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Qual seu sexo? [M/F] ')).upper().strip()[0]
    sair = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if idade >= 18:
        maiorIdade += 1
        if sexo in 'M':
            homem += 1
    elif sexo in 'F' and idade < 20:
        mulher += 1
    else:
        break
print(f'''
Maiores de 18 anos = {maiorIdade}
Homens cadastrados = {homem}
Mulheres com menos de 20 anos = {mulher} 
''')    

# 03 - Crie um programa que leia o nome e o preço de vários produtos. 
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# (C) Qual é o nome do produto mais barato.

maisBarato = ''
total = acimaMil = 0
menor = 1000000
continuar = 0
while continuar != "N":
    produto = str(input('Digite o nome do produto: ')).strip()
    preco = float(input('Preço do produto: R$ '))
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    
    
    if preco > 1000:
        acimaMil += 1
    elif preco < menor:
        maisBarato = produto
        menor = preco
    else:
        break

    total += preco
    
print(f'''Total gasto = R$ {total}
Produtos que custam mais de R$ 1.000 = {acimaMil}
Produto mais barato é {maisBarato}, no valor de {menor}''')

# 04 (DESAFIO) Crie um jogo onde o computador vai “pensar” em um número entre 0 e 10. 
# O jogador vai tentar adivinhar qual número foi escolhido até acertar, entre os 
# palpites diga ao jogador se o número do computador é maior ou menor ao que ele 
# digitou,no final mostre quantos palpites foram necessários para vencer

computador = randint(0, 10)
acerto = False
tentativa = 0
while not acerto:
    n = int(input('Digite um número de 0 a 10: '))
    tentativa += 1
    if n == computador:
        acerto = True
        print(f'Você venceu!!! O computador pensou em {n} em você acertou em {tentativa} tentativa(s).')
    else:
        if n < computador:
            print('Maior...')
        elif n > computador:
            print('Menor...')


# 05 (DESAFIO) Em uma eleição presidencial existem quatro candidatos. Os votos 
# são informados por meio de código. 
# Os códigos utilizados são:
# 1 , 2, 3 - Votos para os respectivos candidatos
# (você deve montar a tabela ex: 1 - José / 2- João / etc)
# 5 - Voto Nulo
# 6 - Voto em Branco
# Faça um programa que calcule e mostre:
# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco; 
# A percentagem de votos nulos sobre o total de votos;
# A percentagem de votos em branco sobre o total de votos.

candidato1 = candidato2 = candidato3 = candidato4 = nulo = branco = total = finalizar = 0
votos = ''


while votos != 7:
    urna = int(input('''
    Digite seu voto:
    1 - Lula
    2 - Bolsonaro
    3 - Kalil
    4 - Dória
    5 - Nulo
    6 - Branco
    7 - Finalizar
    '''))
    
    if urna == 1:
        candidato1 += 1
    elif urna == 2:
        candidato2 += 1
    elif urna == 3:
        candidato3 += 1
    elif urna == 4:
        candidato4 += 1
    elif urna == 5:
        nulo += 1
    elif urna == 6:
        branco += 1
    else:
        break
total = candidato1 + candidato2 + candidato3 + candidato4 + nulo + branco

print(f'''
1 - Lula: {candidato1} votos
2 - Bolsonaro:  {candidato2} votos
3 - Kalil:  {candidato3} votos
4 - Dória:  {candidato4} votos
5 - Nulo: {nulo} votos
6 - Branco: {branco} votos
Percentual de votos Nulos: {nulo/total * 100:.2f} %
Percentual de votos em Branco em relação aos nulos: {(branco/nulo * 100):.2f} %
''')