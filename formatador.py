
# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS OU ATRIBUTOS
# NÃO APAGUE OS DOCSTRINGS 
#------------------------------------------------------------------
     
'''
    Nome: Yrlla Mariana V. de França
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

# CONSTANTES
ESPACO = ' '
BRANCO = ' \n\t\v\r\f'

#------------------------------------------------------------------
def main():
    '''
        Modifique essa função, escrevendo outros testes.
    '''
    # 1. leia o limite de caracteres por linha    
    k = int(input("Digite o no. de colunas por linha (> 0): "))
    
    # 2. leia o texto de um arquivo
    # 2.1 leia o nome do arquivo
    nome = input("Digite o nome do arquivo: ")
    # 2.2 "abra" o arquivo
    arquivo = open(nome, 'r', encoding='utf-8')
    # 2.3 leia o conteudo do arquivo e chame de txt 
    txt = arquivo.read()
    # 2.4 feche o arquivo
    arquivo.close()
    
    # 3. faça uma reguinha
    # reguinha = s[:k]
    reguinha = " " + ((k//5 + 1) * '....*')[:k] # reguinha
    
    # 4. exiba o texto original    
    print("Texto original: ")
    print(reguinha)
    print(txt + '\n') # '\n' para mudar de linha
    
    # 5. ajuste o limite da coluna
    # de txt para uma lista de strings k-ajustadas à esquerda
    print(f"Texto com linhas {k}-ajustadas à esquerda: ")
    lst_str_esq = ajuste_esquerda(txt, k)
    print(reguinha)
    for linha in lst_str_esq:
        print('|'+linha+'|')
        print()
    
    # 6. ajuste o limite da coluna
    # de lista de strings k-ajustadas à esquerda para k-ajustadas completas
    print(f"Texto linhas {k}-ajustadas completamente: ")    
    lst_str_comp = ajuste_completo(lst_str_esq, k)
    print(reguinha)
    for linha in lst_str_comp:
        print("|"+linha+"|")
            
#--------------------------------------------------------
def ajuste_esquerda(txt, k):
    '''(str, int) -> list de str

    RECEBE  uma string `txt` e um inteiro `k`.
    RETORNA A lista de strings k-ajustadas à esquerda que representa `txt`.
   '''
    p_txt = txt.split()
    lst = []
    lst2 = p_txt + ['']
    v = ''
    i = 0
    s =''
    j = 1
    
    
    while i < len(p_txt) and j < len(lst2):
      
        s += p_txt[i] + ' '
        len(p_txt[i])
        print(lst, s, i, j)
        if len(s.strip()) >= k and s != v:
            lst += [s.strip()]
            s = ''
        if len(s) >= k and s != v:
            lst += [s.strip()]
            s = ''

        if len(s) < k and len(lst2[j]) + len(s) > k and s != v:
            lst += [s.strip()]
            s = ''
        if len(s) < k and i == len(p_txt)-1 and s != v:
            lst += [s.strip()]
            s = ''
        i += 1
        j += 1
            
            
      
        
    return lst
                                

  
 
    

#--------------------------------------------------------
def ajuste_completo(lst_str, k):
    '''(list de str, int) -> list de str

    RECEBE  uma lista de strings `lst_str` e um inteiro `k` tais que cada string na 
       lista é `k`-ajustada à esquerda.
    CRIA e RETORNA A lista com as strings em `lst_str` k-ajustadas completamente.
    '''
    
    
    
#######################################################
###                 FIM                             ###
#######################################################
# 
# Esse if serve para rodar a main() dentro do Spyder.
if __name__ == '__main__':
    main()


