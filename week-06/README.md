# Week 6 - Project

## Project for the week

### TkWanderer - The tkinter RPG game
This is a hero based walking on tiles and killing monsters type of game. Heroes and monsters have levels and stats depending on their levels.

#### The Game screen
- the screen contains the first area, which is 20x20 tiles where the hero (and the monsters) can move
    - every area contains 20x20 tiles
- there tiles that cannot be occupied by any character (hero or monster)
- every area contains 5-10 monsters
- the monsters levels come from the number of the area
    - if its the Xth area, the mosters have lvl X (with 50% chance) or lvl X+1 (40%) or lvl X+2 (10%)
- one of the monsters holds the key to the next area

#### Moving
- the hero can move tile-by-tile in four directions on the screen by using the corresponding arrows (or wsad if preferred)
- after every two move, the monsters move one tile as well

#### The Characters
- every character has a (max and current) health point (HP), a defend (DP) and strike point (SP)
- these values can change during the game
- when a character's health point is 0 or below, it is dead
    - if its the hero, it is the end of the game

#### Starting stats
- Hero
    - HP: 20 + 3 * d6
    - DP: 2 * d6
    - SP: 5 + d6
- Monster Lvl x
    - HP: 2 * x * d6
    - DP: x/2 * d6
    - SP: x * d6

#### Battle
- when a hero enters a tile which is occupied by a monster, a battle forms
- the character entering the occupied tile is the attacker who starts the battle
- the attacker strikes on the defender, then the defender strikes and this continues until one of the characters dies
- after a won battle if the character is a hero, it levels up

#### Strike
- on a strike a strike value (SV) is calculated from SP and a random roll of 1-6 (d6)
- the strike is successful if d6*SP is higher than the other character's DP
- on a successful strike the other character's HP is decreased by the SV - the other character's DP

#### Leveling
- after successfully won battle the character is leveling up
- his max HP increases by d6
- his DP increases by d6
- his SP increases by d6

#### Entering next area
- when killing the monster who held the key to the next area, the hero enters immediately
    - which is like the previous one just with new and higher lvl monsters
- when entering a new area the hero has
    - 10% chance to restore all his HP
    - 40% chance to restore the third of his HP
    - 50% chance to restore 10% of his HP
