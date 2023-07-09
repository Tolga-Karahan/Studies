// Mutexes are used to ensure that only one
// goroutine can access to a resource at a time

package main

import (
	"fmt"
	"sync"
	"time"
)

// A counter with a mutex
type SafeCounter struct {
	mu sync.Mutex
	v map[string]int
}

// Increments the counter for the given key by
// ensuring only one goroutine access at a time
func (c *SafeCounter) Inc(key string) {
	c.mu.Lock()
	c.v[key]++
	c.mu.Unlock()
}

// Return current value of the counter by
// ensuring only one goroutine access at a time
func (c *SafeCounter) Value(key string) int {
	c.mu.Lock()
	// We can also use defer to ensure that
	// mutex is unlocked in the end
	defer c.mu.Unlock()
	return c.v[key]
}

func main() {
	counter := SafeCounter{v: make(map[string]int)}
	for i := 0; i < 100; i++ {
		counter.Inc("somekey")
	}

	time.Sleep(time.Second)
	fmt.Println(counter.Value("somekey"))
}
