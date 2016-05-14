# Review

### Spaces between CSS selectors and opening braces
There should be exactly 1 space between the selector and the brace.
```css
/* Good */
.classname {
}

/* Bad */
.classname{
}
```
See https://google.github.io/styleguide/htmlcssguide.xml?showone=Declaration_Block_Separation#Declaration_Block_Separation

### Layout workshop, fixed page layout excercise
#### Consider the responsibilites of the boxes semanticall
 - Use semantic elements, instead of `<div>`-s
 - The black box is content of the red box, it should be nested in it

#### Don't overuse position
 - Try to solve the problem without using position (expect the black box), rather try to use flex-box or float

#### Try to avoid style property duplication, use combined selectors
 - The sidebars has the same width
 - The header and the footer has the same height
