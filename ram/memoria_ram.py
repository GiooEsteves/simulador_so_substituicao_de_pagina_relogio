from constantes import TAMANHO_RAM
from ram.quadro import Quadro

class MemoriaRAM:
    def __init__(self):
        # Cria uma lista de quadros vazios
        self.quadros = [Quadro() for _ in range(TAMANHO_RAM)] # Uma lista com 4 quadros
        self.ponteiro_relogio = 0

    # Verifica se uma pagina já ta no RAM
    def contem_pagina(self, pagina): 
        return any(q.ocupado and q.pagina == pagina for q in self.quadros)
    
    # Acessa uma pagina e altera o seu bit de referência para o de acessado (1)
    def acessar_pagina(self, pagina):
        for quadro in self.quadros:
            if quadro.pagina == pagina:
                quadro.referencia = 1  # Página acessada → bit R = 1
                return

    # Adiciona uma pagina
    def adicionar_pagina(self, pagina):
        while True:
            quadro = self.quadros[self.ponteiro_relogio]

            if not quadro.ocupado:
                # Encontra quadro vazio e insere página
                quadro.pagina = pagina
                quadro.referencia = 1
                quadro.ocupado = True
                break
            elif quadro.referencia == 0: # Substitui página se bit R == 0
                quadro.pagina = pagina
                quadro.referencia = 1
                break
            else:  # Bit R == 1 → zera e avança ponteiro
                quadro.referencia = 0
                self.ponteiro_relogio = (self.ponteiro_relogio + 1) % TAMANHO_RAM   # ponteiro vai para o próximo quadro se fim da ram volta ao inicio
