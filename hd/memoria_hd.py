from constantes import TAMANHO_HD

# Simula o arquivo de paginação
class MemoriaHD:
    def __init__(self):
        # O HD contém todas as páginas possíveis
        self.paginas = list(range(TAMANHO_HD))

    def contem_pagina(self, pagina):
        return pagina in self.paginas
