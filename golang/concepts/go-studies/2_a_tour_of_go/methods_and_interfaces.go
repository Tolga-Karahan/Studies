package main

import (
	"fmt"
	"math"
)

/* Although Go doesn't have classes,
methods still can be defined on types.
A method is a function with receiver
argument which appears between func
keyword and the method name. Receiver
indicates on which type we're going to
define the method.*/

type Vertex struct {
	X, Y float64
}

/* Type of the receiver should present
in the same package. Declaring a method
with a receiver whose type in another
package is not allowed. */

func (v *Vertex) Hypo() float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

/* Methods with pointer receivers can
be defined to change the values
the receiver points instead of
returning a new value. Another reason
to use pointer receivers is to avoid
copying. */

func (v *Vertex) Scale(scale float64) {
	v.X *= scale
	v.Y *= scale
}

/* An interface type is a set of method
signatures. Its value can hold any value
that implements those methods. Interfaces
are implemented implicitly. No need to
explicit declaration of intent such as
using implements keyword in some languages.*/
func (v *Vertex) One() float64 {
	return float64(1)
}

func (v *Vertex) nill_rec_example() {
	if v == nil {
		fmt.Println("Encountered nill receiver!")
		return
	}
	fmt.Println(("Encountered a concrete Vertex!"))
}

type VertexInterface interface {
	Hypo() float64
	One() float64
	nill_rec_example()
}

// One of the most used interfaces is Stringer
// interface which is defined in fmt package.
// A Stringer is a type that is able to describe
// itself as a string.
type Stringer interface {
    String() string
}

type IPAddr byte[4]
func (v IPAddr) String() string {
    return fmt.Sprintf("%d.%d.%d.%d", v[0], v[1], v[2], v[3])
}

// Another most used interface is Error which
// is used to express error state
type error interface {
    Error() string
}

type MyError interface {
    When time.Time
    What string
}

func (e *MyError) Error() string {
    return fmt.Sprintf("at %v, %s", e.When, e.What)
}

func GetError() error {
    return &MyError{
        time.Now(),
        "it didn't work"
    }
}

func main() {
	v := Vertex{3, 4}
	fmt.Println(v.Hypo())
	// Although receiver argument defined
	// as a pointer, there is no need to
	// pass a pointer.
	v.Scale(5)
	fmt.Println(v)

	// All methods on a type either should
	// have a value or pointer receiver
	// but not a mixture of both.

	var vertexInterface VertexInterface

	// If method is defined on pointer
	// receiver then interface value
	// also must be a pointer!
	vertexInterface = &v
	// This code is wrong:
	// vertexInterface = v
	fmt.Println(vertexInterface.Hypo())
	fmt.Println(vertexInterface.One())

	// Behind the scenes interface values
	// can be thought of as tuple of value
	// and types, so when a method is called
	// on interface value, it is actually
	// called on underlying type.

	// If interface value is nil then method
	// is called with nil receiver. Because
	// although it has a type info, it doesn't
	// has a value. In some other languages
	// it causes a null pointer exception, but
	// in Go it is possible to write methods
	// that gracefully handle the situation
	// in which method called with a nill
	// receiver.
	var v_ptr *Vertex
	// Although interface value holds a nill
	// concrete value, it is non-nil.
	vertexInterface = v_ptr
	vertexInterface.nill_rec_example()

	// A nill interface value holds neither
	// a value nor concrete type, so calling
	// it is a runtime error because there is
	// no type information at all:
	// var nillVertexInterface VertexInterface
	// nillVertexInterface.One()

	// Empty interface can take any type,
	// because every type at least implements
	// zero methods. It is used to receive
	// values whose types are unknown.
	var zeroInterface interface{}
	zeroInterface = 5
	fmt.Printf("(%v, %T)\n", zeroInterface, zeroInterface)
	zeroInterface = "Hi"
	fmt.Printf("(%v, %T)\n", zeroInterface, zeroInterface)

	// We can use type assertions to access
	// to an interface value's type and assign
	// it to a variable. If interface value's
	// type is not the specified type then it
	// triggers a panic. We can handle this
	// situation by adding another variable to
	// left hand side of the assignment
	// statement to receive a boolean to
	// understand whether interface value's
	// type is the specified type.
	t := zeroInterface.(string)
	t, ok := zeroInterface.(string)
	fmt.Println(t, ok)

	// We can use type switch constructs to
	// use several type assertions in series.
	switch v := zeroInterface.(type) {
	case int:
		fmt.Println("v has type of int!")
	case string:
		fmt.Println("v has type of string!")
	default:
		fmt.Println("v has a unknown type!")
	}

	/*
		io package has a Reader interface
		to read stream of data. Go has
		many implementations of this
		interface for files, network
		connections, compressors, ciphers,
		etc. This interface has a Read
		method which populates the provided
		slice with data and returns number
		of bytes populated:

		func (T) Read(b []byte) (n int, err error)
	*/
}
