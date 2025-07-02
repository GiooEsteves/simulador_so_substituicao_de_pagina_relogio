from ram.memoria_ram import MemoriaRAM
from hd.memoria_hd import MemoriaHD
from constantes import TAMANHO_VIRTUAL

class GerenciadorMemoriaVirtual:
    def __init__(self):
        self.ram = MemoriaRAM()
        self.hd = MemoriaHD()
        self.ram.hd = self.hd  # permite que a RAM acesse o HD

    # o processo acessa um endereço da memoria  
    def acessar_endereco(self, thread_id, pagina, operacao):
        # Verifica se a pagina é comportada na memoria virtual
        if pagina < 0 or pagina >= TAMANHO_VIRTUAL:
            print(f"[Thread {thread_id}] Erro Fatal: Página {pagina} é maior que o tamanho de momoria virtual permitida")
            return

        print(f"[Thread {thread_id}] Acessando pagina {pagina}")
        
        if self.ram.contem_pagina(pagina):
            # A página está na RAM
            print(f"[Thread {thread_id}] Pagina {pagina} já está na RAM")
            self.ram.acessar_pagina(pagina, operacao)

        elif self.hd.contem_pagina(pagina):
            # Pagina não está na RAM, carrega do HD
            print(f"[Thread {thread_id}] Falta de Pagina: Carregando pagina {pagina} do HD")
            pagina_virtual = self.hd.obter_pagina(pagina)  # pega o objeto PaginaVirtual do HD
            self.ram.adicionar_pagina(pagina_virtual, operacao)  # envia a pagina para a RAM

        else: # Pagina não está nem na RAM em uso e nem no HD armazenada (Página inválida)
            print(f"[Thread {thread_id}] Erro: Pagina {pagina} não encontrada no HD.")
