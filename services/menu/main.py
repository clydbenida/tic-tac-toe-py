import curses
from abc import ABC, abstractmethod
from typing import List, TypedDict

# Menu item type
class MenuItem(ABC):
  id: int
  label: str 
  
  def __init__(self, id, label) -> None:
    self.id = id
    self.label = label

  @abstractmethod
  def on_select(self):
    pass

class Menu:
  def __init__(self, items):
    self.items: List[MenuItem] = items
    self.selected_index: MenuItem = 0
    pass

  def print(self):
    print(self.items)

  def select(self):
    pass

  def next(self):
    last_idx = len(self.items) - 1
    if self.selected_index == last_idx:
      self.selected_index = 0
    else:
      self.selected_index = self.selected_index + 1 
  
  def prev(self):
    last_idx = len(self.items) - 1
    if self.selected_index == 0:
      self.selected_index = last_idx
    else:
      self.selected_index = self.selected_index - 1 
    pass
