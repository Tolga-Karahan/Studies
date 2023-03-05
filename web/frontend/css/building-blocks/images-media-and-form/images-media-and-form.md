<link rel="stylesheet" href="images-media-and-form.css" type="text/css">

# Replaced Elements

    Images and videos are considered as replaced elements. CSS can't affect the internal layout of these elements. It can affect their position on the page.

    Although we can put some width and height relative to the parent so that media doesn't overflow, still we might want to have image to preserve its aspect ratio. We can use object-fit property to configure this behaviour. While cover value scales the image with preserving its aspect ratio, contain value scales until image fits into the box, and fill value fills the box without respecting to aspect ratio.

<div class="container1">
    <div class="box">
        <img class="cover" src="balloons.jpg">
    </div>
    <div class="box">
        <img class="contain" src="balloons.jpg">
    </div>
</div>

    Another behavior of replaced elements is they behave slightly differently in layouts than other elements. For example, in grid and flex layouts they don't stretch like other elements, instead they are aligned to the start of the grid area or flex container.

<div class="container2">
    <img src="star.png">
    <div></div>
    <div></div>
    <div></div>
</div>

# Form Elements
    Some form elements are not as straightforward as HTML elements for styling. Nevertheless, form elements that allows text input are tend to behave as other elements.

<form>
    <div class="input">
        <label for="name">Name</label>
        <input type="text" id="name">
        <label for="email">Email</label>
        <input type="email" id="email">
        <span></span>
        <input type="submit" value="Submit">
    </div>
</div>