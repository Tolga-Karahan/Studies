// A goroutine is a lightweight thread managed by Go runtime.
// go f(x, y, z) starts a new goroutine by running f(x, y, z)
// Evaluation of the function and parameters are evaluated in
// the current goroutine, and execution happens in the new 
// goroutine. Goroutines share same address space, so resources
// must be synchronized.

package main

import (
	"fmt"
	"time"
)

func say(s string) {
	for i := 0; i < 5; i++ {
		time.Sleep(100 * time.Millisecond)
		fmt.Println(s)
	}
}

func main() {
	go say("world")
	say("hello")
}
