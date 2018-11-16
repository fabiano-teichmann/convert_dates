# Teste unitários para validação e conversão de datas
Esse projeto visa de maneira prática como implementar testes unitários para isso utilizei a bibioteca padrão do python o unittest. Essa demanda veio de um projeto onde eu trabalharia com a integração de dados de diversas fontes e de diversos formatos como americano com minutos e segundos, o formato brasileiro somente com data. Para garantir a integridade e interoperabilidade entre os sistema era necessário que a minha implementação converte-se datas de um formato especifico para datetime e de datetime para outro padrão. E com a filosofia Test Fist comecei meu trabalho importando as bibiliotecas necessárias.

    from unittest import TestCase
    from datetime import datetime
    from utils import ConvertDate

Depois comecei escrevendo minha classse e configunrando o Setup

    class TestConvertDate(TestCase):
        def setUp(self):
        self.dates = ['02-12-2018', '01/12/2018 00:31:29', 01-10-2018 00:31:29', '02/12/2018', '02-12-2018']
        self.dates_invalid = ['catota no nariz', '00:01:01 2018/01/20', '31/02/2018', 1, dict(ola='oi'), '31\02/2018', '&02#2018']

Para começar a brincadeira eu começo com  duas lista um de datas válidas de diversos formatos e padrões  e outra de datas inválidas O proposito dessas datas invalidas é forçar uma quebra no programa, quando não consigo converter o comportamento desejado pelo meu programa é retornar um dicionário com um código de resposta padrão do protocolo http e uma mensagem, por isso pensei nas mais loucas possibilidades de usuário colocar algo invalido na data, como por exemplo catota no nariz kkkk. 

## Testando converte uma data no formato brasileiro para datetime
Eu pego minha lista de datas no formato brasileiro válido e testo se minha função converte para datetime. O propósito desse teste é ter certeza que daqui um tempo quando adicionar novos formato de datas que as pessoas vão colocar eu possa verificar de maneira simples e prática se seu software ainda consegue converter para datetime

    def test_convert_string_brazil_to_datetime(self):
        """ Test if function convert string for format datetime """
        for d in self.dates:
            date = ConvertDate().convert_date_brasil_for_datetime(d)
            self.assertIsInstance(date, datetime, msg="A função não consegui converter para datetime")

Somente agora com esse cenário definido do que o que eu espero em caso de sucesso e em caso de falha eu começo escrever meu código em si


    def convert_date_brasil_to_datetime(self, date):
        """
        Receive string date in format brazil and and convert in datetime

        Args:
            date (str): date

        Returns:
            datetime in format year/month/day hours:minute:seconds or return dict with  code error
        """
        date = self.valid_string(date)
        if isinstance(date, dict):
            return date
        try:
            date = date.replace('-', '/')
            return datetime.strptime(date, self.datetime_brazil)
        except ValueError:
            return dict(code=415, help=self.format_invalid, msg='Essa data não é válida tem  dígitos sobrando')
        except Exception as e:
            raise e

Começo  chamando a função valid_string() que recebe a data em formato string e tenta verificar se a string pode ser convertida para data.

    def valid_string(self, date):
        """
        Validator if string can convert for datetime. The function try format string for format valid if not possible
        return dict with code 415, msg and help
        Args:
            date (str): date to be validate

        Returns:
            string or dict
        """
        if isinstance(date, str):
            if len(date) == 8:
                return dict(code=415, help=self.format_invalid, msg='A data tem que ter 8 digitos')

            elif len(date) == 10:
                date = f'{date} 00:00:00'
                if date.count('/') == 2 or date.count('-') == 2 and date.count(':') == 2:
                    return date
                else:
                    return dict(code=415, help=self.format_invalid, msg='Está faltando as duas / na data')
            elif len(date) == 19:
                return date
            elif len(date) > 19:
                return dict(code=415, help=self.format_invalid, msg='Essa data não é válida tem numeros sobrando')
            else:
                return dict(code=415, help=self.format_invalid, msg='Essa data não é válida')
        else:
            return dict(code=415, help=self.format_invalid, msg='Opa você está usando caracteres não válidos')


Como não posso ter certeza que o usuário vai digitar a data num padrão que desejo tento prever alguns padrões de datas e adiciono a hora minutos e segundos, para que minha função consiga converter para datetime e que eu possa salvar no meu banco de dados no padrão datetime.

## Testando a função que converte data e hora no padrão americano para datetime
Uma api que consulto traz a data nesse formato "01-10-2018 00:31:29"  então implemento teste para validar se meu código está conseguindo converter para datetime  assim como converti datas no padrão brasileiro para  datetime, assim quero fazer com a com os dados que eu pego via api salvando no banco de dados no formato datetime, e inserindo na planilha somente a data e no formato brasileiro.
 Então começo criando o cenário que recebo 

