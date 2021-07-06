import time
import logging

from robin_monitor.settings import Settings
from robin_monitor.stock import Stock
from robin_monitor.notifier import *


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')


class Action(Settings):

    def __init__(self, silent_time_sec=3600):
        """
        Action to perform after Trigger returns True.

        :param silent_time_sec: float. Silent period following an executed action, in seconds. Use a reasonable
            value for this option, so that the software won't perform the action every time the triggers are checked,
            in case the trigger condition holds true for an elongated period (for example, when the latest stock
            price keeps below the set threshold). Use np.inf or a exceedingly large number to make the action one-time.
            Note: when the process is rerun, the timer will be reset.
        """
        super(Action, self).__init__()
        self.last_action_time = -2 ** 31
        self.silent_time_sec = silent_time_sec

    def update_last_action_time(self):
        self.last_action_time = time.time()

    def run(self, stock, trigger):
        return


class SendEmailAction(Action):

    def __init__(self, notifier, silent_time_sec=3600):
        super(SendEmailAction, self).__init__(silent_time_sec=silent_time_sec)
        assert isinstance(notifier, EmailNotifier)
        self.notifier = notifier

    def run(self, stock, trigger):
        if time.time() - self.last_action_time >= self.silent_time_sec:
            subject = 'Robin-Monitor: {} triggered an alarm'.format(stock.symbol)
            body = """
            Stock symbol: {}\n
            Trigger message: {}
            """.format(stock.symbol, trigger.message)
            logging.info('Sending email...')
            print(subject, body)
            self.notifier.send_email(subject, body)
            self.update_last_action_time()
        return
