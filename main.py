import threading  # biblioteca para simular múltiplos processos concorrentes 
import time
from memoria_virtual.GerenciadorMemoriaVirtual import GerenciadorMemoriaVirtual

def simular_processo(gerenciador, thread_id, acessos):
    for pagina in acessos:
        gerenciador.acessar_endereco(thread_id, pagina)
        time.sleep(0.5)  # Simula tempo de acesso/processamento

if __name__ == "__main__":
    gerenciador = GerenciadorMemoriaVirtual()

    # Acessos simulados por cada processo de endereços de paginas virtuais
    acessos_thread_1 = [0, 1, 2, 3, 0, 4, 5]
    acessos_thread_2 = [2, 3, 4, 6, 2, 7]

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
