# from __future__ import (absolute_import, division, print_function,
#                         unicode_literals)
# import pyarrow
# import os
# import backtrader as bt
# import pandas
#
# def runstrat():
#
#     # Create a cerebro entity
#     cerebro = bt.Cerebro(stdstats=False)
#
#     # Add a strategy
#     cerebro.addstrategy(bt.Strategy)
#
#     datapath = os.getcwd() + '/daily_bars' + '/FESX_eod.parquet.gzip'
#     print(datapath)
#
#     dataframe = pandas.read_parquet(datapath)
#
#     print(dataframe)
#     dataframe.rename(columns={'date': 'datetime'}, inplace=True)
#     dataframe.drop(columns=['adjusted_close'],inplace=True)
#     dataframe['openinterest'] = 0
#     dataframe.datetime = pandas.to_datetime(dataframe.datetime,format='%Y-%m-%d')
#     dataframe.set_index('datetime',inplace=True)
#     print(dataframe)
#
#
#     # Pass it to the backtrader datafeed and add it to the cerebro
#     data = bt.feeds.PandasData(dataname=dataframe)
#
#     cerebro.adddata(data)
#
#     # Run over everything
#     cerebro.run()
#
#     # Plot the result
#     cerebro.plot(style='bar')
#
# if __name__ == '__main__':
#     runstrat()
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import pandas
import datetime  # For datetime objects
import os.path  # To manage paths
import sys  # To find out the script name (in argv[0])
# Import the backtrader platform
import backtrader as bt


# Create a Stratey

class SmaCross(bt.SignalStrategy):
  def __init__(self):
    sma1 = bt.ind.SMA(period=10)
    sma2 = bt.ind.SMA(period=30)
    crossover = bt.ind.CrossOver(sma1, sma2)
    self.signal_add(bt.SIGNAL_LONG, crossover)



if __name__ == '__main__':
    # Create a cerebro entity
    cerebro = bt.Cerebro()

    cerebro.addstrategy(SmaCross)

    datapath = os.getcwd() + '/daily_bars' + '/FESX_eod.parquet.gzip'
    dataframe = pandas.read_parquet(datapath)
    dataframe.rename(columns={'date': 'datetime'}, inplace=True)
    dataframe.drop(columns=['adjusted_close'],inplace=True)
    dataframe['openinterest'] = 0
    dataframe.datetime = pandas.to_datetime(dataframe.datetime,format='%Y-%m-%d')
    dataframe.set_index('datetime',inplace=True)
    print(dataframe)

    data = bt.feeds.PandasData(dataname=dataframe)

    # Add the Data Feed to Cerebro
    cerebro.adddata(data)

    # Set our desired cash start
    cerebro.broker.setcash(1000.0)

    # Add a FixedSize sizer according to the stake
    cerebro.addsizer(bt.sizers.FixedSize, stake=10)

    # Set the commission
    cerebro.broker.setcommission(commission=0.0)

    # Run over everything
    cerebro.run(maxcpus=1)

    cerebro.plot(style='bar')
