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

## Floats
    Floating an element changes behaviour of the element and following elements in normal flow. Floated element is removed from the normal flow and surrounding content floats around it.

<h2>Float Example</h2>
<div class="float-div">Float</div>
<p>
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla luctus aliquam
    dolor, eu lacinia lorem placerat vulputate. Duis felis orci, pulvinar id metus
    ut, rutrum luctus orci. Cras porttitor imperdiet nunc, at ultricies tellus
    laoreet sit amet. Sed auctor cursus massa at porta. Integer ligula ipsum,
    tristique sit amet orci vel, viverra egestas ligula. Curabitur vehicula tellus
    neque, ac ornare ex malesuada et. In vitae convallis lacus. Aliquam erat
    volutpat. Suspendisse ac imperdiet turpis. Aenean finibus sollicitudin eros
    pharetra congue. Duis ornare egestas augue ut luctus. Proin blandit quam nec
    lacus varius commodo et a urna. Ut id ornare felis, eget fermentum sapien.
</p>

## Positioning
    There are five positioning types:

       1) Static positioning: Default position of an element in the flow.
       2) Relative positioning: Moving an element in relative to its position in normal flow.
       3) Absolute positioning: It moves element out of normal flow and positions it in relative to the edges of closest ancestor, html if no other ancestor is positioned. As can be seen in the example, absolute positioned paragraph is excluded from the normal flow and it sits top of the normal flow. Thus, other two paragraphs are now neighbours in normal flow.
       4) Fixed positioning: Similar to absolute positioning, but it fixes an element relative to the browser viewport. It also moves element out of the normal flow.
       5) Sticky positioning: Makes an element act like relative positioning until it hits edges/offsets of the viewport, at which point it acts like fixed positioning.

<h2>Relative Positioning</h2>
<p class="normal-p">Basic paragraph</p>
<p class="relative-positioned-p">Relative positioned paragraph</p>
<p class="normal-p">Basic paragraph</p>

<h2>Absolute Positioning</h2>
<p class="normal-p">Basic paragraph</p>
<p class="absolute-positioned-p">Absolute positioned paragraph</p>
<p class="normal-p">Basic paragraph</p>

<div class="fixed">This box has fixed positioning no matter how much you scroll.</div>

<div class="sticky">This box has sticky positioning. Will behave as fixed when it hits to offsets of the viewport.</div>

## Multi-column Layout
    It is used to lay out content in columns. Can be applied by using column-count or column-width. The first property determines the number of columns, other is to specify a width and let browser to use as many columns as required.

<div class="multi-column">
  <h1>Multi-column Layout</h1>

  <p>
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla luctus
    aliquam dolor, eu lacinia lorem placerat vulputate. Duis felis orci,
    pulvinar id metus ut, rutrum luctus orci. Cras porttitor imperdiet nunc, at
    ultricies tellus laoreet sit amet. Sed auctor cursus massa at porta.
  </p>

  <p>
    Nam vulputate diam nec tempor bibendum. Donec luctus augue eget malesuada
    ultrices. Phasellus turpis est, posuere sit amet dapibus ut, facilisis sed
    est. Nam id risus quis ante semper consectetur eget aliquam lorem.
  </p>

  <p>
    Vivamus tristique elit dolor, sed pretium metus suscipit vel. Mauris
    ultricies lectus sed lobortis finibus. Vivamus eu urna eget velit cursus
    viverra quis vestibulum sem. Aliquam tincidunt eget purus in interdum. Cum
    sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus
    mus.
  </p>
</div>
