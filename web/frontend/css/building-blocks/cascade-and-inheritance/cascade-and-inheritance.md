<link rel="stylesheet" href="cascade-and-inheritance.css">

## Cascade
    Stylesheets have cascading structure. It means that the origin, the cascade layer, and
    the order of the CSS rules matter. If two rules from the same cascade layer applies to
    same element and if they have same specificity then the one that is defined last has
    effect. 

<h3 class="cascade_example">Cascade example</h1>

## Specificity
    Specificity is the algorithm that browsers use to decide which value of a property is
    applied to an element. If same property of the element is configured by multiple style
    blocks that are using different selectors, specificity decides the value that will be
    assigned to the property. It is a measure of the level of specificity of selectors.
    For example an element selector selects all same elements on a page, so it is less
    specific and has less weight comparing to a class selector which selects only the 
    elements that have same class attribute value.

<h3 class="specificity_example">Specificity example</h1>

## Inheritance
    Some CSS properties are set on the parent and are inherited in child elements some
    aren't. For example if color and font-family are set on an element, every element
    that is inside this element will also have same properties unless they don't define
    color and font-family by themselves. On the other side, width element is not
    inherited. For example if parent element's width set into 50%, its descendants
    don't have width of 50% of their parents.

<div id="inheritance_div">
    <p>Inherits color from parent element.</p>
    <p id="p_color">Defines its own color.</p>        
</div>