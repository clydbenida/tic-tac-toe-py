import curses
from services.menu.main import Menu  

class Display:
  def __init__(self, stdscr: curses.window):
    self.screen = stdscr
    self.dimensions = stdscr.getmaxyx()
    pass

  def get_key(self):
    return self.screen.getch()

  def print_menu(self, menu: Menu):
    selected_item = None
    for idx, item in enumerate(menu.items):
      if menu.selected_index == idx:
        self.screen.addstr(f"{item['label']}\n", curses.A_UNDERLINE)
        selected_item = item
      else:
        self.screen.addstr(f"{item['label']}\n")
    self.screen.refresh()

    key = self.get_key()

    if key == 10:
      selected_item['on_select']()
    elif key == curses.KEY_UP:
      self.screen.clear()
      menu.next()
    elif key == curses.KEY_DOWN:
      self.screen.clear()
      menu.prev()

    self.screen.refresh()

  def print_banner(self):
    banner = r"""
======================================
||                                  ||
||                                  ||
||     /$$   /$$        /$$$$$$     ||
||    | $$  / $$       /$$__  $$    ||
||    |  $$/ $$/      | $$  \ $$    ||
||     \  $$$$/       | $$  | $$    ||
||      >$$  $$       | $$  | $$    ||
||     /$$/\  $$      | $$  | $$    ||
||    | $$  \ $$      |  $$$$$$/    ||
||    |__/  |__/       \______/     ||
||                                  ||
||                                  ||
======================================
"""
    lines = banner.split("\n")
    for idx, line in enumerate(lines):
      self.screen.addstr(idx, 0, line)
      