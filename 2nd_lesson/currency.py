__author__ = 'vladimir.pekarsky'

import json
import sys
import urllib2


def get_request(*pairs_list):
    request_first_part = ("https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.xchange"
                          "%20where%20pair%20%3D%20%22")
    request_last_part = "%22&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"
    pairs = '%2C'.join(pairs_list)

    return request_first_part + pairs + request_last_part


def get_currency_rate(*currency_list):
    if not currency_list[0]:
        return 'Please provide pairs'

    data = {}
    request = get_request(*currency_list)
    rates = get_rates(request)
    if isinstance(rates, dict):
        data[rates['Name']] = float(rates['Rate'])
    elif isinstance(rates, list):
        for rate in rates:
            data[rate['Name']] = float(rate['Rate'])

    return data


def get_rates(request):
    response = urllib2.urlopen(request)
    check_response_code(response)
    response_str = response.read()
    parsed_str = json.loads(response_str)

    return parsed_str['query']['results']['rate']


def check_response_code(response):
    response_code = response.getcode()
    if response_code != 200:
        print('something went wrong')
        sys.exit(response_code)

print(get_currency_rate('USDBYR', 'EURBYR', 'RUBBYR'))
print(get_currency_rate('USDBYR', 'EURBYR'))
print(get_currency_rate('USDEUR', 'EURUSD'))
print(get_currency_rate('USDBYR'))
print(get_currency_rate([]))
