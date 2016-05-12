# Styleguide for Greenfox Velox

This is a document for containing the coding style guides at Greenfox's Velox class.
Currently covers:
- HTML
- CSS
- Python
- Javascript

## HTML and CSS

https://google.github.io/styleguide/htmlcssguide.xml

#### Exceptions
- HTML
    - Optional Tags
- CSS
    - Declaration Order

#### Additions
- HTML
    - Self closing slashes `/` for `void` HTML tags are optional in HTML5, be consistent, either use it in every `void` tag or in none
        - we will democratically agree to use it nowhere
        - list of `void` tags in HTML5: https://www.w3.org/TR/html-markup/syntax.html#syntax-elements
        ```html
        <!-- Good -->
        <link name="value">
        <img src="value">

        <!-- Bad -->
        <link name="value"></link>
        <img src="value"/>
        ```
- CSS
    - Use `::` instead of `:` on pseudo element selectors. Eg.:
    ```css
    /* Good */
    .my-class::after {
      content: "apple";
    }

    /* Bad */
    .my-class:after {
      content: "apple";
    }
    ```
## Python

https://google.github.io/styleguide/pyguide.html

## Javascript

https://github.com/airbnb/javascript
