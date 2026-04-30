package main

import "fmt"

type Allocation struct {
	GeminiResearch float64
	Banking        float64
}

func GetAllocation(earnings float64) Allocation {
	return Allocation{
		GeminiResearch: earnings * 0.80,
		Banking:        earnings * 0.20,
	}
}

func main() {
    // Test logic
    earnings := 500000.0
    alloc := GetAllocation(earnings)
    fmt.Printf("Alpha-One Disbursement - Research: $%.2f, Banking: $%.2f\n", alloc.GeminiResearch, alloc.Banking)
}
