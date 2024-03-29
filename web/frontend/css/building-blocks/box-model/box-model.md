<link rel="stylesheet" href="box-model.css" type="text/css">

## The Box Model
        Everything in CSS has a box around it. There are mainly two types of boxes: block boxes and inline boxes.

## Block and Inline Boxes
        These type distinction is based on how box behaves in terms of page flow and how
    it interacts with other boxes. By default, elements inside a box are laid out in normal
    flow and behave as block or inline boxes. Boxes also have an inner display type and outer display type. It can be set by using display property.

    1 - Outer display type
            If a box has an outer display type of block:
                - The box will break onto a new line.
                - The width and height properties are respected.
                - Padding, margin and border will cause other elements
                to be pushed away from the box.
                - The box will extend in the inline direction to fill
                the space in the container.
                - Elements such as <h1> and <p> uses block as their
                default outer display type.

            If a box has an outer display type of inline:
                - The box won't break onto a new line.
                - The width and height properties won't apply.
                - Vertical padding, margins and borders take effect,
                but they don't cause other elements to be pushed away
                from the box.
                - Horizontal padding, margins and borders take effect,
                and they cause other elements to be pushed away from 
                the box.
                - Elements such as <a>, <span>, <em> and <strong> use
                inline as their default outer display type.

    2 - Inner display type
            Inner display type determines how elements inside the box are laid out.
            It can be changed via display property. display property can change inner display as well as the outer display depending on what value is
            used.  For example just using flex only lays outs inner elements in flex layout and doesn't change   the outer display type of the element.
            It is not the case if inline-flex is used which causes outer display to be changed as well. By default elements inside a box are laid out
            in normal flow.

## Examples
        There are three block level elements in the example below. Paragraph has outer display type of block. It extends to the entire available width.
        List is also type of block. It means that it also extends to the entire width of the container, but in the example display of the inner elements
        are changed. span is an inline element, but its child can be displayed as a block element.

<p class="block-example">
    Paragraphs are block elements! Take a look to its border and how it extends to full extend of its container.
</p>
<ul class="block-example">
    <li>List is also a block element. </li>
    <li>But we can change display of </li>
    <li>the child elements in the container.</li>
</ul>
<p class="block-example">span is normally an <span class="block">inline</span> element. <span>But we can change its display too!</span></p>

        When display is changed to inline-flex, it doesn't just change the way child elements in the container shown, but also creates an inline container. As can be seen in the list below:

<ul class="inline-example">
    <li>Item One</li>
    <li>Item Two</li>
    <li>Item Three</li>
</ul>
<p class="inline">A paragraph that behaves as an inline element.</p>
<p class="inline">Another paragraph that behaves as an inline element.</p>

## CSS Box Model
        CSS box model applies to block boxes as a whole while it partially applies to inline boxes. It define how margin, border, padding and content work together to create a box.

<img src="box-model.png">

        Content box is the area where the content is displayed. It can be sized by inline-size, block-size, width and height.

        Padding box is the space around the content. Sized by padding property.

        Border box wraps all the content and padding. It is configured via border and related properties.

        Margin box is the space between this box and other elements. Configured via margin and related properties.

        inline-size, block-size, width and height properties determine the size of the content. Space taken up by the box is calculated by considering padding and border in addition to content size. Margin is not counted towards the size of the box, box ends in borders. It's called standard CSS box model.

<img src="standard-css-box-model.png">

        There is also alternative CSS box model. In alternative model, width is the width of the whole visible box on the screen not just width of the content box. Content area width is calculated as width-2xborder-2xpadding.

<img src="alternative-css-box-model.png">

        To use the alternative box model, box-sizing property on the html element must be border-box and all other elements must inherit it.

        html {
            box-sizing: border-box;
        }
        *,
        *::before,
        *::after {
        box-sizing: inherit;
        }

## Margin, Border, and Padding
        Margin: Margin is invisible space between the box and other elements. It can take positive or negative values. Negative margin can
        cause the box to overlap with other content on the page. Margins of adjacent boxes collapse. If both are positive then the largest
        one is used, if both are negative then the smallest one is used. If one is negative and other is positive then sum of them is used.

        Border: It is drawn between padding and margin. 

        Padding: It is between the border and the content area and used to push content away from the border. Unlike margin, it can't have
        negative value. Any applied background appears behind the padding.

## Display: inline-block
        display: inline-block makes an element to exhibit behaviour in the middle of inline and block types. It doesn't break into a new
        line, but its width, height properties are respected and its margin, border and padding properties push other elements away. It
        is quite common to allow padding in a link so that users can click it in easier way for example in navbars.

<p>
    I am a paragraph and this is a <span id="inline-block-example">span</span> inside that paragraph. A span is an inline element and so does not respect width and height.
</p>
<nav>
    <ul class="navbar-list">
        <li><a>Link One</a></li>
        <li><a>Link Two</a></li>
        <li><a>Link Three</a></li>
    </ul>
</nav>