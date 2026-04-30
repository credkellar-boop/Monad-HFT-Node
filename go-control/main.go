package main

import (
	"fmt"
	"log"
	"os"
	"os/exec"
	"os/signal"
	"syscall"
)

func main() {
	fmt.Println("🚀 Initializing Eternity Ledger: Sovereign Command Center")

	// 1. Start the Rust HFT Node
	rustNode := exec.Command("cargo", "run", "--release")
	rustNode.Stdout = os.Stdout
	rustNode.Stderr = os.Stderr

	if err := rustNode.Start(); err != nil {
		log.Fatalf("❌ Failed to start Rust HFT Node: %v", err)
	}
	fmt.Println("✅ Monad-HFT-Node: ACTIVE")

	// 2. Start the Python Risk Guardian
	pythonRisk := exec.Command("python3", "../risk_guardian.py")
	pythonRisk.Stdout = os.Stdout
	pythonRisk.Stderr = os.Stderr

	if err := pythonRisk.Start(); err != nil {
		log.Printf("⚠️ Warning: Risk Guardian failed to start: %v", err)
	} else {
		fmt.Println("✅ Risk Guardian: ACTIVE")
	}

	// Handle Graceful Shutdown (Ctrl+C)
	stop := make(chan os.Signal, 1)
	signal.Notify(stop, os.Interrupt, syscall.SIGTERM)

	<-stop
	fmt.Println("\n🛑 Shutting down Sovereign systems...")
	
	// Kill processes on exit
	rustNode.Process.Kill()
	if pythonRisk.Process != nil {
		pythonRisk.Process.Kill()
	}
	
	fmt.Println("👋 Systems Offline.")
}
