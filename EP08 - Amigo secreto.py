# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS E ATRIBUTOS
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
#####################################################################
# MÓDULOS A SEREM UTILIZADOS NO PROGRAMA
# random.shuffle(lst) embaralha os elementos da lista lst.
import random 

#####################################################################
def main():
    '''
    Essa função auxilia no teste das funções pedidas para o EP08.
    Se desejar, escreva mais testes.
    
    Atenção: a tabulação das linhas foi removida e deve ser consertada 
    antes que a função possa ser utilizada.
    '''
    print("Testes do EP08")
    
    # testes da função circular()
    print("Função circular()")
    amigos1 = [1,2,3,4,0]
    amigos2 = [1,2,0,4,3]
    print("circular(%s) = %s"%(amigos1, circular(amigos1)))
    print("circular(%s) = %s"%(amigos2, circular(amigos2)))
    
    # testes da função experimento()
    print("Função experimento()")
    semente = int(input("Digite o valor da semente do gerador de números pseudo-aleatórios: "))
    random.seed(semente)
    MINN  = int(input("Qual o número mínimo de pessoas: "))
    MAXN  = int(input("Qual o número máximo de pessoas: "))
    passo = int(input("Qual o passo: "))
    T     = int(input("Qual o número de tentativas em cada experimento: "))
    SHOW  = input("Você quer ver as listas que são circulares [s/n]: ")
    
    debug = False
    if SHOW == 'S' or SHOW == 's':
        debug = True
    
    n = MINN
    while n <= MAXN:
        pn = experimento(n, T, debug)
        print("p(%d) = %f"%(n, pn))
        n = n + passo

###################################################################
def sorteie_lista( n ):
    ''' (int) -> list
    Retorna uma lista de tamanho n, contendo os números 
    de 0 a n em ordem aleatória.
    
    Atenção: a tabulação das linhas foi removida e a ordem de algumas 
    linhas alterada. Ela deve ser consertada antes possa ser utilizada.
    '''
    lista = []
    i = 0
    while i < n:
        lista += [i]
        i += 1
    random.shuffle(lista)
    
    return lista
######################################################################
def circular(amigo_de):
    ''' (list) -> bool 
    Recebe uma lista de "amigo secreto" e retorna True caso exista 
    um único ciclo na lista (a lista seja circular).
    Retorna False caso contrário.
    '''
    n = len(amigo_de)
        
    j = 0
    prim = t = amigo_de[j]
    circular = False
    i = 1
    while t != j and i <= n:
        j = t
        t = amigo_de[j]
        if j == t and i < n-1:
            circular = False
        if i < n-1 and t == 0:
            circular = False  
        if i == n and t == prim:
            circular = True
        i += 1
   
    # modifique o código abaixo para conter a sua solução.
   
    return circular
        

###################################################################
def experimento(N, T, debug=False):
    ''' (int, int) -> float, list
    Calcula a probabilidade de uma lista de "amigo secreto" com N 
    participantes ter apenas 1 ciclo. Essa probabilidade deve
    ser calculada a partir de T sorteios de listas de tamanho N, 
    e calculando a frequência relativa das listas com apenas 1 ciclo
    (listas circulares).
    '''
    s = 0
    i = 1
    while i <= T:
        lista = sorteie_lista(N)
        if circular(lista):
            s += 1
            print(lista, s)
        i += 1
    prob = s/T
    # modifique o código abaixo para conter a sua solução.
    
    return prob
#=====================================================================
# Não modifique as linhas abaixo
# Esse if serve para executar a main() dentro do Spyder
# e não atrapalhar o avaliador
if __name__ == '__main__':
    main()
