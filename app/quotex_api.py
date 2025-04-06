from pyquotex.api import Quotex

class QuotexClient:
    def __init__(self, email, password):
        self.qx = Quotex(email, password)
        self.is_connected = False

    def connect(self):
        if self.qx.profile_balance() is not None:
            self.is_connected = True
            return True
        return False

    def get_profile(self):
        if self.is_connected:
            return self.qx.profile_balance()
        return None

    def place_trade(self, asset, direction, amount, duration=1):
        if self.is_connected:
            return self.qx.buy(amount, asset, direction, duration)
        return None
