__author__ = 'vladimir.pekarsky'

import json
import sys
import urllib2

init_request = ("https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.xchange"
                "%20where%20pair%20%3D%20%22USDBYR%2CEURBYR%2CRUBBYR%22&format=json&env="
                "store%3A%2F%2Fdatatables.org%2Falltableswithkeys")


def get_currency_rate(*currency_list):
    data = {}
    rate_list = get_rate_list(init_request)
    for currency in currency_list:
        for rate in rate_list:
            if currency == rate['id']:
                data[rate['Name']] = float(rate['Rate'])

    return data


def get_rate_list(request):
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
print(get_currency_rate('USDBYR'))
