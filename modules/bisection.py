class Bisection:
    def __init__(self, a: float, b: float, X) -> None:
        self.a = a
        self.b = b
        self.f = lambda x: X
        self.c = lambda a, b: (a + b)/2
        self.existe_raiz = lambda a, b: (self.f(a) * self.f(b)) < 0
    
    
    def bisection(self, a, b, tolerancia=1e-5):
        
        if self.existe_raiz(a, b):
            c = self.c(a, b)
            while abs(self.f(c)) > tolerancia:
                c = self.c(a, b)
                
                if self.existe_raiz(a, b): 
                    b = c
                else: 
                    a = c
            print(f"A raiz aproximada é {c}")
            return c
        
        print(f'Não existe raiz em {a, b}')
        return None