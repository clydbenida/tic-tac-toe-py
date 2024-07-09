import curses

global_stdscr = None

class Display:
  def __init__(self, stdscr):
    global_stdscr = stdscr
    self.screen = stdscr

    self.screen.clear()
    pass

  def get_key(self):
    return self.screen.getch()

  def print_menu(self, menu_items):
    for item in menu_items:
      self.screen.addstr(f"{item['label']}\n")
    self.screen.refresh()

  def print_banner(self):
    self.screen.addstr("""
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
""")