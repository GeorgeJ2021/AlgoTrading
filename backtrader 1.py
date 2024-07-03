import backtrader as bt
import datetime
from strategy1 import TestStrategy

cerebro = bt.Cerebro()
cerebro.broker.set_cash(10000)

data = bt.feeds.YahooFinanceCSVData(
        dataname='oracle 1995_2014.csv',
        # Do not pass values before this date
        fromdate=datetime.datetime(2000, 1, 1),
        # Do not pass values before this date
        todate=datetime.datetime(2000, 12, 31),
        # Do not pass values after this date
        reverse=False)


cerebro.adddata(data)
cerebro.addstrategy(TestStrategy)

print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
cerebro.run()
print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())