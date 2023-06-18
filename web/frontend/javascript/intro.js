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



// A simple loop
const fruits = ["apple", "banana", "grape"]
for (const fruit of fruits) {
    console.log(fruit);
}

