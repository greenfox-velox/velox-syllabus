# Thursday - Todo console application

## Before lesson materials

Mandatory:

None. :wink:

Optional:

* [argparse][1] for command-line argument parsing

## Tasks

Write a command-line todo application to easily keep track of your day-to-day tasks.

### Functional requirements

Basics (_mandatory_):

* A todo item has (at least) a `completed` state and a description
* Load todo items on application start
* Save todo items on application exit
* Add new items
* Complete items
* Remove items
* List items

Advanced (optional):

* Remove all completed items
* Add search functionality for items
* Add due date to items
* Sort items by due date
* Add priority to items
* Sort items by priority
* Handle multiple lists of items
* Support multiple item states (such as todo, in-progress, done)
* Boost user experience with [curses][2]

### Tips

* Use a simple text file to store items, every line is an item.
* To support more advanced features use a semi-structured format like JSON or CSV.
* Turn the application into a full-fledged [CLI][3] application by providing `--help`

### Sample solution

The sample solution can be found in the `todo` folder. It only implements the basic requirements. This aim was not to create a solution as complete as possible but to show how to structure your application so it can be easily extended in the future. It heavily focuses on composition[4].

#### How to use it?

    $ cd path/to/4-todo-app
    $ todo/todo

And follow the application menu from there.

Also see:

    $ todo/todo --help

#### How to explore?

1. Start from the `todo/todo` executable file. This contains the main loop and it wires together the menu and the business logic.
2. `todo/store.py`: this file contains the in-mempory store that keeps track of all the todo items managed by the app. It also know how to load and save (persist) items in files. It has two "backends" for persisting: simple text and json.
3. `todo/menu.py`: this file contains the framework for the menu system. The `Menu` class can display the menu element and run the chosen one. Each menu item has a command associated with it.
4. `todo/commands.py`: this file contains the actual business logic with all the available commands.
5. `todo/item.py`: this hold the data model which describes a single todo item.

[1]: https://docs.python.org/3.5/library/argparse.html#module-argparse
[2]: https://docs.python.org/3/howto/curses.html
[3]: https://en.wikipedia.org/wiki/Command-line_interface
[4]: https://en.wikipedia.org/wiki/Object_composition
