from model.console_handler import RichConsole
from time import sleep

class ConsoleView:
    def __init__(self):
        pass

    def rich_traceback_handler(self):
        """Calls Rich traceback handler installer"""
        RichConsole().install_rich_traceback_handler()

    def welcome_message(self):
        RichConsole().print_btc_ascii_logo()
        sleep(1)