import threading  # biblioteca para simular múltiplos processos concorrentes 
import time
from memoria_virtual.gerenciador_memoria_virtual import GerenciadorMemoriaVirtual

def simular_processo(gerenciador, thread_id, acessos):
    for pagina, operacao in acessos:
        gerenciador.acessar_endereco(thread_id, pagina, operacao)
        time.sleep(0.5)  # Simula tempo de processamento

if __name__ == "__main__":
    gerenciador = GerenciadorMemoriaVirtual()

    # Acessos simulados por cada processo de endereços de paginas virtuais
    acessos_thread_1 = [(0, "R"), (1, "W"), (2, "R"), (3, "W")]
    acessos_thread_2 = [(2, "R"), (4, "W"), (6, "R"), (6, "W")]

    # Threads simultâneas acessando memória
    thread1 = threading.Thread(target=simular_processo, args=(gerenciador, 1, acessos_thread_1))
    thread2 = threading.Thread(target=simular_processo, args=(gerenciador, 2, acessos_thread_2))

    # Inicia
    thread1.start() 
    thread2.start()

    # Aguarda o fim da execução para não ocorrer fluxo desordenado e sujeito a erros
    thread1.join()
    thread2.join()

    print("\nFIM.")
