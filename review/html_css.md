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

### Use the short version of the self closing tags
```html
<!-- Bad -->
<img src="duck.png" alt="duck"/>

<!-- Good -->
<img src="duck.png" alt="duck">
```

### Try to avoid using HR and BR element
 - Use `<hr>` tag only for page break. For visual lines usually use borders.
 - Use `<br>` tag only for line break in inline text. For separating elements use block level wrappers.

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

### Don't style general elements
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

### Don't commit empty selectors
```css
/* Bad */
.something {

}
```

### UL should only have LIs as children
Please don't use any element as children to `<ul>`-s that is not `<li>`
```html
<!-- Bad -->
<ul>
  <li>Apple</li>
  <li>Pear</li>
  <ul>
    <li>Peach</li>
    <li>Melon</li>
  </ul>
</ul>

<!-- Good -->
<ul>
  <li>Apple</li>
  <li>Pear</li>
  <li>
    <ul>
      <li>Peach</li>
      <li>Melon</li>
    </ul>
  </li>
</ul>
```

### Use the shortest possible shorthands
```css
/* Bad */
margin: 5px 20px 5px 20px;

/* Good */
margin: 5px 20px;

/* Bad */
padding: 10px 5px 8px 5px;

/* Good */
padding: 10px 5px 8px;
```

### Don't use the same id for multiple elements
```html
<!-- Bad -->
<input type="radio" id="gender">
<input type="radio" id="gender">

<!-- Good -->
<input type="radio" id="female">
<input type="radio" id="male">
```

### Use hyphen case for ids and classes
Use hyphen case instead of underscore or CamelCase, for ids and classes
```css
/* Bad */
.myClass {}

/* Bad */
.my_class

/* Good */
.my-class
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


