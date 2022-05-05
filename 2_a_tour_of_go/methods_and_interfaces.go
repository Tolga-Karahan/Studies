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

type Vertex struct{
	X, Y float64
}

/* Type of the receiver should present
in the same package. Declaring a method
with a receiver whose type in another
package is not allowed. */

func (v *Vertex) Hypo() float64 {
	return math.Sqrt(v.X * v.X + v.Y * v.Y)
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
that implements those methods.*/
func (v *Vertex) One() float64 {
	return float64(1)
}

type VertexInterface interface {
	Hypo() float64
	One() float64
}

func main() {
	v := Vertex{3, 4}
	fmt.Println(v.Hypo())
	// Although receiver argument defined
	// as a pointer, there is no need to
	// pass a pointer.
	v.Scale(5)
	fmt.Println(v)

	var vertexInterface VertexInterface
	vertexInterface = &v
	fmt.Println(vertexInterface.Hypo())
	fmt.Println(vertexInterface.One())
}
