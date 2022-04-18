import pandas
import pytest
from pytdxext.__main__ import bestip

from pytdxext.quotes import Quotes
from pytdxext.consts import MARKET_SH

client = Quotes.factory(market='std',forceip="106.14.201.131", timeout=10)
data = client.transactions(symbol='000001',start=0, offset=2000,date=20020419)
print(data)