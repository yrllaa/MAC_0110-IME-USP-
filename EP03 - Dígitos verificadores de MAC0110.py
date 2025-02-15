# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS E ATRIBUTOS
# NÃO APAGUE OS DOCSTRINGS
#------------------------------------------------------------------
     
'''
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

'''

# escreva seu programa a seguir

n = int(input("Digiite n: "))

natu = n
ac1 = 1
ac2 = 0
soma1 = 0
soma2 = 0
acs1 = 0
acs2 = 0
pot = 1
i = 0
r = 0
while natu != 0:
    if n // pot != 0:
        pot = pot *10
        i = i + 1
        w = i - 1
    else:
        dig = natu // 10 ** (w)
        soma1 = dig*ac1
        soma2 = dig*ac2
        acs1 = soma1 + acs1
        acs2 = soma2 + acs2
        r = acs2
        natu = natu - dig*10**(w)
        w = w - 1
        ac1 = ac1 + 1
        ac2 = ac2 + 1
        dv1 = acs1%11
        dv2 = acs2%11
        
        if dv1 == 10:
            dv1 = 0
        else:
            dv1 = acs1%11
        if dv1 != 0:
            l = dv1*i
            r = acs2 + l
            dv2 = r%11
            
        else:
            dv2 = acs2%11
        if dv2 == 10:
            dv2 = 0
        else:
            dv2 = dv2
        
print(f"DV= {dv1} {dv2}")