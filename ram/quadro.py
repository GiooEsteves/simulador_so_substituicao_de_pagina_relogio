# Define um quadro de memória RAM
class Quadro:
    def __init__(self):
        self.pagina = None           # Página armazenada nesse quadro
        self.referencia = 0          # Bit de referência usado pelo algoritmo do relógio
        self.ocupado = False         # Indica se o quadro está sendo usado
        self.modificado = False      # Indica se a página foi escrita
