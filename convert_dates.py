from datetime import datetime


class ConvertDate(object):
    def __init__(self):
        # 2018/10/31 00:31:29
        self.datetime_american = '%Y-%m-%d %H:%M:%S'
        self.datetime_brazil = '%d/%m/%Y %H:%M:%S'
        self.date_american = '%m/%d/%Y'
        self.date_brazil = '%d/%m/%Y'
        self.format_invalid = 'Esse é o formato aceito xx/xx/xxxx'

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

    def convert_date_american_to_datetime(self, date):
        """
        Receive string date in format american and and convert in datetime

        Args:
            date (str): date

        Returns:
            datetime in format year/month/day hours:minute:seconds or return dict with  code error
        """
        date = self.valid_string(date)
        if isinstance(date, dict):
            return date
        try:
            date = date.replace('/', '-')
            return datetime.strptime(date, self.datetime_american)
        except ValueError:
            return dict(code=415, help=self.format_invalid, msg='Essa data não é válida tem  dígitos sobrando')
        except Exception as e:
            raise e

    def convert_datetime_to_date_brazil(self, date):
        """
        Receive  datetime in format american and convert for string in format day/month/year
        Args:
            date (datetime):

        Returns:

        """
        if isinstance(date, datetime):
            return date.strftime(self.date_brazil)
        else:
            return dict(code=415, help=self.format_invalid, msg='Não Foi possível converter a data')

    def convert_datetime_to_date_american(self, date):
        """
        Receive datetime in format american and convert for string in format year-month-day hour:minute:second
        Args:
            date (datetime):

        Returns:

        """
        if isinstance(date, datetime):
            return date.strftime(self.datetime_american)
        else:
            return dict(code=415, help=self.format_invalid, msg='Não Foi possível converter a data')
