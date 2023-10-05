argument = input("Entre Argument: ")

match argument:
    case "Hi":
        print("Hello")
    case "How Are You?":
        print("I am Good")
    case "Who Are You?":
        print("I am a bot build bye tiergamer.py")
    case _:
        print("I Don't Know Answer Of Your Argument")