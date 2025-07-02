# Define um quadro de memória RAM
class Quadro:
    def __init__(self):
        self.pagina = None           # Página virtual armazenada nesse quadro
        self.referencia = 0          # Bit de referência usado pelo algoritmo do relógio
        