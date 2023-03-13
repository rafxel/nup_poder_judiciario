import unittest

from src.nup_poder_judiciario.nup import NumeroUnicoProcesso


class TestBasico(unittest.TestCase):
    def test_carrega_string(self):
        """
        Testa se consegue carregar digitos em forma de string
        """
        data = '1024981-09.2022.4.01.3600'
        result = NumeroUnicoProcesso(data)
        self.assertIsInstance(result, NumeroUnicoProcesso)

    def test_carrega_inteiro(self):
        """
        Testa se consegue carregar digitos em forma de número inteiro
        """
        data = 10249810920224013600
        result = NumeroUnicoProcesso(data)
        self.assertIsInstance(result, NumeroUnicoProcesso)

    def test_carrega_list(self):
        """
        Testa se consegue carregar digitos em forma de lista
        """
        data = [1, 0, 2, 4, 9, 8, 1, 0, 9, 2, 0, 2, 2, 4, 0, 1, 3, 6, 0, 0]
        result = NumeroUnicoProcesso(data)
        self.assertIsInstance(result, NumeroUnicoProcesso)

class TestChaves(unittest.TestCase):
    def test_chave_numero(self):
        """
        Testa se as chaves número está na classe
        """
        data = ''
        result = NumeroUnicoProcesso(data)
        self.assertEqual(result.numero, '0000000')

    def test_chave_dv(self):
        """
        Testa se a chave DV está na classe
        """
        data = ''
        result = NumeroUnicoProcesso(data)
        self.assertEqual(result.dv, '')

    def test_chave_ano(self):
        """
        Testa se a chave ANO está na classe
        """
        data = ''
        result = NumeroUnicoProcesso(data)
        self.assertEqual(result.ano, '')

    def test_chave_segmento(self):
        """
        Testa se a chave SEGMENTO está na classe
        """
        data = ''
        result = NumeroUnicoProcesso(data)
        self.assertEqual(result.segmento, '')

    def test_chave_tribunal(self):
        """
        Testa se a chave TRIBUNAL está na classe
        """
        data = ''
        result = NumeroUnicoProcesso(data)
        self.assertEqual(result.tribunal, '')

    def test_chave_orgao(self):
        """
        Testa se a chave ORGAO está na classe
        """
        data = ''
        result = NumeroUnicoProcesso(data)
        self.assertEqual(result.orgao, '')

class TestDicionariza(unittest.TestCase):
    def test_dicionariza_numero(self):
        """
        Testa se a chave número está com o valor correto
        """
        data = '1024981-09.2022.4.01.3600'
        result = NumeroUnicoProcesso(data)
        self.assertEqual(result.numero, '1024981')

    def test_dicionariza_dv(self):
        """
        Testa se a chave DV está com o valor correto
        """
        data = '1024981-09.2022.4.01.3600'
        result = NumeroUnicoProcesso(data)
        self.assertEqual(result.dv, '09')

    def test_dicionariza_ano(self):
        """
        Testa se a chave ANO está com o valor correto
        """
        data = '1024981-09.2022.4.01.3600'
        result = NumeroUnicoProcesso(data)
        self.assertEqual(result.ano, '2022')

    def test_dicionariza_segmento(self):
        """
        Testa se a chave SEGMENTO está com o valor correto
        """
        data = '1024981-09.2022.4.01.3600'
        result = NumeroUnicoProcesso(data)
        self.assertEqual(result.segmento, '4')

    def test_dicionariza_tribunal(self):
        """
        Testa se a chave TRIBUNAL está com o valor correto
        """
        data = '1024981-09.2022.4.01.3600'
        result = NumeroUnicoProcesso(data)
        self.assertEqual(result.tribunal, '01')

    def test_dicionariza_orgao(self):
        """
        Testa se a chave ORGAO está com o valor correto
        """
        data = '1024981-09.2022.4.01.3600'
        result = NumeroUnicoProcesso(data)
        self.assertEqual(result.orgao, '3600')

class TestDunder(unittest.TestCase):
    def test_dunder_string(self):
        """
        Testa se a chave número está com o valor correto
        """
        data = '1024981-09.2022.4.01.3600'
        result = NumeroUnicoProcesso(data)
        self.assertEqual(str(result), data)

    def test_dunder_integer(self):
        """
        Testa se a chave número está com o valor correto
        """
        data = '1024981-09.2022.4.01.3600'
        result = NumeroUnicoProcesso(data)
        self.assertEqual(int(result), 10249810920224013600)


if __name__ == '__main__':
    unittest.main()