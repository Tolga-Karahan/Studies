// Simplest object
let obj = {};

// An object example
const person = {
    //name: ["Bob", "Smith"],
    // Nested object
    name: {
        first: "Bob",
        last: "Smith"
    },
    age: 32,
    bio: function () {
        console.log(`${this.name.first} ${this.name.last} is ${this.age} years old.`);
    },
    // We can define functions via simpler syntax too
    introduceSelf() {
        // Its possible to access properties via bracket notation
        console.log(`Hi! I'm ${this["name"]["last"]}.`);
    },
};

// We can define a constructor to consruct as many
// objects as we desire
function Employee(firstName, lastName) {
    this.name = firstName;
    this.last = lastName;
}

let employee = new Employee("Tolga", "Karahan");

// Each JS object has a built-in property called a prototype.
// Because it's an object, the prototype also has a prototype.
// It's called prototype chain. Chain ends when there is a
// prototype whose own prototype is null. Prototypes of each
// object can be accessed via Object.getPrototypeOf() method.
// If an accessed property can't be found on the object, the
// property is searched inside its prototype, if it is not
// present in the immediate prototype then prototype of
// prototype is searched and so on. If end of the chain is
// reached, undefined is returned. Prototypes work like
// inheritance in some ways, but not completely same. It is
// more like delagation. An object either can do the thing
// requested from it by itself, or can delegate it to other
// objects, in this case to its prototype.

// We can set a prototype either via Object.create, or via
// constructor
const greetPrototype = {
    greet() {
        console.log("Hey!");
    },
};

// Create an object and assign greetPrototype as its
// prototype
let greetObj = Object.create(greetPrototype);
greetObj.greet()

// In JS all functions have a property called prototype.
// When function is used as a constructor, this property
// is assigned to new object as a prototype, so if we 
// change prototype property of constructor function,
// new prototype value will be assigned to newly created
// objects as prototype.
const personPrototype = {
    greet() {
        console.log(`Hi ${this.name}!`);
    }
}

function Person(name) {
    this.name = name;
}

Object.assign(Person.prototype, personPrototype);
const person2 = new Person("Tolga");
person2.greet();

// Properties directly defined on the object is called
// own properties. It can be checked via Object.hasOwn().
console.log(Object.hasOwn(person2, "name"))


// OOP constructs can be defined in JS in more traditional
// way, although they use prototypes under the hood.
// Prototypes resembles inheritance, but there are
// differences. For example in classical OOP, properties
// of a subclass and baseclass is combined in a single
// object. With prototyping, each prototype is a separate
// object. Prototype chain behaviour is more like delagation.
class Person {
    // Not mandatory. Constructor can create the field
    // # is added to make field private
    #name;

    constructor(name) {
        this.name = name;
        this.#privateMethod();
    }

    // # is added to make methods private as well
    #privateMethod() {
        console.log("It's a private method!");
    }

    introduceSelf() {
        console.log(`Hi. I'm ${this.name}!`);
    }
}

class Professor extends Person {
    #teaches;

    constructor(name, teaches) {
        super(name);
        this.teaches = teaches;
    }

    introduceSelf() {
        console.log(`Hi! I'm Professor ${this.name}. I teach ${this.teaches}.`)
    }

    grade(paper) {
        const grade = Math.floor(Math.random() * (5 - 1) + 1);
        console.log(`Grade of the paper ${paper} is ${grade}.`)
    }
}

prof = new Professor("Einstein", "Physics");
prof.grade("Tolga's Paper");

