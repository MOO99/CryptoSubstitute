from controller.clipboard_controller import ClipboardData
from controller.console_controller import ConsoleController
from controller.files_controller import WalletsController


class ConsoleView:
    def __init__(self):

        pass

    @staticmethod
    def show_welcome_message():
        ConsoleController().welcome_message()

    @staticmethod
    def rich_text(text):
        ConsoleController().print_rich_text(text=text)

    @staticmethod
    def rich_input(text=""):
        return ConsoleController().input_rich_text(text=text)

    @staticmethod
    def print_clipboard_content():
        ConsoleController().print_rich_text(
            ClipboardData().clipboard_content())

    def enter_your_wallets(self):
        pass

    @staticmethod
    def confirm_default_wallets_csv():
        WalletsController().confirm_or_create_default_wallets_csv()

    @staticmethod
    def confirm_default_wallets_dir():
        WalletsController().confirm_or_create_default_wallets_dir()
