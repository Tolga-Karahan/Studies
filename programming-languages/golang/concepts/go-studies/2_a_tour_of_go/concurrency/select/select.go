// select statement makes a goroutine wait on multiple
// communication operations. It blocks until one of its
// cases can run. If multiple cases can run, it selects
// one at random.

package main

import "fmt"

func fibonacci(c, quit chan int) {
	first, second := 0, 1
	for {
		select {
			case c <- first:
				first, second = second, first + second
			case <-quit:
				fmt.Println("quit")
				return
		}
	}
}

func main() {
	c := make(chan int)
	quit := make(chan int)

	go func() {
		for i:=0; i < 10; i++ {
			fmt.Println(<-c)
		}
		// What we send doesn't matter
		quit <- 7
	}()
	fibonacci(c, quit)

	// We can also add a default case
	// in which no other case can run

}