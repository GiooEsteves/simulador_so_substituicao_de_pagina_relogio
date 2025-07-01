from constantes import TAMANHO_RAM
from ram.quadro import Quadro

class MemoriaRAM:
    def __init__(self):
        # Cria uma lista de quadros vazios
        self.quadros = [Quadro() for _ in range(TAMANHO_RAM)] # Uma lista com 4 quadros
        self.ponteiro_relogio = 0 # Inicializa o ponteiro do relogio em 0

    # Verifica se tem pagina no RAM
    def contem_pagina(self, pagina): 
        return any(q.ocupado and q.pagina == pagina for q in self.quadros) # Retorna True se algum quadro está ocupado e contém a página
    
    # Acessa uma pagina e altera o seu bit de referência para o de acessado
    def acessar_pagina(self, pagina, operacao):
        for quadro in self.quadros:
            if quadro.pagina == pagina:
                quadro.referencia = 1  # Página acessada → bit R = 1
                if operacao in ['W', 'w']:
                    quadro.modificado = True
                    print(f"         Página {pagina} é marcada como W (escrita)")
                else:
                    print(f"         Pagina {pagina} é marcada como R (leitura)")
                return

    # Adiciona uma pagina
    def adicionar_pagina(self, pagina, operacao):
        while True:
            quadro = self.quadros[self.ponteiro_relogio] # Pega o quadro que está sendo apontado pelo ponteiro

            if not quadro.ocupado:
                # Encontra quadro vazio e insere página
                quadro.pagina = pagina
                quadro.referencia = 1
                quadro.ocupado = True
                quadro.modificado = (operacao in ['W', 'w'])
                if quadro.modificado:
                    print(f"         Página {pagina} inserida como W (escrita)")
                else:
                    print(f"         Pagina {pagina} inserida como R (leitura)")
                break
            elif quadro.referencia == 0: # Substitui página se bit R = 0
                quadro.pagina = pagina
                quadro.referencia = 1
                quadro.modificado = (operacao in ['W', 'w'])
                if quadro.modificado:
                    print(f"         Página {pagina} inserida como W (escrita)")
                else:
                    print(f"         Pagina {pagina} inserida como R (leitura)")
                break
            else:  # Bit R = 1 → zera e avança ponteiro
                quadro.referencia = 0
                self.ponteiro_relogio = (self.ponteiro_relogio + 1) % TAMANHO_RAM   # Ponteiro vai para o próximo quadro se fim da ram volta ao inicio
