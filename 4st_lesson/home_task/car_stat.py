# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

import csv
import urllib2
import xml.etree.ElementTree as ET

request = 'http://www.nbrb.by/Services/XmlExRates.aspx'
csv_file = 'car_stats.csv'


def print_requested_info(file):
    prepared_data = get_data_from_csv_file(file)
    months_in_use = count_months(prepared_data)
    oil_cost_all_time = sum_of_column(prepared_data, 3)
    charged_oil_all_time = sum_of_column(prepared_data, 2)
    all_run = prepared_data[-1][1]

    average_spending_by_month = oil_cost_all_time / months_in_use
    average_rate_liters_of_oil_by_100km = charged_oil_all_time / (all_run / 100)

    print('For all time Varvara has spent about {} BYR for oil.'
          .format(oil_cost_all_time))
    print('Average spending by month {} BYR'.
          format(average_spending_by_month))
    print('Average rate liters of oil by 100km: {}'
          .format(average_rate_liters_of_oil_by_100km))


def prepare_data(data):
    convert_date_to_digits(data)
    exchange_currency(data)
    prepared_data = get_rid_empty_string(data)

    return prepared_data


def get_data_from_csv_file(file):
    car_stat_file = open(file)
    car_stat_reader = csv.reader(car_stat_file)
    car_stat_full_data = list(car_stat_reader)
    prepared_data = prepare_data(car_stat_full_data[1:])

    return prepared_data


def get_currency_as_xml_string(url):
    response = urllib2.urlopen(request)
    response_string = response.read()

    return response_string


def get_exchange_rate(required_currency):
    currency_xml_string = get_currency_as_xml_string(request)
    root = ET.fromstring(currency_xml_string)

    for currency in root.findall('Currency'):
        char_code = currency.find('CharCode').text
        if char_code == required_currency:
            return currency.find('Rate').text


def convert_date_to_digits(data):
    for row in data:
        for index, column in enumerate(row):
            if column.isdigit():
                row[index] = int(column)
            elif '.' in column:
                splited_column = column.split('.')
                if splited_column[0].isdigit():
                    row[index] = float(column)


def exchange_currency(data):
    for row in data:
        if row[5] == 'RUR':
            exchange_rate = float(get_exchange_rate('RUB'))
            row[4] = int(row[4] * exchange_rate)
            row[3] = int(row[3] * exchange_rate)
            row[5] = 'BYR'


def get_rid_empty_string(data):
    for index, row in enumerate(data):
        if not row[0]:
            data = data[:index]

    return data


def sum_of_column(prepared_data, column):
    sum = 0
    for row in prepared_data:
        sum += row[column]

    return sum


def count_months(prepared_data):
    months = set()
    for row in prepared_data:
        if row[0]:
            months_data = row[0].split('/')
            months.add(months_data[0] + months_data[2])

    return len(months)


print_requested_info(csv_file)


