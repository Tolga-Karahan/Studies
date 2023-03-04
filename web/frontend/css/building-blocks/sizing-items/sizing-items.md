<link rel="stylesheet" href="sizing-items.css" type="text/css">

Some items have intrinsic sizes by itself such as image which has the size of the image without applying any rule. On the other hand, some elements such as div doesn't have any size without content. We should give extrinsize size to such elements.

When padding and margin are set with percentages, their values are in relative to the parent container's inline size which is width in a horizontal language.

<div class="box">
    Margin and padding set to 10% on all sides.
</div>

There are some cases using max, min properties instead of using fixed properties. It is especially useful while dealing with variable size content. For example we can give a max-width to an image to ensure that it isn't larger then the limit if its intrinsic size is larger than the container, or to ensure that it is not pixelated by stretching if its intrinsic size is smaller than the container size.

<div class="container1">
    <div class="min-box"></div>
    <div class="min-box">
        This content is more than specified minimum height hence the size of the box grew.
    </div>
</div>

