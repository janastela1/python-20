
import unittest

import requests


def get_endereco(cep):
    return requests.get('https://viacep.com.br/ws/{}/json/'.format(cep)).json()

class TestGetEndereco(unittest.TestCase):

    def test_get_endereco(self):
        cep = '01523000'
        resposta = get_endereco(cep)
        self.assertEqual(
            resposta['logradouro'],
            'Rua Clímaco Barbosa'
        )

if __name__ == '__main__':
    unittest.main()