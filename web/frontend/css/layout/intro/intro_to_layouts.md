<link rel="stylesheet" href="style.css" type="text/css">
 Layouts
## Normal flow
    Normal flow is how browsers lay out HTML by default.

## Methods to change layout
    1) display property: It can change how elements behave in normal flow, for example by making an inline element to behave like a block element by getting values such as inline, block, inline-block, etc. It can also determine how child elements will be laid out in parent elements.

    2) float: It can make a block element to wrap along one side of a element. Takes values such as left, right, etc.
    
    3) position property: It is to control positioning of boxes inside other boxes.

    4) Table layout: To use features for styling tables to style non-table elements.
    
    5) Multi-column layout: To layout content in columns.

## Flexbox
    Flexbox is for laying out items in one dimension either in rows or columns. display:flex is used to lay out child elements in one dimension.

<div class="flex-wrapper">
    <div class="flex-box">One</div>
    <div class="flex-box">Two</div>
    <div class="flex-box">Three</div>
</div>
<br>

## Grid Layout
    Grid layout is designed for laying out elements in two dimensions. Used by setting display: grid.

<div class="grid-wrapper">
  <div class="grid-box">One</div>
  <div class="grid-box">Two</div>
  <div class="grid-box">Three</div>
  <div class="grid-box">Four</div>
  <div class="grid-box">Five</div>
  <div class="grid-box">Six</div>
</div>

    Each cell may take different size.

<div class="grid-wrapper2">
  <div class="grid-box1">One</div>
  <div class="grid-box2">Two</div>
  <div class="grid-box3">Three</div>
</div>
