import requests as http


class Rate:
    def __init__(self, diff: bool):
        self.diff = diff

    def get_exchanges(self):
        r = http.get('https://www.cbr-xml-daily.ru/daily_json.js')
        return r.json()['Valute']

    def get_max_value(self):
        res = self.get_exchanges()

        Currencies = {}

        for currency in res:
            Currencies.update({res[currency]['Name']: res[currency]['Value']})

        max_value = max(Currencies, key=Currencies.get)
        return max_value

    def make_format(self, currency):
        response = self.get_exchanges()

        if currency in response:
            if self.diff:
                return response[currency]['Value'] - response[currency]['Previous']

            if not self.diff:
                return response[currency]

        return 'error'

    def eur(self):
        return self.make_format('EUR')

    def usd(self):
        return self.make_format('USD')

    def jpy(self):
        return self.make_format('JPY')
