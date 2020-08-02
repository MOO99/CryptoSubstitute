from model.console_handler import RichConsole
from time import sleep


class ConsoleController:
    def __init__(self):
        pass

    def rich_traceback_handler(self):
        """Calls Rich traceback handler installer"""
        RichConsole().install_rich_traceback_handler()

    def welcome_message(self):
        RichConsole().print_btc_ascii_logo()
        sleep(1)

    def print_rich_text(self, text):
        RichConsole().print_rich_text(text=text)

    def input_rich_text(self, text):
        return RichConsole().input_rich_text(text=text)
