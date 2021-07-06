from robin_monitor.settings import Settings


class Stock(Settings):

    def __init__(self, symbol):
        super(Stock, self).__init__()
        self.symbol = symbol
        self.histories = {'day': None,
                          'week': None,
                          'month': None,
                          'year': None
                          }
        self.latest = None

    def set_history(self, history, type='day'):
        """
        Set day history.

        :param history: List. A list returned by robin_stocks.robinhood.stocks.get_stock_historicals.
                        This is a list of dictionaries where each dictionary is for a different time. If multiple
                        stocks are provided the historical data is listed one after another.
                        Dictionary Keys:
                        begins_at
                        open_price
                        close_price
                        high_price
                        low_price
                        volume
                        session
                        interpolated
                        symbol
        """
        self.histories[type] = history