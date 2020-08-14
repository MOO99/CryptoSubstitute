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
        self.user_friendly_types = {
            "p2pkh": _("Legacy"),
            "p2sh": _("Segwit wrapped"),
            "bech32": _("Segwit")
        }
