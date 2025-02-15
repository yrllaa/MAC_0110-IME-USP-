# -*- coding: utf-8 -*-
# ------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS E ATRIBUTOS
# NÃO APAGUE OS DOCSTRINGS
# ------------------------------------------------------------------

"""
    Nome: Yrlla Mariana Vieira de França
    NUSP: 11276412

    Ao preencher esse cabeçalho com o meu nome e o meu número USP,
    declaro que todas as partes originais desse exercício programa (EP)
    foram desenvolvidas e implementadas por mim e que portanto não
    constituem desonestidade acadêmica ou plágio.
    Declaro também que sou responsável por todas as cópias desse
    programa e que não distribui ou facilitei a sua distribuição.
    Estou ciente que os casos de plágio e desonestidade acadêmica
    serão tratados segundo os critérios divulgados na página da
    disciplina.
    Entendo que EPs sem assinatura devem receber nota zero e, ainda
    assim, poderão ser punidos por desonestidade acadêmica.

    Abaixo descreva qualquer ajuda que você recebeu para fazer este
    EP.  Inclua qualquer ajuda recebida por pessoas (inclusive
    monitores e colegas). Com exceção de material de MAC0110, caso
    você tenha utilizado alguma informação, trecho de código,...
    indique esse fato abaixo para que o seu programa não seja
    considerado plágio ou irregular.

    Exemplo:

        A monitora me explicou que eu devia utilizar a função int() quando
        fazemos leitura de números inteiros.

        A minha função quicksort() foi baseada na descrição encontrada na
        página https://www.ime.usp.br/~pf/algoritmos/aulas/quick.html.

    Descrição de ajuda ou indicação de fonte:

"""

##################################################################

# leitura da coordenada em x, y
x = float(input("Digite x: "))
y = float(input("Digite y: "))

## ESCREVA O RESTO DO SEU PROGRAMA ABAIXO USANDO x, y
dentro = False 



if -3 <= x <= 3 and -2 <= y <= 2:
    dentro = True
    if -3 <= x < -2 and -2 <= y < -1:
        dentro = False
    if 2 < x <= 3 and 1 < y <= 2:
        dentro = False
    if -2.5 <= x <= -1.5 and 0.5 <= y <= 1.5:
        dentro = False
        if -2.25 <= x <= -1.75 and 0.75 <= y <= 1.25 :
            dentro = True 
    if 1 < x < 1.5 and 1 < y < 1.5 :
        dentro = False 
    if 1.5 <= x <= 2.5 and -1.5 <= y <= -0.5:
        dentro = False
        if 1.75 <= x <= 2.25 and -1.25 <= y <= -0.75:
            dentro = True
    if -1 <= x <= 1 and -1 <= y <= 1:
        dentro = True 
       # if 0.5 <= x**2 + y**2 < 1:
        #    dentro = False
        if 0.25 <= x**2 + y**2 < 1:
            dentro = False
        if x**2 + y**2 < 0.25:
            dentro = True
        
           
    
if dentro:
    print("acertou")
else:
    print("errou")