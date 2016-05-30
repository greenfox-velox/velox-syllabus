# Monday - TDD

## Materials for this day
- https://jeffknupp.com/blog/2013/12/09/improve-your-python-understanding-unit-testing/
- https://www.youtube.com/watch?v=0Keq3E2bbeE
- http://docs.python-guide.org/en/latest/writing/tests/ (Just the general rules of testing)
- http://code.tutsplus.com/tutorials/beginning-test-driven-development-in-python--net-30137


## Assignment Review
- unit testing
- assertions
    - equals
    - true or false
    - in
    - not
    - raise
- what should you test?
- how should you name your test?
- what is TDD?

## Tasks

### The Big Testing

#### Setting up environment
- create a file named as `your_name_work.py`, and work in that file
- create the following methods in that file
- create a `your_name_test.py` where these methods are tested

#### def anagramm
Write a function, that takes two strings and returns a boolean value based on if the two strings are Anagramms or not.

#### def count_letters
Write a function, that takes a string as an argument and returns a dictionary with all letters in the string as keys, and numbers as values that shows how many occurrences there are.

#### Now for something completely different
Send me your work and test file on Slack, and in the afternoon we'll see how many of you go through against the tests of others'.

## Lunch somewhere around here

### Extension
Check out the `extend` folder. There's a work file and a test file.
- Run the tests, all 10 should be green (passing).
- The implementations though are not quite good.
- Create tests that'll fail, and will show how the implementations are wrong
- After creating the tests, fix the implementations
- Check again, if you can create failing tests
- Implement if needed

### Cows and Bulls
Create a class what is capable of playing exactly one game of Cows and Bulls (CAB). The player have to guess a 4 digit number. For every digit that the player guessed correctly in the correct place, they have a “cow”. For every digit the player guessed correctly in the wrong place is a “bull.”
- The CAB object should have a random 4 digit number, which is the goal to guess.
- The CAB object should have a state where the game state is stored (`playing`, `finished`).
- The CAB object should have a counter where it counts the guesses.
- The CAB object should have a guess method, which returns a string of the guess result
- All methods, including constructor should be tested
