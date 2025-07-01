from constantes import TAMANHO_HD

# Simula o arquivo de paginação
class MemoriaHD:
    def __init__(self):
        self.paginas = list(range(TAMANHO_HD)) # Cria uma lista com as páginas virtuais disponíveis no HD

    # Verifica se a página existe no HD
    def contem_pagina(self, pagina):
        return pagina in self.paginas
