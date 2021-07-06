import time
import datetime
import logging

import robin_stocks
import robin_stocks.robinhood.stocks

from robin_monitor.settings import Settings
from robin_monitor.user import *
from robin_monitor.notifier import *
from robin_monitor.stock import *


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')


class Monitor(Settings):

    def __init__(self, refresh_interval_sec=60):
        super(Monitor, self).__init__()
        self.user = None
        self.notifier = None
        self.watch_dict = {}
        self.refresh_interval_sec = refresh_interval_sec

    def set_user(self, user):
        assert isinstance(user, User)
        self.user = user

    def add_watch(self, stock, trigger_ls, action_ls):
        """
        Add a stock into watch.

        :param stock: Stock.
        :param trigger_ls: List of Trigger.
        :param action_ls: List of Action.
        """
        self.watch_dict[stock] = (trigger_ls, action_ls)

    def refresh_all_stocks(self):
        for i, stock in enumerate(list(self.watch_dict.keys())):
            latest = robin_stocks.robinhood.stocks.get_latest_price(stock.symbol)
            stock.latest = float(latest[0])
            history_day = robin_stocks.robinhood.stocks.get_stock_historicals(stock.symbol, interval='10minute', span='day')
            stock.set_history(history_day, type='day')
            logging.info('Refreshed {}: latest = {}.'.format(stock.symbol, stock.latest))

    def run(self):
        logging.info('Logging in...')
        robin_stocks.robinhood.login(self.user.robin_username,
                                     self.user.robin_password,
                                     store_session=True)
        logging.info('Monitor running.')
        while True:
            self.refresh_all_stocks()
            for i, (stock, (trigger_ls, action_ls)) in enumerate(self.watch_dict.items()):
                for trigger in trigger_ls:
                    if trigger.check(stock):
                        for action in action_ls:
                            logging.info('Action triggered by {}.'.format(stock.symbol))
                            action.run(stock, trigger)

            time.sleep(self.refresh_interval_sec)

