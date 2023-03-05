<link rel="stylesheet" href="css-values-and-units.css" type="text/css">
 
## Values
    Every CSS property has a value type that defines the set of values allowed for the property. CSS value or data types are denoted in angle brackets such as: <color>.

### Lengths
    There are two types of lengths in CSS: relative and absolute. For example px is an absolute type. Relative units are relative to something else like parent properties such as font-size, em, rem, vw(viewport width), vh(viewport hight) are some examples. em is relative to the font-size of the parent in case it is a typographical property such as font-size, in case of other properties such as width it is relative to the font size of the element itself. rem is font size of the root element. vw and vh is relative to the viewport which is visible area of the page in the browser, 10vw means 10% of the viewport width.

### Percentages
    Percentages are always set relative to some other value. For example, if font-size or width is set by using percentage value, it will be a percentage of the parent value.

<div class="box px">I am 200px wide</div>
<div class="box percent">I am 40% wide</div>
<div class="container">
    <div class="box px">I am 200px wide</div>
    <div class="box percent">I am 40% wide</div>
</div>

### Functions
    Functions are also considered as values in CSS. For example, we can use calc() function as a value in order to make calculations in runtime, especially for the cases we can't know beforehand such as width or height of a container.

<div class="func-container">
    <p class="func-msg">My width is calculated dynamically!</p>
</div>