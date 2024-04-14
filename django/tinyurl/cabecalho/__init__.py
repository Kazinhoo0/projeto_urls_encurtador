def linhas( linhas = 45):
    return ("=" * linhas)



def cabecalho(txt):
    print(linhas())
    print(txt.center(45))
    print(linhas())
    
    
    
def opcoes():
 
    print("""Programa encurtador de Urls, abaixo você terá algumas opcoes basta escolher.\n
          1 - Adicionar nova url
          2 - Ver urls encurtadas adicionadas
          3 - Ver urls não encurtadas adicionadas
          4 - SAIR
          5 - Criar tabela
          """)