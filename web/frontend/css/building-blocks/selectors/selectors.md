## CSS Selectors
    Selectors are used to target HTML elements to style them. Some more selectors are:

### Attribute selectors
    Allows us to select elements based on their attributes. For
    example if attribute is present or has a certain value: a[title], 
    a[href="example.com"]. 
    
    There are also other operators to match for attributes:
        - p[class^="value"]: If attribute starts with value.
        - p[class$="value"]: If attribute ends with value.
        - p[class*="value"]: If attribute contains value inside.
        - p[class~="value"]: If attribute is exactly value or contains it in space seperated list of values. For example if class attribute is like:
        class="abc value def".
        - p[class|="value"]: If attribute is exactly value or begins with value
        immediately followed by a hyphen. 

### Pseudo-classes and pseudo-elements
    Pseudo-classes style a state of the element. For example hover is a pseudo-class and can be used to style when user hovers on an element: a:hover. Pseudo-elements are used to select a part of the elements rather than the whole element. For example to style first line of a paragraph: p::first-line.

### Combinators
    Combinators combines different selectors. For example to select paragraphs that are direct children of <article> elenent: article > p.



