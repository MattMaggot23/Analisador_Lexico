def analisador(expressao):
    simbolos = []
    
    definicoes = [
        ('0123456789', 'Número'),
        ('(', 'Parêntese Aberto'),
        (')', 'Parentêse Fechado'),
        ('{', 'Chave Aberta'),
        ('}', 'Chave Fechada'),
        ('+', 'Adição'),
        ('-', 'Subtração'),
        ('*', 'Multiplicação'),
        ('/', 'Divisão'),
        ('^', 'Exponenciação'),
        ('[', 'Colchete aberto'),
        (']', 'Colchete fechado'),
    ]
    
    for caractere in expressao:
        simbolo_tipo = None
        for padrao, tipo in definicoes:
            if caractere in padrao:
                simbolo_tipo = tipo
                break
        
        if simbolo_tipo:
            simbolos.append((caractere, simbolo_tipo))
    
    return simbolos

def main():
    expressao = input("Digite a expressão: ")
    simbolos = analisador(expressao)
    
    print("caractere\t\t\ttipo")
    print("---------------------")
    for simbolo in simbolos:
        print(f"{simbolo[0]}\t\t\t{simbolo[1]}")

if __name__ == "__main__":
    main()
