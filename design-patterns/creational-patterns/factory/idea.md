## Factory Method

Factory method separates object construction code from the parts that are using created objects. In this way, we can extend construction code and add new types as needed.

Instead of directly instantiating classes, we can delegate this task to a factory method, and factory method relies on abstract types. In this way, we can introduce new types to  
the application without changing codebase. The class contains factory method can contain some business logic. Subclasses can use these business logic on the types created  
via their factory method which overrides the one in the base class.