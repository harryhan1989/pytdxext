import pandas
import pytest
from pytdxext.__main__ import bestip

from pytdxext.quotes import Quotes
from pytdxext import consts

# ips=['120.79.60.82', '8.129.13.54', '120.24.149.49', '47.113.94.204', '8.129.174.169',
#         '47.113.123.248', '47.103.48.45', '47.100.236.28', '101.133.214.242', '47.116.21.80', '47.116.105.28',
#         '47.116.10.29', '39.98.234.173', '39.98.198.249', '39.100.68.59', '58.23.131.163', '218.6.170.47', '123.125.108.14', '180.153.18.170', '180.153.18.171',
#         '60.191.117.167', '115.238.56.198', '218.75.126.9',
#         '115.238.90.165', '60.12.136.250', '218.108.98.244', '218.108.47.69', '114.80.63.12', '114.80.63.35',
#         '119.147.212.81', '101.133.214.242', '114.80.149.19', '114.80.149.21', '114.80.149.22', '114.80.149.91',
#         '114.80.149.92', '59.36.5.11', '119.29.19.242', '117.34.114.13', '117.34.114.14', '117.34.114.15', '117.34.114.16',
#         '117.34.114.17', '117.34.114.18', '117.34.114.20', '117.34.114.27', '117.34.114.30', '58.63.254.247',
#         '123.125.108.90', '175.6.5.153', '182.118.47.151', '182.131.3.245', '202.100.166.27', '58.63.254.191',
#         '58.63.254.217', '202.100.166.21', '202.96.138.90', '218.106.92.182', '218.106.92.183', '220.178.55.71',
#         '220.178.55.86']
ips=['106.14.201.131']
for ip in ips:
    print(ip)
    client = Quotes.factory(market='std',forceip=[ip,7709], timeout=2)
    data = client.transactions(symbol='600519',start=0, offset=2000,date=20220401)
    print(data)
# print(len(data))
# print(data['vol'].sum())
# print(data['price'][0])
# print(data.iloc[-1]['price'])
# print(data['price'].max())
# print(data['price'].min())


# client = Quotes.factory(market='std')
# symbol = client.stocks(market=44)
# df1=symbol[(symbol.code == '835179')]
# print(symbol)