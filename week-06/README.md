# Week 6 - Project

## Project
Text based RPG game

## Stories

### Main menu Story
Simple command line main menu
#### Print menu
- Given a User
- When the program is runned by typing `python game.py`
- Then the menu should be shown
Menu items: New game, Load Game, Exit

#### Select menu item
- When the menu is show
- Then it should list the possible menu items
- Then it should require an integer as selecting a menu items

#### Enter submenu
- When the menu item is selected (by pressing enter)
- Then it should enter the submenu (by printing the sub menu list)

#### Wrong input
- Given the menu waiting for an input
- When wrong input is entered
- Then it should print an error message and require the input again

#### Exit menu item
- Given the menu waiting for an input
- When the Exit item is selected
- Then it should exit

### New game Story
#### Name
- Given a user
- When the `New Game` menu item is selected
- Then it should ask for a name
- Then it should display it after enter it

#### Name Submenu
- Given an entered name
- When the name is displayed
- Then it should show a submenu
Menu items: Reenter name, Continue, Save, Quit

#### Reenter Name
- Given an entered Name
- When the Reenter name submenu is selected
- Then it should ask for the name again

#### Quit
- Given an entered name
- When Quit is selected
- Then it should show the quit submenu:
Save and Quit, Quit without save, Resume
- Then Save and Quit should save the game and Quit
- Quit without save should not save the character

#### Roll stats
- Given an entered name
- When `Continue` is selected
- Then it should roll the basic stats and display them:
  - Dexterity: 1d6 + 6
  - Health: 2d6 + 12
  - Luck: 1d6 + 6
- Then it should show a submenu
Menu items: Reroll stats, Continue, Save, Quit

#### Reroll stats
- Given the rolled stats
- When `Reroll stats` is selected
- Then it should refresh the stats with new values

#### Select Potion
- Given the rolled stats
- When `Continue` is selected
- Then it should show a submenu
Menu items: Potion of Health, Potion of Dexterity, Potion of Luck

#### Choosed Potion
- Given the potion menu
- When the potion is selected
- Then it should print the selected potion and show a submenu
Menu items: Reselect the Potion, Continue, Quit

#### Reselect Potion
- Given the selected potion
- When the Reselect the Potion item is selected
- Then it should go back to the potion menu

#### Begin
- Given the selected potion
- When the Continue item is selected
- Then it should print the whole character stats:
  - Dexterity
  - Strength
  - Luck
  - Inventory:
    - Sword
    - Leather Armor
    - Selected potion
- Also it should show a submenu
Menu items: Begin, Save, Quit

### Save Story

#### Save menu
- Given any menu that contains the Save item
- When the save item is selected
- Then it should show a submenu, that lists the already saved items and other items
Menu items: add new item, Resume, Quit

#### Add new item
- Given the save menu displayed
- When the add new item is selected 
- Then it should ask for a name (finnish it with enter)
- Then it should create a new file with the given name like: <name>.json

#### Already saved item
- Given the save menu displayed
- When an already saved item is selected
- Then it should rewrite the file with the new state

#### Load game menu
- Given the main menu
- When the Load Game item is selected 
- Then it should show a submenu, that lists the already saved items and other items
Menu items: Quit

#### Load game
- Given the load menu
- When an item is selected
- Then it should read the state from the file and enter the game

### Fight

#### Test Fight
- Given a finished character
- When Begin is selected
- Then it prints that "Test your Sword in a test fight"
- Then it show your and a monsters stats:
  - Name
  - Max and current Health
  - Dexterity
  - Max and current Luck (Not for the monsters)
- Then it should show a fight submenu
Items: Strike, Retreat, Quit

#### Strike
- Given a fight menu
- When Strike is selected
- Then it should roll with 2d6 for the monster and the player as well
  add the dexterity for each and 
- If the player's is higher than the monsters print: You hit the monster
Print the submenu: Continue, Try your Luck, Retreat, Quit
- If the player's is higher than the monsters print: The monster hit you
Print the submenu: Continue, Try your Luck, Retreat, Quit

#### After strike
- Given the after strike menu
- When Continue is selected
- Then should show the Fight menu, and substract 2 from the loser

#### Try your luck
- GTiven the after strike menu
- When Try your luck is selected
- Then roll with 2d6 
- If your current luck is smaller than the result and the monster hit you,
  reduce 3 Health points
- If your current luck is at least the result and the monster hit you,
  reduce 1 Health points, and one luck 
- If your current luck is smaller than the result and you hit the monster,
  reduce 1 Health points
- If your current luck is at least the result and you hit the monster,
  reduce 4 Health points, and one luck

