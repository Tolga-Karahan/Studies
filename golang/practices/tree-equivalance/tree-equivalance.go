package main

import "golang.org/x/tour/tree"
import "fmt"

// Walk walks the tree t sending all values
// from the tree to the channel ch.
func Walk(t *tree.Tree, ch chan int) {
	// Lets traverse the tree in pre-order
	node := (*t)
	
	if node.Left != nil {
		Walk(node.Left, ch)
	}
	
	ch <- node.Value
	
	if node.Right != nil {
		Walk(node.Right, ch)
	}
}

// Same determines whether the trees
// t1 and t2 contain the same values.
func Same(t1, t2 *tree.Tree) bool {
	ch1 := make(chan int, 10)
	ch2 := make(chan int, 10)
	
	go Walk(t1, ch1)
	go Walk(t2, ch2)
	
	for i := 0; i < cap(ch1); i++ {
		val1 := <- ch1
		val2 := <- ch2
		
		if val1 != val2 {
			return false
		}
	}
	
	return true
}


func main() {
	fmt.Println(Same(tree.New(1), tree.New(1)))
}