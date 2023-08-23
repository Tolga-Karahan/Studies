package main

import (
	"fmt"
)

/* 
	Go functions can work on multiple
	types by using type parameters.
	An example signature:
	func Index[T comparable](s []T, x T) int

	Above signature states that T is
	any type that fulfills built-in
	comparable constraint.

	Besides generic functions, generic
	types also can be created:

	type List[T any] struct {
		next *List[T]
		val T
	}
*/

// comparable constraint is used to ensure
// that we can use comparison operators
func Index[T comparable](arr []T, elem T) int {
	for i, val := range arr {
		if val == elem {
			return i
		}
	}
	return -1
}

// A generic Linked list that
// holds values of any type
type LinkedList[T any] struct {
	next *LinkedList[T]
	value T
}

func (v LinkedList[T]) String() string {
	return fmt.Sprintf("Value: %v\n", v.value)
}

func main() {
	int_arr := []int{1, 2, 3}
	fmt.Printf("Index of 2 is: %d\n", Index(int_arr, 2))

	str_arr := []string{"abc", "qwe", "hdf"}
	fmt.Printf("Index of abc is: %d\n", Index(str_arr, "abc"))

	a_val := LinkedList[int]{nil, 6}
	fmt.Print(a_val)
}