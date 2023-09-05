## Builder Pattern

Builder pattern allows us to build complex objects step-by-step. Imagine an object which can be constructed in a great variety of ways.  
Each possible combination can be a subclass, but in this case we end up with many subclasses. Instead, we can put all possible object  
construction combinations in the constructor, but we end up with a big constructor with many unused fields. It also makes object  
instantatiation quite ugly. 

Builder pattern delegates object construction code from object to build to builder objects. Builder objects has methods each coresponds  
to a step in construction process. This steps are optional and allows users to build objects in various combinations. Builder interface  
defines all possible steps, and concrete builder objects builds various representations of the product. End products don't need to be  
from common interface. As long as their construction steps are defined in the builder interface, we can build different types of objects.