from unittest import TestCase
from datetime import datetime
from utils import ConvertDate


class TestConvertDate(TestCase):
    def setUp(self):
        self.dates_brasil = ['02-12-2018', '01/12/2018 00:31:29', '01-10-2018 00:31:29', '02/12/2018', '02-12-2018']
        self.dates_invalid = ['catota no nariz', '00:01:01 2018/01/20', '31/02/2018', 1, dict(ola='oi'), '31\02/2018',
                              '&1!02#2018']
        self.date_american = ['01-31-2018 04:32:32']

    def test_convert_string_brazil_to_datetime(self):
        """Test convert datetime for string in format date brazil"""

        for d in self.dates_brasil:
            date = ConvertDate().convert_date_brasil_for_datetime(d)
            self.assertIsInstance(date, datetime, msg="A função não consegui converter para datetime")

    def test_convert_to_string_american_to_datetime(self):
        """Test convert datetime for string in format american"""
        for d in self.dates_brasil:
            date = ConvertDate().convert_date_american_for_datetime(d)
           self.assertIsInstance(date, datetime, msg="A função não consegui converter para datetime")

    def test_return_error(self):
        for d in self.dates_invalid:
            date = ConvertDate().convert_date_brasil_for_datetime(d)
            self.assertIsInstance(date, dict, msg="Esse teste deveria retornar um dicionário com um código de erro")
