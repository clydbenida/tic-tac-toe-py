def underlineString(string):
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    return f"{UNDERLINE}{string}{END}"
