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
        - draw one tile
        - draw the whole map with tiles
        - create a wall
        - draw some walls on the map
    - place a character on it and move with key bindings
        - draw a character
        - bind keyevents and handle them
        - handle walls
        - handle end of map
    - TDD create the heroes and monsters
        - this can be done easily test driven
        - create a class for the hero
        - stats
        - strike
        - lvl UP
    - create area and gamelogic
        - randMap
        - nextArea
        - generate monsters and BOSS
- Break down the stories to tasks
    - To classes
    - To methods
    - To data and actions
    - try to measure the time needed for the tasks
