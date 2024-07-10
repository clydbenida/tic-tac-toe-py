import curses
from game.game import Game 

def main():
  game = Game()
  curses.wrapper(game.init)

main()