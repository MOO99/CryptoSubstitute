from pyperclip import copy
from pyperclip import paste


class ClipboardData:
    def __init__(self):
        pass

    @staticmethod
    def copy_wallet(wallet):
        copy(wallet)

    @staticmethod
    def clipboard_content():
        return paste()
