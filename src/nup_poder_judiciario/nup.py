#  Classe que oferece funcionalidades para a Numeração Única de Processos
#  do Poder Judiciário instituída pelo Conselho Nacional de Justiça
#
#  Estrutura: NNNNNNN-DD.AAAA.J.TR.OOOO
#  Norma: ISO 7064
#
#  Resolução: Nº 65 de 16/12/2008
#  Disponível em: http://www.cnj.jus.br/atos-normativos?documento=119
#
#
# Projeto de referência em TypeScript:
#  https://github.com/edipojuan/numero-unico-processo/blob/master/src/numero-unico-processo.util.ts
#
from datetime import date

class NumeroUnicoProcesso:
    def __init__(self, numero):
        if type(numero) is str:
            numero = self.dicionariza(''.join(i for i in numero if i.isdigit()))
        if type(numero) is int:
            numero = self.dicionariza(str(numero))
        if type(numero) is list:
            numero = self.dicionariza(''.join(str(i) for i in numero))

        self.numero = numero['numero'].zfill(7)
        self.dv = numero['dv']
        self.ano = numero['ano']
        self.segmento = numero['segmento']
        self.tribunal = numero['tribunal']
        self.orgao = numero['orgao']

    def __str__(self):
        return self.formatado()

    def __int__(self):
        return int(self.soNumeros())

    def dicionariza(self, numero: str) -> dict:
        numero_dic = dict()
        numero_dic['numero'] = numero[:-13] # (NNNNNNN)
        numero_dic['dv'] = numero[-13:-11] # (DD)
        numero_dic['ano'] = numero[-11:-7] # (AAAA)
        numero_dic['segmento'] = numero[-7:-6] # (J)
        numero_dic['tribunal'] =  numero[-6:-4] # (TR)
        numero_dic['orgao'] = numero[-4:] # (OOOO)

        return numero_dic

    def calcularDigitoVerificador(self):
        valor = self.calcular()
        calculo = 98 - (valor % 97)
        digitoVerificador = f"{calculo}".zfill(2)

        return digitoVerificador

    def calcular(self):
        digitoVerificador = '00'
        valor = int(f"{self.numero}{self.ano}{self.segmento}{self.tribunal}{self.orgao}{digitoVerificador}")

        return valor

    def soNumeros(self):
        return f"{self.numero}{self.dv}{self.ano}{self.segmento}{self.tribunal}{self.orgao}"

    def formatado(self):
        return f"{self.numero}-{self.dv}.{self.ano}.{self.segmento}.{self.tribunal}.{self.orgao}"

    def validar(self):
        if not (len(self.numero) == 7):
            raise ValueError("Erro no número de dígitos do processo")
        if not (self.dv == self.calcularDigitoVerificador()):
            raise ValueError("Erro no digito verificador")
        if not (1895 <= int(self.ano) <= date.today().year):
            raise ValueError("Erro no Ano do processo")
        if not (1 <= int(self.segmento) <= 9):
            raise ValueError("Erro no número do segmento de justiça")
        if 1 <= int(self.segmento) <= 3:
            if not (int(self.tribunal) == 0):
                raise ValueError("Erro no número para processos do STF, STJ ou CNJ")
        elif int(self.segmento) == 4:
            if not (1 <= int(self.tribunal) <= 6) or self.tribunal == '90':
                raise ValueError("Erro no número do tribunal na justiça federal")
        elif int(self.segmento) == 5:
            if not (1 <= int(self.tribunal) <= 24) or self.tribunal == '00' or self.tribunal == '90':
                raise ValueError("Erro no número do tribunal na justiça do trabalho")
        elif int(self.segmento) == 6:
            if not (1 <= int(self.tribunal) <= 27) or self.tribunal == '00':
                raise ValueError("Erro no número do tribunal na justiça eleitoral")
        elif int(self.segmento) == 7:
            if not (1 <= int(self.tribunal) <= 12) or self.tribunal == '00':
                raise ValueError("Erro no número do tribunal na justiça militar da união")
        elif int(self.segmento) == 8:
            if not (1 <= int(self.tribunal) <= 27):
                raise ValueError("Erro no número do tribunal na justiça estadual ou do distrito federal e territórios")
        elif int(self.segmento) == 9:
            if not (self.tribunal in ['13', '21', '26']):
                raise ValueError("Erro no número do tribunal na justiça militar estadual")
        if not (1 <= int(self.orgao) <= 8999) or self.orgao == '0000':
            raise ValueError("Erro no número da unidade de origem do processo")

        return True
