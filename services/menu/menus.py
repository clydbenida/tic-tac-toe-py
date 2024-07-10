from services.menu.main import Menu

def getMainMenu():
  def on_start():
    pass

  def on_exit():
    exit()

  main_menu = Menu(items=[
    {
      "id": 1,
      "label": "> Start",
      "on_select": on_start
    },
    {
      "id": 2,
      "label": "> Exit",
      "on_select": on_exit
      },
  ])

  return main_menu