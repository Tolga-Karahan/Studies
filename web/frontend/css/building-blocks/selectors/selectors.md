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
        - p[class~="value"]: If attribute is equals to the value or
        contains it in space seperated list of values. For example
        if class attribute is like: class="abc value def".
        - p[class|="value"]: If attribute is equals to the value or
        begins with value immediately followed by a hyphen. 

### Pseudo-classes and pseudo-elements
    Pseudo-classes select elements that are in a specific state of the element or for
    example if they are the first element of their type. For example hover is a
    pseudo-class and can be used to style when user hovers on an element: a:hover. This
    type of pseudo-classes are called user-action or dynamic pseudo class because it is
    like a class is added to the element when user interacts with the element. Another
    example is selecting the first paragraph of an article element: article p:first-child.
    :first-child or *:first-child is corresponding to any element that is first child.
    
    Pseudo-elements are used to select a part of the elements rather than the whole
    element. Although similar to pseudo-classes they are not selecting an existing element
    but more like you adding a new element into HTML. For example to style first line of a
    paragraph: p::first-line. Another example is ::before and ::after pseudo-elements which
    are used to insert some content via content property. It is called generated content.
    Mostly used for visual purposes. Such as inserting arrow before and after text: 
    https://cssarrowplease.com.

    We can combine pseudo-classes and pseudo-elements together. For example if we want to
    select first line of first paragraph instead of selecting first lines of all paragraphs
    under an article: article p:first-child::first-line.

### Combinators
    Combinators combines different selectors. There are various combinator selectors.

    Descendant combinator: Selects the last element in the selector if previous elements in
    the selector are its parents. For example to target paragraphs
    that are inside an element whose class is box: .box p.

    Child combinator: Used to target direct child elements of an element. For example to
    target all paragraphs that are direct children of an article element: article > p.

    Adjacent sibling combinator: Selects last element in the selector if it is next sibling
    element of the previous one. For example to target paragprahs that are immediately 
    preceded by h1 elements: h1 + p.

    General sibling combinator: It is used to select all sibling elements that is not
    directly adjacent. For example to target all paragraph elements that are sibling with
    a h1 element: h1 ~ p.




