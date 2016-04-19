from menu import Menu
from menu_item import MenuItem

def start_game():
    print('WOOOHOOOO')

def load_game():
    print('Commencing')

main_menu = Menu([
  MenuItem(1, 'Start Game', start_game),    
  MenuItem(2, 'Load Game', load_game)    
])

main_menu.choose(1)
