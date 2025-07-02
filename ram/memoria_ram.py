from constantes import TAMANHO_RAM
from ram.quadro import Quadro

class MemoriaRAM:
    def __init__(self):
        # Cria uma lista de quadros vazios
        self.quadros = [Quadro() for _ in range(TAMANHO_RAM)] # Uma lista com 4 quadros
        self.ponteiro_relogio = 0 # Inicializa o ponteiro do relogio em 0

    # Verifica se tem pagina no RAM
    def contem_pagina(self, pagina_num): 
        return any(q.pagina and q.pagina.numero == pagina_num for q in self.quadros)

    # Acessa uma pagina e altera o seu bit de referência para o de acessado
    def acessar_pagina(self, pagina_num, operacao):
        for i, quadro in enumerate (self.quadros):
            if quadro.pagina and quadro.pagina.numero == pagina_num:
                quadro.referencia = 1  # Página acessada → bit R = 1
                quadro.pagina.set_operacao(operacao) # seta a operação que está sendo passada na pagina virtual
                if operacao == 'W':
                    quadro.pagina.set_modificado(True)
            
                print(f"           Página {pagina_num} | Presente: {quadro.pagina.presente} | R: {quadro.referencia} " 
                        f"| M: {int(quadro.pagina.modificado)} | Op: {quadro.pagina.operacao} | Quadro: {i}")
                return

    # Adiciona uma pagina
    def adicionar_pagina(self, pagina_virtual, operacao):
        while True:
            quadro = self.quadros[self.ponteiro_relogio] # Pega o quadro que está sendo apontado pelo ponteiro

            if quadro.referencia == 0: # Substitui página se bit R = 0
                if quadro.pagina:
                    quadro.pagina.set_presente(False)

                quadro.pagina = pagina_virtual
                quadro.referencia = 1
                pagina_virtual.set_presente(True) # Altera o bit P para 1
                pagina_virtual.set_operacao(operacao) # Adiciona a operação na pagina virtual R ou W

                if operacao == 'W':
                    pagina_virtual.set_modificado(True)

                print(f"           Página {pagina_virtual.numero} | Presente: {pagina_virtual.presente} | R: {quadro.referencia} " 
                      f"| M: {int(pagina_virtual.modificado)} | Op: {pagina_virtual.operacao} | Quadro: {self.ponteiro_relogio}")
                break
            else:  # Bit R = 1 → zera e avança ponteiro
                quadro.referencia = 0
                self.ponteiro_relogio = (self.ponteiro_relogio + 1) % TAMANHO_RAM   # Ponteiro vai para o próximo quadro se fim da ram volta ao inicio
