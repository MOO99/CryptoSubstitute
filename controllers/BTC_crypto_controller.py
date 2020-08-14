from models.BTC_crypto_model import BTCCryptoModel
from views.BTC_crypto_view import BTCCryptoView
from models.unspecified_crypto_model import UnrecognizedCurrencyError
import re


class BTCCryptoController:
    def __init__(self, target: str = None, replacement: str = None, model=BTCCryptoModel()):
        self._model = model
        self._target = target if target is not None else self._model.target
        self._replacement = replacement if replacement is not None else self._model.replacement
        self._regex_P2PKH = self._model.regex_P2PKH
        self._regex_P2SH = self._model.regex_P2SH
        self._regex_Bech32 = self._model.regex_Bech32

    def is_P2PKH(self, wallet: str):
        return True if re.search(self._regex_P2PKH, wallet) else False

    def is_P2SH(self, wallet: str):
        return True if re.search(self._regex_P2SH, wallet) else False

    def is_Bech32(self, wallet: str):
        return True if re.search(self._regex_Bech32, wallet) else False

    def is_BTC(self, wallet: str):
        return True if self.is_P2PKH(wallet) or self.is_P2SH(wallet) or self.is_Bech32(wallet) else False

    def determine_format(self, wallet: str, user_friendly: bool = False):
        if self.is_P2PKH(wallet) and user_friendly is False:
            return BTCCryptoView().types["p2pkh"]
        elif self.is_P2PKH(wallet) and user_friendly is True:
            return BTCCryptoView().user_friendly_types["p2pkh"]

        elif self.is_P2SH(wallet) and user_friendly is False:
            return BTCCryptoView().types["p2sh"]
        elif self.is_P2SH(wallet) and user_friendly is True:
            return BTCCryptoView().user_friendly_types["p2sh"]

        elif self.is_Bech32(wallet) and user_friendly is False:
            return BTCCryptoView().types["bech32"]
        elif self.is_Bech32(wallet) and user_friendly is True:
            return BTCCryptoView().user_friendly_types["bech32"]
        else:
            raise UnrecognizedCurrencyError("Please enter valid BTC wallet!")
