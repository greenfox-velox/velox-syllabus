# HTML and CSS Review concerns

## General Problems
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

### Try to avoid CSS style property duplication
Use combined selectors, or a new class for the similarities.
```css
/* Bad */
.sidebar-left {
  width: 100px;
  height: 100px;
  background: orange;
}

.sidebar-right {
  width: 100px;
  height: 100px;
  background: purple;
}

/* Good */
.sidebar-left, .sidebar-right {
  width: 100px;
  height: 100px;
}

.sidebar-left {
  background: orange;
}

.sidebar-right {
  background: purple;
}
```

## Don't style general elements
 - Don't style general elements like `<div>`, `<span>` please use classes instead
```css
/* Bad */
span {
  color: red;
}

/* Good */
.alert {
  color: red;
}
```

## Workshop excercises
### Layout workshop, fixed page layout excercise
#### Consider the responsibilites of the boxes semantically
 - Use semantic elements, instead of `<div>`-s
 - The black box is content of the red box, it should be nested in it

#### Don't overuse position
 - Try to solve the problem without using position (expect the black box), rather try to use flex-box or float

### Layout workshop, modal layout exercise
#### Consider the responsibilites of the sections in the modal semantically
 - Use semantic elements, instead of `<div>`-s or `<p>`-s


