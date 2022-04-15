import pandas
import pytest

from pytdxext.quotes import Quotes
from pytdxext.consts import MARKET_SH

client = Quotes.factory(market='std', timeout=10)
data = client.transactions(symbol='600036',start=0, offset=10,date=20110209)
print(data)