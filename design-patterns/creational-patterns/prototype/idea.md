## Prototype 

Prototype pattern is used for the cases in which we need to have an exact copy of an object. To achieve this, we can go over  
all the fields, members, etc. that object have and attemp to copy them to the new object, but it isn't possible for some cases.  
Some members of the object can be private and unreachable outside its the class. Also, in some cases we only know the interface  
that object implements, but we don't know its concrete class. To be able to create a copy of the object even in this cases, we  
shouldn't be dependent on the class of the object to be copied.

Prototype pattern delegates the cloning operation to the objects to be cloned by declaring a common interface for the obhects  
that support cloning. In this way, objects can be cloned without coupling with its class. An Object that support cloning is  
called a prototype.