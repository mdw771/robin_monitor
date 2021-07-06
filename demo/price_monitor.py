import robin_monitor

user = robin_monitor.User()
user.try_load_credentials()

notifier = robin_monitor.GmailNotifier(user)

monitor = robin_monitor.Monitor(refresh_interval_sec=30)
monitor.set_user(user)

email_action = robin_monitor.SendEmailAction(notifier, silent_time_sec=3600)

monitor.add_watch(robin_monitor.Stock('NVDA'),
                  [robin_monitor.DropBelowThresholdTrigger(820)],
                  [email_action])

monitor.run()
