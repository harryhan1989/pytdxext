import pandas
import pytest

from pytdxext.quotes import Quotes
from pytdxext.consts import MARKET_SH

client = Quotes.factory(market='std', timeout=10)
data = client.transactions(symbol='000001',start=0, offset=2000,date=20020419)
print(data)