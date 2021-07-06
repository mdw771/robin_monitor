import numpy as np

import time

from robin_monitor.settings import Settings
from robin_monitor.stock import Stock


class Trigger(Settings):
    
    def __init__(self):
        super(Trigger, self).__init__()
        self.message = None

    def check(self, stock):
        """
        Run trigger check.

        :param stock: Stock.
        :return: bool.
        """
        return False


class DropBelowThresholdTrigger(Trigger):

    def __init__(self, threshold):
        super(DropBelowThresholdTrigger, self).__init__()
        self.threshold = threshold

    def check(self, stock):
        assert isinstance(stock, Stock)
        if stock.latest < self.threshold:
            self.message = 'Dropped below threshold of {} (latest: {}).'.format(self.threshold, stock.latest)
            return True
        else:
            return False


class DropBelowPercentDayOpenTrigger(Trigger):

    def __init__(self, percent_lower_than_open):
        super(DropBelowPercentDayOpenTrigger, self).__init__()
        self.percent_lower_than_open = percent_lower_than_open

    def check(self, stock):
        assert isinstance(stock, Stock)
        open = float(stock.histories[0]['open_price'])
        if stock.latest < open * (1 - self.percent_lower_than_open):
            self.message = 'Dropped below {} percent of day open {} (latest: {}).'.format(self.percent_lower_than_open,
                                                                                          open,
                                                                                          stock.latest)
            return True
        else:
            return False
