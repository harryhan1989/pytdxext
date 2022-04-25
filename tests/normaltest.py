import pandas
import pytest
from pytdxext.__main__ import bestip

from pytdxext.quotes import Quotes
from pytdxext import consts

client = Quotes.factory(market='std',forceip=["8.129.13.54",7709], timeout=10)
data = client.transactions(symbol='600519',start=0, offset=2000,date=20090105)
print(len(data))
print(data['vol'].sum())
print(data['price'][0])
print(data.iloc[-1])

client = Quotes.factory(market='std',forceip=["139.159.239.163",7709], timeout=10)
data = client.transactions(symbol='600519',start=0, offset=2000,date=20090105)
print(len(data))
print(data['vol'].sum())
print(data['price'][0])
print(data.iloc[-1])

# client = Quotes.factory(market='std')
# symbol = client.stocks(market=44)
# df1=symbol[(symbol.code == '835179')]
# print(symbol)