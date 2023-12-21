# Segunda Aula
'''
Primeiro Código
Trabalhar as variáveis
Explicar sobre as variáveis
dar exemplo da prateleira 
Falar também sobre os comentarios usando # jogo da velha
Se usar comentários multilinhas utiliza 3 aspas como intervalo de linhas 


'''

# variáveis

# 1. Variáveis

idade = 26 # aqui estou criando uma variável  # = significa recebe # 26 
# leia idade recebe 26
# o python já reconhece o 26 como número inteiro, pq ela tem tipagem dinâmica

# imprimir a idade 

print (idade)

nome = 'Carvalho'  # criando outra variável 
# note que agora foi utilizado o aspas pra mesagem pois se trata de um string
# vamos já aprender sobre tipos de variáveis 
# Agora vamo imprimar a variável nome

print ('nome') # note o que aecontece se colocar a variável entre aspas

print (nome) # agora sem aspas, ou seja toda variável não é um string

# podemos limpar o terminal pra despoluir digitando clear ou cls

# vamos agora para os tipos de variáveis

# Tipos de variáveis
'''
1. int = Números inteiros, ou seja, sem parte decimal = 1, 2, 100 , 300
2. float = Números reais, ou seja, com parte decimal = 0.2 ; 1.7 ; 2.0
3. str = cadeias de caractéres, ou seja , dados textuais (string)
4. bool = Valores lógicos (booleanos) = True ou False # muito util para fazer comparação

Agora vamos testar essas variáveis 
'''
idade = 44
Altura = 1.81
nome = 'Claudio Carvalho'
estudando = True  
# lembrar que tem que escrever (True e False) com letra maiuscula
# NO python tem o 'Case Sensitive' ele indica o erro

# Agora como fazemos para visualizar o tipo dessa variável?

print (type(idade))  # imprime o tipo da variável idade
print (type(Altura))
print (type(nome))
print (type(estudando))


# Agora sim podemos resolver o problema da aula anterior
# Qual seria o problema?  não está salvando a resposta do usuário

# Obtendo os dados do usuário e salvando em variáveis
# Vamos refazer a pergunta?

input('Qual é a linguagem de programação que vc está estudando?') 
# quando for pedir a informação para dar entrada 
# o usuário vai responder e para onde vai essa informação
# tenho que criar uma variável para armazenar a informação

linguagem = input('Qual é a linguagem de programação que vc está estudando?') 
# linguagem recebe input ( a pergunta que estamos fazendo aqui)
# vamosa testar

print (' A linguagem que vc está estudando é',linguagem)

# Agora faca a sguinte atividade
# crie as variáveis

nome = input('Qual é o seu Nome?') 
idade = input('Qual é a sua idade?')
altura = input('Qual é a sua altura?')

# depois imprima utilizando todas as variáveis juntas

print ('Seu nome é', nome , 'você tem', idade, 'anos' , 'e', altura, 'de altura')p
