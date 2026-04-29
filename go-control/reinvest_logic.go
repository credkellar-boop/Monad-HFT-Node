package main

type Allocation struct {
	Crypto, Stocks, Forex, Banking, AI float64
}

func GetAllocation(earnings float64) Allocation {
	return Allocation{
		Crypto: earnings * 0.25,
		Stocks: earnings * 0.25,
		Forex:  earnings * 0.25,
		Banking: earnings * 0.15,
		AI:     earnings * 0.10,
	}
}
