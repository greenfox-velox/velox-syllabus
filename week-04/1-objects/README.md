# Monday - Object Oriented Programing

## Practice

## Simple functions 
1. Create a function that sums the values of a list (create your own sum function)
2. Create a function that calculates factorial

## Objects
### Car
Create a `Car` class that has 3 properties:
 - The `type` of the car
 - The `color` of the car
 - The `km`-s the car already run
Methods:
 - It should have a method called `ride` that takes an integer and adds it to the `km`

### Bank account
Create a `Bank_account` class that stores a `name` and a `balance`
Methods:
 - It should have a method called `pay` that reduces the balance with the given amount
 - It should have a method called `receive` that increases the balance with the given amount
 - It should have a method called `print_balance` that prints the current balance

### RPG game
Create a Game Character class:
 - that stores it's Name
 - that stores it's Health Points (HP)
 - that stores it's Damage

Methods:
 - It should have a `print_status` method that describes the object:
   - if the `HP` are zero it should print it's name and "Dead"
   - if the `HP` are bigger than zero it should print it's name and `HP`
 - It should have a `drink_potion` method that increases its `HP` by 10
 - It should have a `strike` method that takes an other object and reduces it's `HP` by the current objects `demage` 

