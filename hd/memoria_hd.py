from constantes import TAMANHO_HD
from memoria_virtual.pagina_virtual import PaginaVirtual

# Simula o arquivo de paginação
class MemoriaHD:
    def __init__(self):
        # Armazena objetos PaginaVirtual
        self.paginas = {i: PaginaVirtual(i) for i in range(TAMANHO_HD)} # Cria uma lista com as páginas virtuais disponíveis no HD

    # Verifica se a página existe no HD
    def contem_pagina(self, numero):
        return numero in self.paginas

    # Pega o indice da pagina
    def obter_pagina(self, numero):
        return self.paginas.get(numero)
