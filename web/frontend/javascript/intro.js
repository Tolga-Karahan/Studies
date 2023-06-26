// === operator is for evaluating strict equality
'2' === 2; // False cause one is string another is number
5 === 2 + 3 // True

// == operator doesn't take data type into account,
// and can be misleading.
'2' == 2 // evaluates to true

// let keyword is used to declare variables
let myVar;

// const keyword is used to create constants. They must
// be declared and initialized in the same statement.
const myConst = 5;

// Data Types:
// JS have one data type for numbers: Number. There is
// also BigInt which is used for very large integers.
const myInt = 5;
const myFloat = 3.2;
console.log(typeof myInt);
console.log(typeof myFloat);

// typeof keyword returns the type of the variable
myVar = "Tolga";
typeof myVar;

// Strings
// string concatenation
one = "one";
two = "two";
cat = `${one}${two}`; // template literal
cat2 = one + two;

// template literals respect multi-line strings
const template = `a template literal
with multi lines.`;

// some conversions
a_num = Number("123");
a_string = a_num.toString();

// getting length
console.log(cat2.length);

// retrieve a letter
console.log(cat2[3]);

// testing if substring is included
console.log(cat2.includes("two"));

// to get position of substring in a bigger string
console.log(cat2.indexOf("two"));

// getting position of second occurrence
myString = "abcabc";
myString.
myString.indexOf("abc", myString.indexOf("abc") + 1);

// slicing
console.log(myString.slice(2, 4));

// Arrays
// various types can be stored in an array
const myArr = ["abc", 5, ["def", "ghi"]];

// getting length of the array
console.log(myArr.length);

// finding position of an element
console.log(myArr.indexOf(5));

// adding elements to the array
myArr.push("xyz", [1, 2, 3]);

// to add element to the start of the array
myArr.unshift("firstElement");

// removing last element from the array
myArr.pop();

// removing first element from the array
myArr.shift()

// removing an element by using its index
myArr.splice(1);

// mapping elements to new ones
myNums = [1, 2, 3];
console.log(myNums.map((x) => 2 * x));

// filtering elements in an array
myNums.filter((x) => x >= 2);

// splitting an string to an array
myStr = "abc, def, ghi";
strArr = myStr.split(',');
// to convert it to the same string
myStr = strArr.join(',');

// Conditionals
// plain old if-else statement
myBoolean = true;
if (myBoolean) {
    console.log("My boolean is true!");
} else {
    console.log("My boolean is false!");
}

// Any value that is not false, undefined, null,
// 0, NaN, or "" returns true when tested

// We should rely to switch stateemnts if there
// are too many conditions
const choice = "1";
switch (choice){
    case "1":
        console.log("Choice is 1");
        break;
    case "2":
        console.log("Choice is 2");
        break;
}

// Ternary
let ternaryVal = true ? 5 : 3;
console.log(ternaryVal);

// A simple loop
for (let i=1; i < 10; i++) {
    console.log(i);
}
// a foreach
const fruits = ["apple", "banana", "grape"]
for (const fruit of fruits) {
    console.log(fruit);
}

// Functions
// a simple function
function myFunction() {
    console.log("hey");
}

// an anonymous function
(function () {
    console.log("hey");
})

// arrow function notation can be used
// instead of anonymous functions
(() => console.log("Hey"));

// if arrow function only accepts one
// parameter, there is no need to use
// brackets
(param => console.log(param));

// if a arrow function only consists of
// a return statement, there is no need
// to specify return explicitly either
(param => param * 2);


// Events
// adding an event handler
btn = document.querySelector("button");

function clickHandler() {
    console.log("Hey!");
}
btn.addEventListener("click", clickHandler);

// we can also remove event listeners
btn.removeEventListener("click", clickHandler);

// we can also delete an event listener via
// controllers and AbortSignal
const controller = new AbortController(); 
btn.addEventListener("click",
    () => console.log("Hey"),
    { signal: controller.signal }
);
controller.abort();

// we can utilize event objects in event
// handlers. target property is the element
// targeted by the event, currentTarget 
// is the element that is handling the event
btn.addEventListener("click", (event) => {
    event.target.style.backgroundColor = "red";
})

// When event listeners are added to parent
// elements, event is invoked by interacting
// with child elements too. If child element
// also have a listener added to it, first
// listener of the child elements is invoked
// and then delagation goes up in the hierarchy.
// It is called event bubling in Javascript