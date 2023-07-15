## Abstract Factory

Abstract factory pattern allows us to produce families of related objects by delegating object creation instead of creating concrete classes directly.  
In this way, new types of diffent variants can be introduced with minimal changes. Both types and variants can be changed via factories without
changing the code base, because now factories as well depends on a abstract interface.

We should rely on interfaces for each distinct family of objects, and add their corresponding object creation methods to the Abstract Factory which    
is another abstract type as well. We can create concrete factories from this abstract factory for each variant of the objects.