<link rel="stylesheet" href="cascade-and-inheritance.css">

## Cascade, specificity, and inheritance
    Stylesheets have cascading structure. It means that the origin, the cascade layer, and
    the order of the CSS rules matter. If two rules from the same cascade layer applies to
    same element and if they have same specificity then the one that is defined last takes
    effect. 

    There are three factors ordered in increasing importance:
        1. Source order
        2. Specificity
        3. Importance

    Source Order
        If specificity weights are same, last rule is applied.

    Specificity
        Specificity calculated in points. Elements with higher points overrides elements
        with less points. Calculation is based on three different values: identifiers,
        classes and elements.

        Identifiers: Gets score one for each ID selector inside the overall selector.
        
        Classes: Gets score one for each class selector, attribute selector, or pseudo-
        class in the selector.

        Elements: Gets score one for each element selector or pseudo-element contained
        inside the overall selector.

        Universal selector(*), combinators(+, >, ~, ''), and specificity adjustment
        selector(:where()) have no effect on specificity. The negation(:not()) and
        the matches-any(:is()) pseudo-classes are not counted by themselves but their
        parameters are. Their specificity is the selector in their parameters which
        have most weight.
<table>
    <thead>
        <tr>
            <th>
                Selector
            </th>
            <th>
                Identifiers
            </th>
            <th>
                Classes
            </th>
            <th>
                Elements
            </th>
            <th>
                Total specificity
            </th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>h1</td>
            <td>0</td>
            <td>0</td>
            <td>1</td>
            <td>0-0-1</td>
        </tr>
        <tr>
            <td>h1 + p::first-letter</td>
            <td>0</td>
            <td>0</td>
            <td>3</td>
            <td>0-0-3</td>
        </tr>
        <tr>
            <td>li > a[href*="en-US"] > .inline-warning</td>
            <td>0</td>
            <td>2</td>
            <td>2</td>
            <td>0-2-2</td>
        </tr>
        <tr>
            <td>#identifier</td>
            <td>1</td>
            <td>0</td>
            <td>0</td>
            <td>1-0-0</td>
        </tr>
        <tr>
            <td>button:not(#mainBtn, .cta)</td>
            <td>1</td>
            <td>0</td>
            <td>1</td>
            <td>1-0-1</td>
        </tr>
    </tbody>
</table>

<h3 class="order_example">Order example</h1>

## Specificity
    Specificity is the algorithm that browsers use to decide which rules is applied to
    an element. If same property of the element is configured by multiple style blocks
    that are using different selectors, specificity decides the value that will be
    assigned to the property. It is a measure of the level of specificity of selectors.
    For example element selector selects all same elements on a page, so it is less
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

    Default inheritance behaviour can be changed by using special property values to
    control inheritance:

        - inherit: Sets selected element's property value to the parent's value for
        the same property.

        - initial: Sets value of property to its initial value.

        - revert: Resets the property value to the browser's default styling. Acts
        like unset in many cases.

        - revert-layer: Resets the property value to the value established in previous
        cascade layer.

        - unset: Sets the property to its natural value. If the property is naturally
        inherited it acts like inherit, otherwise it acts like initial.

<ul class="link_list">
    <li>Default <a href="#">link</a></li>
    <li class="link1">Inherit <a href="#">link</a></li>
    <li class="link2">Initial <a href="#">link</a></li>
    <li class="link3">Unset <a href="#">link</a></li>
    <li class="link4">Revert <a href="#">link</a></li>
</ul>
