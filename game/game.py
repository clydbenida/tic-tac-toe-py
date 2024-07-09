from services.display import Display
from services.input import Input
from services.menu import Menu
from helpers.constants import main_menu_items

class Game:
  def __init__(self) -> None:
    self.is_running = True
    pass

  def init(self, stdscr):
    display = Display(stdscr=stdscr)
    main_menu = Menu(items=main_menu_items)

    display.print_banner()
    display.print_menu(menu_items=main_menu.items)
    # main_menu.print()

    key = display.get_key()

    if key == ord('q'):
      self.is_running = False 

  def end_game(self):
    self.is_running = False