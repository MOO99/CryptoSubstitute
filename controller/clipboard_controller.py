
from model.clipboard_data import ClipboardData
from model.crypto_types import BitcoinCrypto
from model.console_handler import RichConsole

#TODO Class take copy and send it to verify

class ClipboardController:
    def __init__(self):
        pass

    def check_wallet_format(self, wallet_to_check):
        return BitcoinCrypto().recognize_format(wallet=wallet_to_check)
    
    def clipboard_data(self):
        return ClipboardData().clipboard_content()

    def paste_new_data(self, text):
        ClipboardData().copy_wallet(text)