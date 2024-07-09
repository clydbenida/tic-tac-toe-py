class Input:
  def __init__(self):
    pass
  
  def display(self, message):
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    print(f"{UNDERLINE}{message}{END}")
    return input("> ")