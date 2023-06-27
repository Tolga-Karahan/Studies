package intro

import "fmt"

// Global declaration
var g int

// An example struct
type Vertex struct {
	X int
	Y int
}

// A closure example
// A closure is a function value that
// references variables outside its body
func adder() func(int) int {
	sum := 0
	return func(x int) int {
		sum += x
		return sum
	}
}

// We can provide arbitrary number of
// arguments to variadic functions. To
// make a variadic function, "..." is
// added to parameter type as prefix.
// This parameter can be iterated like
// a slice. To send values from a slice
// to a variadic function, "..." is used
// after names of the slice in function 
// call: variadicFunction(a_slice...)
func variadicFunction(vary ...int) {
	sum := 0

	for _, num := range vary {
		sum += num
	}

	fmt.Printf("Sum: %d\n", sum)
}

func main() {
	// To declare variables we use var
	var a, b int

	// Inside a function we can use :=
	// short assignment statement to 
	// declare and assign value
	c := 5

	/* Basic GO types:
	bool
	string
	int int8 int16 int32 int64
	uint  uint8 uint16 uint32 uint64 uintptr

	byte: alias for uint8

	rune: represents a Unicode code point
	alias for int32

	float32 float64

	complex64 complex128
	*/

	// const keyword used to declare constants
	const i := 5

    // Go only one looping construct: for loop
	for i:=0; i < 5; i++{
		fmt.Println(i)
	}

	// We can use for loop as while loop
	sum := 1
	for sum < 100 {
		sum += sum
	}

	/* infinite loop
	for {
	
	}*/

	// if statement also doesn't require
	// parentheses around conditions
	if sum < 100 {
		fmt.Println(sum)
	}

	// We can define an initial statement
	// with if as we do with for loops
	if x := 5; x < 6 {
		fmt.Println(x)
	}

	// Variables declared in initial statements
	// are also available in else blocks
	if x := 5; x > 6 {
		fmt.Sprintln(x, "is greater than 6")
	} else {
		fmt.Srintln(x, "is less than 6")
	}

	// GO inserts break statements to switch
	// constructs by itself, so it only runs
	// the selected case. Swich cases don't
	// have to be constant and values don't
	// have to be integers.
	fmt.Print("Go runs on ")
	switch os := runtime.GOOS; os {
	case "darwin":
		fmt.Println("OS X.")
	case "linux":
		fmt.Println("Linux.")
	default:
		fmt.Printf("%s. \n", os)
	}

	// defer keyword defers the execution of
	// a function until it returns, but its
	// arguments are evaluated immediately
	defer fmt.Println("Hello")
	fmt.Println("World")

	// Instantiate a struct and print it
	fmt.Println(Vertex{1, 2})

	// Print just a field of a struct
	v = Vertex{1, 2}
	v.X = 3
	fmt.Println(v.X)

	// When using a pointer to a struct
	// no need to explicitly dereference it
	p := &v
	p.Y = 5
	fmt.Println(v)

	// We can provide a subset of values
	// in instantiation of a struct. Other
	// fields get their default values
	v2 := Vertex{Y:1}

	// Array declaration
	var a [10]int

	// Slices are dynamically-sized
	q := []int{3, 5, 7}
	
	// Slices also can be created by
	// using start:end syntax
	some_primes := [4]int{2, 3, 5, 7}
	some_primes_slice := some_primes[1:3]
	
	// Slices don't store data, they reference
	// a section of underlying array, so 
	// changing elements of a slice also
	// changes underlying array
	some_primes_slice[0] = 11
	fmt.Println(some_primes_slice)

	// Creating a slice that references
	// structs created in slice definition
	struct_slice := []struct {
		name string
		val  int
	}{
		{"Tolga", 100},
		{"Tim", 70},
		{"Alice", 80},
	}

	// A slice has a length and capacity.
	// Length is number of elements a slice
	// refers to. Capacity of a slice is 
	// number of elements in underlying array
	// starting from the first element of the
	// slice!
	fmt.Println("Length:", len(some_primes_slice))
	fmt.Println("Capacity:", cap(some_primes_slice))

	// Zero value for a slice is nil
	// A nil slice has a length and
	// capacity of 0
	var s []int
	fmt.Printf("len=%d capacity=%d %v\n",
		len(s), cap(s), s)

	// We can create slices with built-in
	// make function to create dynamically
	// sized arrays
	// Creates a zeroed array and returns
	// a slice that refers to that array
	a := make([]int, 5) // len: 5 cap: 5

	// We can also provide a third argument
	// to determine capacity of the underlying
	// array
	a := make([]int, 0, 5) //len:0 cap: 5

	// We can create n-dimensional slices
	two_d_slice := [][]int{
		[]int{1, 2},
		[]int{1,2,3},
	}

	// To append elements to a slice we
	// can use built-in append function.
	// If the underlying array is not
	// sufficient, a new bigger array
	// is created
	a_slice := []int{1, 2}
	append(a_slice, 3, 4)

	// We can iterate over slices and 
	// maps by using range 
	for i, v := range a_slice {
		fmt.Printf("%d:%d", i, v)
	}

	// A map data structure associates
	// keys with values. We use make
	// function to initiliaze a map
	a_map = make(map[string]int)

	// We can also explicitly create
	// maps out of literals
	var a_map = map[string]int{
		"key1":5,
		"key2":10,
	}

	a_map := map[string]int{
		"key1":5,
		"key2":10,
	}

	// While appending a slice to another
	// we can use ... notation to prevent
	// explicitly specifting elements of
	// the second slice that will be
	// appended
	firstSlice := []byte{'a', 'b'}
	secondSlice := []byte{'c', 'd'}
	concatenatedSlice := append(firstSlice, secondSlice...)

	// Deleting a key-value pair
	delete(a_map, "key1")

	// Testing presence of a key
	// If key is present then ok 
	// evaluates to true
	value, ok := m["key3"]
}
