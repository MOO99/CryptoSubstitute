import re

class UnspecifiedCrypto:
    def __init__(self, replacement_wallet: str = "", target_wallet: str = ""):
        self.replacement_wallet = replacement_wallet
        self.target_wallet = target_wallet

    def get_replacement(self):
        return self.replacement_wallet

    def set_replacement(self, replacement_wallet: str):
        self.replacement_wallet = replacement_wallet

class BitcoinCrypto(UnspecifiedCrypto):
    def __init__(self, replacement_wallet = "", target_wallet = ""):
        super().__init__(replacement_wallet, target_wallet)
        #self.address_formats_regex = {
        #    "P2PKH" : "^[1][a-km-zA-HJ-NP-Z1-9]{25,34}$",
        #    "P2SH" : "^[3][a-km-zA-HJ-NP-Z1-9]{25,34}$",
        #    "Bech32" : "\bbc(0([ac-hj-np-z02-9]{39}|[ac-hj-np-z02-9]{59})|1[ac-hj-np-z02-9]{8,87})\b"
        #}
        self.regex_P2PKH = "^[1][a-km-zA-HJ-NP-Z1-9]{25,34}$"
        self.regex_P2SH = "^[3][a-km-zA-HJ-NP-Z1-9]{25,34}$"
        self.regex_Bech32 = """bc(0([ac-hj-np-z02-9]{39}|[ac-hj-np-z02-9]{59})|1[ac-hj-np-z02-9]{8,87})"""

    def recognize_and_set_format(self, wallet: str): #TODO add controller entry for this one
        if(re.search(self.regex_P2PKH, wallet)):
            return f"{wallet}:P2PKH:BTC"
        elif(re.search(self.regex_P2SH, wallet)):
            return f"{wallet}:P2SH:BTC"
        elif(re.search(self.regex_Bech32, wallet)):
            return f"{wallet}:Bech32:BTC"
        else:
            return None

    def recognize_format(self, wallet: str):
        if(re.search(self.regex_P2PKH, wallet)):
            return "P2PKH"
        elif(re.search(self.regex_P2SH, wallet)):
            return "P2SH"
        elif(re.search(self.regex_Bech32, wallet)):
            return "Bech32"
        else:
            return None


#TODO TAKE CRYPTO
#TODO ASSIGN IT TO CLASS
#TODO ASK IF IT'S LEGIT AND DEFINE FORMAT
#TODO REPLACE TARGET
