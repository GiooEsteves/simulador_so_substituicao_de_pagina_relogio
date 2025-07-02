class PaginaVirtual:
    def __init__(self, numero):
        self.numero = numero             # Identificador da página
        self.presente = 0                # Bit P: 1 = está na RAM, 0 = está apenas no HD
        self.modificado = 0              # Bit M: se foi escrita
        self.operacao = None             # Última operação realizada (R ou W)

    def set_presente(self, valor: bool):
        self.presente = int(valor)   # Atualiza o bit presente P

    def set_modificado(self, valor: bool):
        self.modificado = int(valor) # Atualiza o bit modificado M

    def set_operacao(self, op: str):
        self.operacao = op.upper()   # Atualiza a última operação (R ou W)
