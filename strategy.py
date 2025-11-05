from freqtrade.strategy.interface import IStrategy
from pandas import DataFrame

class SimpleStrategy(IStrategy):
    """
    Простая стратегия — вход, если цена выше скользящей средней, выход — если ниже.
    """
    minimal_roi = {"0": 0.03}
    stoploss = -0.10
    timeframe = '5m'

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe['sma'] = dataframe['close'].rolling(window=20).mean()
        return dataframe

    def populate_buy_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[
            (dataframe['close'] > dataframe['sma']),
            'buy'
        ] = 1
        return dataframe

    def populate_sell_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[
            (dataframe['close'] < dataframe['sma']),
            'sell'
        ] = 1
        return dataframe
