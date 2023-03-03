<link rel="stylesheet" href="writing-mode-and-text-directions.css" type="text/css">

Writing mode is horizontal by default. When we change it to vertical, it changes block and inline directions. For example in vertical-rl mode, content flows from right to left and sentences run in vertical. In this case block direction becomes right to left and inline direction becomes top to bottom.

<div class="container">
    <div>
        <h1>Vertical Heading</h1>
        <p>Vertical paragraph</p>
    </div>
    <div class="horizontal-tb">
        <h1>Normal Heading</h1>
        <p>Normal paragraph</p>
    </div>
</div>