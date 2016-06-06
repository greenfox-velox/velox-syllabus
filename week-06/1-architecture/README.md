# Architecture

## Materials

### Mandatory
 - https://www.youtube.com/watch?v=lbXsrHGhBAU
 - The 2nd chapter of the clean code book: Clean Code - A Handbook of Agile Software Craftsmanship / Robert C. Martin
     - http://ricardogeek.com/docs/clean_code.pdf

### Optional
 - The 1st chapter :)

## Assignment Review
- class / object
    - members (data, function)
    - instances / objects
- inheritance
- data and action encapsulation
- naming
    - variables
        - intention-revealing
        - avoid disinformation
        - pronounceable
        - searchable
    - classes
        - noun or noun phrase
        - not a verb!
        - avoid data synonyms
    - class instance methods
        - verb or verb phrase
        - dont be cute
        - be consistent
        - don pun (2 meanings)
        - context

## Workshop

### Todo app - how should it have ended

### Design ws in groups
- Designing stories
- Models
    - GameObject
        - Character
            - Monster
            - Hero
            - tpyes?
        - Area
        - Tile
            - EmptyTile
            - NotEmptyTile
- GameLogic
    - current hero
    - current area
- MainLoop
    - handling events
    - current game
- Stories
    - draw a screen with tiles
    - place a character on it and move with key bindings
    - TDD create the heroes and monsters
    - create area and gamelogic
- Break down the stories to tasks
    - To classes
    - To methods
    - To data and actions
    - try to measure the time needed for the tasks
