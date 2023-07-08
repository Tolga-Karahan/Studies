## Factory Method

Factory method allows us to create objects without explicitly specifying the class. It also separates object construction code from the parts that are using created objects.  
In this way, we can extend construction code and add new types as needed.

Instead of directly instantiating classes, we can delegate this task to a factory method, and factory method relies on abstract types. In this way, we can introduce new types  
to the application without changing codebase.

We can either implement the pattern via inheritance or using a control statement in the factory method. In the first implementation, the class contains factory method can  
contain some business logic. Subclasses can use these business logic on the types created via their factory method which overrides the one in the base class. In second approach,
we provide an input, for example a string, to the factory method to make it instantiate corresponding class based on input.