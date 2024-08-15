import os, sys, argparse
import pandas as pd 
import backtrader as bt
from strategies.goldencross import GoldenCross

cerebro = bt.Cerebro()
cerebro.broker.setcash(10000)

spy_prices = pd.read_csv('NVDA5Y.csv', index_col='Date', parse_dates=True)

feed = bt.feeds.PandasData(dataname=spy_prices)
cerebro.adddata(feed)

cerebro.addstrategy(GoldenCross)

cerebro.run()
cerebro.plot()