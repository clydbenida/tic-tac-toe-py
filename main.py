import curses
from game.game import Game 

def main():
  game = Game()

  while game.is_running:
    curses.wrapper(game.init)

main()