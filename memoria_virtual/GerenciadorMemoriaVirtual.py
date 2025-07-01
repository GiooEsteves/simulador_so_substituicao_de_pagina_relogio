from ram.memoria_ram import MemoriaRAM
from hd.memoria_hd import MemoriaHD

class GerenciadorMemoriaVirtual:
    def __init__(self):
        self.ram = MemoriaRAM()
        self.hd = MemoriaHD()

    def acessar_endereco(self, thread_id, pagina):
        print(f"[Thread {thread_id}] Acessando pagina {pagina}")

        if self.ram.contem_pagina(pagina):
            # A página está na RAM, basta usar
            print(f"[Thread {thread_id}] Pagina {pagina} já está na RAM (sem falta)")
            self.ram.acessar_pagina(pagina)

        elif self.hd.contem_pagina(pagina):
            # Falta de página: carrega do HD
            print(f"[Thread {thread_id}] Falta de Pagina: Carregando pagina {pagina} do HD")
            self.ram.adicionar_pagina(pagina)

        else:
            # Página inválida
            print(f"[Thread {thread_id}] Erro: Pagina {pagina} não encontrada no HD.")
