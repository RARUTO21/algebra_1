class TipoA:
    def __init__(self, f1, f2):
            self.nombre = "Tipo A"
            self.filaA = f1+1
            self.filaB = f2+1


class TipoB:
    def __init__(self, f1, c1):
            self.nombre = "Tipo B"
            self.filaC = f1+1
            self.constanteA = c1


class TipoC:
    def __init__(self, f1, f2, c1):
            self.nombre = "Tipo C"
            self.filaD = f1+1
            self.filaE = f2+1
            self.constanteB = c1