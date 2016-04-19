# Monday - TDD


## Tasks

### Anagramm
Write a function, that takes two strings and returns a boolean value based on
if the two strings are Anagramms or not.

### Count letters
Write a function, that takes a string as an argument and returns a dictionary
with all letters in the string ad keys, and numbers as values that shows how
many occurrences there are.

### RPG game
Create a Character class
Create a Game Character class:
 - that stores it's Name
 - that stores it's Health Points (HP)
 - that stores it's Damage

Methods:
 - It should have a `print_status` method that describes the object:
   - if the `HP` are zero it should print it's name and "Dead"
   - if the `HP` are bigger than zero it should print it's name and `HP`
 - It should have a `drink_potion` method that increases its `HP` by 10
 - It should have a `strike` method that takes an other object and reduces it's `HP` by the current objects `damage` 

Create a Cerlic class
 - It should have a `heal` method that can heal 10 `HP` on an other character

Create a Barbarian class
 - It should take a double damage on `strike`

Create a Monster class
 - It should heal 2 `HP` on each `strike`

Create a Wizard class
 - It should have an additional property called `manna`
 - On each `strike` the `manna` should reduce by 5
 - If the `manna` is more than 5 the taken damage on strike should be tripple on `strike` and third otherwise


