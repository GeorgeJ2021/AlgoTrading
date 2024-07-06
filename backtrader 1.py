import backtrader as bt
import datetime
from strategy1 import TestStrategy

cerebro = bt.Cerebro()
cerebro.broker.set_cash(10000)

data = bt.feeds.YahooFinanceCSVData(
        dataname='NVDA.csv',
        # Do not pass values before this date
        fromdate=datetime.datetime(2023, 7, 3),
        # Do not pass values before this date
        todate=datetime.datetime(2024, 7, 3),
        # Do not pass values after this date
        reverse=False)


cerebro.adddata(data)
cerebro.addstrategy(TestStrategy)
cerebro.addsizer(bt.sizers.FixedSize, stake=10)

print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
cerebro.run()
print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
cerebro.plot()