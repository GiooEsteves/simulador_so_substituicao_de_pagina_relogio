from ram.memoria_ram import MemoriaRAM
from hd.memoria_hd import MemoriaHD

class GerenciadorMemoriaVirtual:
    def __init__(self):
        self.ram = MemoriaRAM()
        self.hd = MemoriaHD()

    # o processo acessa um endereço da memoria  
    def acessar_endereco(self, thread_id, pagina, operacao):
        print(f"[Thread {thread_id}] Acessando pagina {pagina}")

        if self.ram.contem_pagina(pagina):
            # A página está na RAM
            print(f"[Thread {thread_id}] Pagina {pagina} está na RAM")
            self.ram.acessar_pagina(pagina, operacao)

        elif self.hd.contem_pagina(pagina):
            # Pagina não está na RAM, carrega do HD
            print(f"[Thread {thread_id}] Falta de Pagina: Carregando pagina {pagina} do HD")
            self.ram.adicionar_pagina(pagina, operacao)

        else: # Pagina não está nem na RAM em uso e nem no HD armazenada (Página inválida)
            print(f"[Thread {thread_id}] Erro: Pagina {pagina} não encontrada no HD.")
