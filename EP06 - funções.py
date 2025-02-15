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

#----------------------------------------------------    
def main():
    n = int(input("Digite n: "))
    k = primo(n)
    w = int(input("Digite w: "))
    l = goldbach(w)
    d = float(input("Digite d: "))
    n0 = float(input("Digite n0: "))
    e = float(input("Digite e: "))
    p = float(input("Digite d: "))
    m0 = float(input("Digite n0: "))
    j = float(input("Digite e: "))
    q = float(input("Digite p: "))
    m = float(input("Digite n: "))
    dd = float(input("Digite d: "))
def primo(k):
    '''(int) -> bool

       Recebe um número inteiro n e retorna True se n é primo.
       Em caso contrário a função retorna False.
    '''
    i = 3
    primo = True
    if k % 2 == 0 or k < 0 or k == 1:
        primo = False
    if k == 2:
        primo = True
    while i < k:
        if k % i == 0:
            primo = False
        i = i + 2
    return primo

#----------------------------------------------------        
def goldbach(l):
    '''(int) -> bool, int, int 

       Recebe um número inteiro n e retorna True se n pode
       ser escrito como a soma de dois nḿeros primos. 
       Nesse caso a função deve retornar dois números primos
       p e q tais que p + q == n.

       Em caso contrário a função retorna False, 0, 0.
    '''
    i = l - 1
    j = 1
    gold = False
    while j <= l:
        c = primo(j)
        t = primo(i)
        if c == True and t == True:
            gold = True
            z = j
            y = i
    
        j = j + 1
        i = i - 1
            
    if gold:
        return gold, y, z
    else:
        return gold, 0, 0
#----------------------------------------------------    
def exponencial(n0, e, p, d):
    '''(int, int, float, int) -> int 

       Recebe 

         * o número `n0` de indivíduos infectados em um dia 0;
         * o número diário médio `e` de indivíduos com quem alguém 
           infectado é exposto;
         * a probabilidade `p` de uma exposição resultar em uma infecção;
         * um inteiro `d`,  d >=  0. 

      Retorna o número total de indivíduos infectados até o dia d 
      determinado por (n0, e, p).
    '''
    nd = ((1 + e*p)**d)*n0    
    return int(nd)
#--------------------------------------------------
def logistica(m0, j, q, m, dd):
    '''(int, int, float, int, int) -> int
 
       Recebe 

         * o número `n0` de indivíduos infectados em um dia 0;
         * o número diário médio `e` de indivíduos com quem alguém 
           infectado é exposto;
         * a probabilidade `p` de uma exposição resultar em uma infecção;
         * o número `n` de indivíduos na população; e
         * um inteiro `d`, d >= 0. 

       Retorna o número total de indivíduos infectados até o dia `d` 
       determinado por (n0, e, p, n).

    '''
    f = 1
    nant = m0
    if dd == 0:
        nf = m0
    while f <= dd:
        nf = (1 + (j*q*(1 - (nant/m))))*nant
        nant = nf
        f = f + 1
    return int(nf)     
