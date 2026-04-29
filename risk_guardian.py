class RiskGuardian:
    def __init__(self, max_drawdown=0.02):
        self.max_drawdown = max_drawdown

    def validate_trade(self, balance, risk_amount):
        if risk_amount > (balance * self.max_drawdown):
            return False, "Risk limit exceeded"
        return True, "Trade authorized"
