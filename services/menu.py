import curses

class Menu:
  def __init__(self, items):
    self.items = items
    self.selected_item = 0
    pass

  def print(self):
    print(self.items)

  def select(self):
    pass
