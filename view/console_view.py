from controller.console_controller import ConsoleController
from controller.clipboard_controller import ClipboardData
from controller.files_controller import WalletsController


class ConsoleView:
    def __init__(self):
        pass

    def show_welcome_message(self):
        ConsoleController().welcome_message()

    def rich_text(self, text):
        ConsoleController().print_rich_text(text=text)

    def rich_input(self, text=''):
        return ConsoleController().input_rich_text(text=text)

    def print_clipboard_content(self):
        ConsoleController().print_rich_text(ClipboardData().clipboard_content())

    def enter_your_wallets(self):
        pass

    def confirm_default_wallets_csv(self):
        WalletsController().confirm_or_create_default_wallets_csv()

    def confirm_default_wallets_dir(self):
        WalletsController().confirm_or_create_default_wallets_dir()
