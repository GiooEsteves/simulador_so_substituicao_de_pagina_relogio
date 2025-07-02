import threading
import time
from memoria_virtual.gerenciador_memoria_virtual import GerenciadorMemoriaVirtual
from fabrica_de_entradas import FabricaDeEntradas

def simular_processo(gerenciador, thread_id, acessos):
    for pagina, operacao in acessos:
        gerenciador.acessar_endereco(thread_id, pagina, operacao)
        time.sleep(0.1)

# transforma string da fábrica em lista de tuplas
def parse_acessos(entrada_str):
    acessos = []
    for item in entrada_str.split(','):
        partes = item.split('-')
        endereco = int(partes[0])
        operacao = partes[1]
        acessos.append((endereco, operacao))
    return acessos

if __name__ == "__main__":
    gerenciador = GerenciadorMemoriaVirtual()

    # Gera entrada automatizada com memória virtual de 10 páginas
    gerador = FabricaDeEntradas(tamanho_memoria=10)
    entrada = gerador.get_nova_entrada()
    acessos = parse_acessos(entrada)

    # Divide os acessos entre duas threads
    metade = len(acessos) // 2
    acessos_thread_1 = acessos[:metade]
    acessos_thread_2 = acessos[metade:]

    thread1 = threading.Thread(target=simular_processo, args=(gerenciador, 1, acessos_thread_1))
    thread2 = threading.Thread(target=simular_processo, args=(gerenciador, 2, acessos_thread_2))

    # inicia
    thread1.start()
    thread2.start()

    # sincroniza
    thread1.join()
    thread2.join()

    print("\nFIM")
