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

func main() {
	v := Vertex{3, 4}
	fmt.Println(v.Hypo())
	// Although receiver argument defined
	// as a pointer, there is no need to
	// pass a pointer.
	v.Scale(5)
	fmt.Println(v)

	// All methods on a type either should
	// have a a value or pointer receiver
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
	// can be though of as tuple of value
	// and types, so when a method is called
	// on interface value, it is actually
	// called on underlying type.

	// If interface value is nil then method
	// is called with nil receiver.
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
}
