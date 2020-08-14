class UnspecifiedCryptoModel:
    def __init__(self, target: str = "", replacement: str = ""):
        self._target = target
        self._replacement = replacement

    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, new_target: str):
        self._target = new_target

    @property
    def replacement(self):
        return self._replacement

    @replacement.setter
    def replacement(self, new_replacement: str):
        self._replacement = new_replacement


class UnrecognizedCurrencyError(ValueError):
    def __init__(self, *args):
        super().__init__(*args)

