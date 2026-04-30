# Eternity Sovereign Reinvestment Logic
class Reinvestor:
    def __init__(self, weekly_profit):
        self.profit = weekly_profit
        self.allocation = {
            "Crypto": 0.25,
            "Stocks": 0.25,
            "Forex": 0.25,
            "Banking": 0.15,
            "AI_Research": 0.10
        }

    def distribute(self):
        print(f"--- Alpha-One Disbursement: ${self.profit:,} ---")
        for asset, pct in self.allocation.items():
            amount = self.profit * pct
            print(f"Allocating ${amount:,.2f} to {asset}")

if __name__ == "__main__":
    # Example test run
    bot = Reinvestor(500000)
    bot.distribute()
