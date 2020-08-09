from model.clipboard_data import ClipboardData
from model.console_handler import RichConsole
from model.crypto_types import BitcoinCrypto

# TODO Class take copy and send it to verify


class ClipboardController:
    def __init__(self):
        pass

    @staticmethod
    def check_wallet_format(wallet_to_check):
        if BitcoinCrypto().recognize_format(wallet=wallet_to_check) is not None:
            return BitcoinCrypto().recognize_and_set_format(
                wallet=wallet_to_check)

        # if whatever-else-wallet:
        # return that wallet with type of encryption and currency name
        else:
            return None

    @staticmethod
    def clipboard_data():
        return ClipboardData().clipboard_content()

    @staticmethod
    def paste_new_data(text):
        ClipboardData().copy_wallet(text)
