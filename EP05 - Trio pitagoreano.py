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

# Escreva seu programa aqui


n = int(input("Digite n: "))
pitagoreano = False
a = 3
b = 4
c = 5
while a < n:
    b = a + 1
    while b < n:
        c = b + 1
        while a + b + c <= n:
            if (a**2 + b**2) == c**2 and a + b + c == n:
                pitagoreano = True
                s = a
                t = b
                u = c
                a = n
                b = n
                c = n
            c = c + 1
        b = b + 1
    a = a + 1
    
if pitagoreano:
    print(f"{n} é pitagoreano: {n} = {s} + {t} + {u}")
else:
    print(f"{n} não é pitagoreano")









