from controllers.localization_controller import LocalizationController

# noinspection PyProtectedMember
_ = LocalizationController()._


class BTCCryptoView:
    def __init__(self):
        self.types = {
            "p2pkh": _("P2PKH"),
            "p2sh": _("P2SH"),
            "bech32": _("BECH32")
        }
