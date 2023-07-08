// Channels are typed conduits to and from which values
// can be sent and read. <- operator is used to send and
// receive values. By default sending and receiving is
// blocked until other end is ready. Thanks to this
// feature goroutines can synchronize without explicit
// locks or condition variables.

package main

import "fmt"

func sum(s []int, c chan int) {
	sum := 0
	for _, v := range s {
		sum += v
	}
	c <- sum
}

func main() {
	// Channels must be created before usage
	ch := make(chan int)

	// We can define a buffered channel too
	// by providing size with second argument
	// Sends to a full buffered channel is a
	// blocking operation. Reads from a empty
	// buffered channel is also a blocking
	// operation.

	// Define the slice on which gorounites
	// will work
	s := []int {7, 2, 8, -9, 4, 0}

	go sum(s[:len(s)/2], ch)
	go sum(s[len(s)/2:], ch)

	// Runs when goroutines finish
	sum_last, sum_first := <-ch, <-ch

	fmt.Printf("Sum of the first half: %v\n", sum_first)
	fmt.Printf("Sum of the second half: %v\n", sum_last)
}