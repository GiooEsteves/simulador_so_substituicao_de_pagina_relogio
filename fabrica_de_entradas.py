import random
from constantes import QTD_ACESSO_ENTRADA

class FabricaDeEntradas:
    def __init__(self, tamanho_memoria):
        # Validações dos limites da memória virtual
        if tamanho_memoria < 10:
            raise ValueError("Memória muito pequena - valor mínimo 10")
        if tamanho_memoria > 40:
            raise ValueError("Memória grande - valor máximo 40")
        if QTD_ACESSO_ENTRADA < 50:
            raise ValueError("Tamanho da entrada não pode ser menor que 50")

        self.tamanho_memoria_virtual = tamanho_memoria

        # Gera uma semente aleatória para repetir a mesma sequência toda vez
        self.seed = random.randint(0, tamanho_memoria)
        print("Semente =", self.seed)

    def get_nova_entrada(self):
        # Usa a semente gerada para repetir os mesmos acessos
        random.seed(self.seed)
        r = random.Random(self.seed)  # Para gerar endereços e controlar tipo de acesso (R ou W)
        r1 = random.Random()          # Para gerar valores aleatórios de escrita (0 a 99)

        reads = []              # Lista de endereços que já foram lidos/escritos
        loop = [""] * 4         # Buffer com últimos 4 acessos para repetir (simula localidade temporal)
        index_loop = 0          # Índice de controle do loop circular
        entrada = []            # Lista com as entradas geradas (formato: "10-R", "5-W-32", ...)

        # Pontos onde os acessos do loop serão repetidos
        loop1 = QTD_ACESSO_ENTRADA // 3
        loop2 = QTD_ACESSO_ENTRADA // 3 * 2

        i = 0
        while i < QTD_ACESSO_ENTRADA:
            # Quando chegar nas posições loop1 ou loop2, repete os últimos 4 acessos
            if i == loop1 or i == loop2:
                for j in range(len(loop)):
                    entrada.append(loop[index_loop])
                    index_loop = (index_loop + 1) % len(loop)
                i += len(loop)  # Pula os acessos já adicionados
                continue

            # Gera endereço de memória virtual aleatório
            endereco = r.randint(0, self.tamanho_memoria_virtual - 1)

            if endereco not in reads:
                # Primeira vez que esse endereço é acessado → leitura
                acesso = f"{endereco}-R"
                reads.append(endereco)
            else:
                # Endereço já foi acessado antes → pode ser leitura ou escrita
                if r.random() < 0.5:
                    acesso = f"{endereco}-R"
                else:
                    valor = r1.randint(0, 99)  # Valor simulado para escrita
                    acesso = f"{endereco}-W-{valor}"

            # Adiciona o acesso à lista de saída
            entrada.append(acesso)

            # Atualiza o buffer de repetição (circular)
            loop[index_loop] = acesso
            index_loop = (index_loop + 1) % len(loop)

            i += 1

        # Retorna a string final com os acessos separados por vírgula
        return ",".join(entrada)
