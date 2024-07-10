from services.display import Display
from services.input import Input
from services.menu.main import Menu
from services.menu.menus import getMainMenu
from helpers.constants import main_menu_items

class Game:
  def __init__(self) -> None:
    self.is_running = True
    pass

  def init(self, stdscr):
    display = Display(stdscr=stdscr)
    main_menu = getMainMenu()

    while True:
      display.screen.clear()

      display.print_banner()
      display.print_menu(menu=main_menu)

      display.screen.refresh()


  def end_game(self):
    self.is_running = False