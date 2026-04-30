import os
from decimal import Decimal
from dotenv import load_dotenv

load_dotenv()

class SovereignReinvestor:
    def __init__(self, weekly_profit):
        # Updated to the 80/20 split mandate
        self.profit = Decimal(str(weekly_profit))
        self.reinvest_rate = Decimal('0.80')
        self.liquid_rate = Decimal('0.20')
        
    def calculate_allocation(self):
        """
        Calculates the split for Gemini research and operational liquidity.
        """
        to_research = self.profit * self.reinvest_rate
        to_checking = self.profit * self.liquid_rate
        
        return {
            "gemini_research_80": float(to_research),
            "liquid_checking_20": float(to_checking)
        }

    def distribute(self):
        allocation = self.calculate_allocation()
        print(f"--- Alpha-One Disbursement: ${self.profit} ---")
        for asset, amount in allocation.items():
            print(f"Allocating ${amount:,.2f} to {asset}")

if __name__ == "__main__":
    # Example logic test for Alpha-One
    test_earnings = 500000 
    bot = SovereignReinvestor(test_earnings)
    bot.distribute()
