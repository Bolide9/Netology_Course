def get_max_value(self):
    res = self.get_exchanges()

    Currencies = {}

    for currency in res:
        Currencies.update({res[currency]['Name']: res[currency]['Value']})

    max_value = max(Currencies, key=Currencies.get)
    return max_value


get_max_value()
