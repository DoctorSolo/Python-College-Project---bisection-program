class Bisection:
    def __init__(self, a: float, b: float, func) -> None:
        self.a = a
        self.b = b
        
        self.f = func                       # f recebe a função do contrutor
        self.c = lambda a, b: (a + b)/2     # c é uma função do calculo do ponto medio
        
        # esta variavel verifica se a raiz existe 
        # dentro do intervalo [a,b] e retorna True ou False
        self.existe_raiz = lambda a, b: (self.f(a) * self.f(b)) < 0
        
        # este dicionario da classe ira armazenar todos os intervalos
        self.intervalos = {}
        
        # Esta variavel adquire a raiz da bisseção
        self.resposta = self.bisection(self.a, self.b)
    
    
    
    # Este metodo é o que ira aplicar a bisseção
    def bisection(self, a, b):
        # Verifica se a raiz esite
        if self.existe_raiz(a, b):
            c = self.c(a, b) # Esta variavel apenas recebe o valor de (a+b)/2
            
            # Defino um limite para o loop para não gastar recurso da minha maquina
            for i in range(50):
                
                # se a raiz existir no intervalo [a, b] b recebe c,
                # em outras palavras [a, c]
                if self.existe_raiz(a, b): 
                    b = c
                
                # se a raiz não existir no intervalo [a, b] a recebe c,
                # em outras palavras [c, b]
                else:
                    a = c
                
                # c_novo recebe o valor do novo intervalo primeiro 
                # para fazer o calculo da precisão
                c_novo = self.c(a, b)
                
                # Esta variavel adiquire o percentual de precisão
                E = 100*abs((c_novo - c)/c_novo)
                
                # Este dicionario ira armazenar o intervalo [a,b]
                # e o valor do ponto medio
                self.intervalos[i] = {'a': a,
                                      'b': b,
                                      'Ponto Medio': c_novo,
                                      'Precisao': f"{E:.2f}%"
                                      }
                # Essa condição faz o calculo da precisão, 
                # caso for verdadeira ela retorna o valor do c_novo
                if E < 1:
                    print(f"A raiz aproximada é {c_novo}")
                    return c_novo
                
                # Caso não, então o velho c recebe c_novo e segue o loop
                c = c_novo
        
        # Se a raiz não existir então o metodo ira retornar none
        print(f'Não existe raiz em {a, b}')
        return None
    
    
    # Este metodo calcula o percentual
    def percentual(self, a, b):
        EA = abs(b - a)
        ER = EA/b
        return ER*100