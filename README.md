# Numeração Única do Poder Judiciário - nup_poder_judiciario

Este package oferece funcionalidades relacionadas à numeração única de processos do Poder Judiciário, que segue a estrutura NNNNNNN-DD.AAAA.J.TR.OOOO, instituida pelo Conselho Nacional de Justiça.

 Resolução nº 65 de 16/12/2008
 Disponível em: <http://www.cnj.jus.br/atos-normativos?documento=119>

Projeto de referência em TypeScript:
 <https://github.com/edipojuan/numero-unico-processo/blob/master/src/numero-unico-processo.util.ts>

Uso:
``
from nup_poder_judiciario import NumeroUnicoProcesso

numero_processo = NumeroUnicoProcesso('1024981-09.2022.4.01.3600')
``

Atributos:
    'ano' - ano do processo
    'numero' - retorna só a parte NNNNNNN
    'orgao' - retorna só a parte OOOO
    'segmento' - retorna só a parte J
    'soNumeros' - retorna só os dígitos
    'tribunal' - retorna só a parte TR
    'dv' - dígito verificador do processo

Funcionalidades:
    'calcular' - calcular a fórmula inicial
    'calcularDigitoVerificador' - calcular dígito verificador
    'dicionariza' - transforma em dicionário
    'formatado' - retorna o número formatado
    'validar' - verificar se é um número de processo válido
