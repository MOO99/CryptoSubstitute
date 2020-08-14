from models.unspecified_crypto_model import UnspecifiedCryptoModel


class BTCCryptoModel(UnspecifiedCryptoModel):
    def __init__(self, target: str = "", replacement: str = ""):
        super(BTCCryptoModel, self).__init__(target, replacement)
        self.regex_P2PKH = "^[1][a-km-zA-HJ-NP-Z1-9]{25,34}$"
        self.regex_P2SH = "^[3][a-km-zA-HJ-NP-Z1-9]{25,34}$"
        self.regex_Bech32 = """bc(0([ac-hj-np-z02-9]{39}|[ac-hj-np-z02-9]{59})|1[ac-hj-np-z02-9]{8,87})"""

