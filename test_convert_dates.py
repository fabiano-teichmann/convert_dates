from unittest import TestCase
from datetime import datetime
from convert_dates import ConvertDate


class TestConvertDate(TestCase):
    def setUp(self):
        self.dates_brasil = ['02-12-2018', '01/12/2018 00:31:29', '01-10-2018 00:31:29', '02/12/2018', '02-12-2018']
        self.dates_invalid = ['catota no nariz', '00:01:01 2018/01/20', '31/02/2018', 1, dict(ola='oi'), '31\02/2018',
                              '&1!02#2018']
        self.date_american = ['2018-12-31 04:32:32', '2018/12/31 04:32:32']

    def test_convert_string_brazil_to_datetime(self):
        """Test convert datetime for string in format date brazil"""

        for d in self.dates_brasil:
            date = ConvertDate().convert_date_brasil_to_datetime(d)
            self.assertIsInstance(date, datetime, msg="A função não consegui converter para datetime")
            date_brasil = ConvertDate().convert_datetime_to_date_brazil(date)
            """Aqui faço a troca do - pelo / pois o usuário pode digitar com o -  e removo a hora minutos e segundo
            """
            self.assertEqual(date_brasil,  d[0:10].replace('-', '/'),
                             msg="Opa o output deve ser igual ao input")

    def test_convert_to_string_american_to_datetime(self):
        """Test convert datetime for string in format american '%Y-%m-%d %H:%M:%S'"""
        for d in self.date_american:
            date = ConvertDate().convert_date_american_to_datetime(d)
            self.assertIsInstance(date, datetime, msg="A função não consegui converter para datetime")

    def test_return_error(self):
        for d in self.dates_invalid:
            date = ConvertDate().convert_date_brasil_to_datetime(d)
            self.assertIsInstance(date, dict, msg="Esse teste deveria retornar um dicionário com um código de erro")
