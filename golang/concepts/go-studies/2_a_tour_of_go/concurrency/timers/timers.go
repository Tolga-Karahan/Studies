package main

import (
	"fmt"
	"math/rand"
	"time"
)

func populateChannel(c chan int) {
	for {
		c <- rand.Intn(100)
	}
}

func main() {
	ticker := time.NewTicker(200 * time.Microsecond)
	c := make(chan int)

	go populateChannel(c)

	for {
		select {
			case v := <- c:
				fmt.Println(v)
			case <- ticker.C:
				fmt.Println("Game Over!")
				return
		}
	}
}