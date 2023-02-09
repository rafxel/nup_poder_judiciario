# nup_poder_judiciario

Este package oferece funcionalidades relacionadas à numeração única de processos do Poder Judiciário, que segue a estrutura NNNNNNN-DD.AAAA.J.TR.OOOO, instituida pelo Conselho Nacional de Justiça.

 Resolução: Nº 65 de 16/12/2008
 Disponível em: http://www.cnj.jus.br/atos-normativos?documento=119


Projeto de referência em TypeScript:
 https://github.com/edipojuan/numero-unico-processo/blob/master/src/numero-unico-processo.util.ts

Testes:

python -m unittest .\tests\test_nup.py

Uso:

from src.nup_poder_judiciario.nup import NumeroUnicoProcesso

numero_processo = NumeroUnicoProcesso('1024981-09.2022.4.01.3600')