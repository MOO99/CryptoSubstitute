from time import sleep

from model.console_handler import RichConsole


class ConsoleController:
    def __init__(self):
        pass

    @staticmethod
    def rich_traceback_handler():
        """Calls Rich traceback handler installer"""
        RichConsole().install_rich_traceback_handler()

    @staticmethod
    def welcome_message():
        RichConsole().print_btc_ascii_logo()
        sleep(1)

    @staticmethod
    def print_rich_text(text):
        RichConsole().print_rich_text(text=text)

    @staticmethod
    def input_rich_text(text):
        return RichConsole().input_rich_text(text=text)
