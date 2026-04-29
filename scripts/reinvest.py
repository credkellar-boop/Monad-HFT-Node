def process_reinvestment(earnings):
    allocation = {
        "Crypto_Staking": earnings * 0.25,
        "Stocks_Tech": earnings * 0.25,
        "Forex_Liquidity": earnings * 0.25,
        "Banking_Reserves": earnings * 0.15,
        "AI_Research": earnings * 0.10
    }
    return allocation

if __name__ == "__main__":
    weekly_profit = 500000 # Example
    print(process_reinvestment(weekly_profit))
