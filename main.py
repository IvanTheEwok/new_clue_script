import dependencies.func

def main():
    while True:
        action = raw_input("What would you like to do? [read, write, statistics, quit]: ")
        if action.lower() == "quit":
            print "Goodbye!"
            break
        if action.lower() == "write":
            #clue = Clue()
            func.write_clue()

    raw_input()    #Press enter to quit

if __name__ == "__main__":
    main()
