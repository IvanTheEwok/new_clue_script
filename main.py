import dependencies.func as func

def main():
    while True:
        action = raw_input("What would you like to do? [write, statistics, quit]: ")
        if action.lower() == "quit":
            print "Goodbye!"
            break
        elif action.lower() == "write":
            func.write_clue()
        elif action.lower() == "statistics":
            action_statistics = raw_input("What statstics would you like to see? [easy, medium, hard, elite, master, all]: ")
            if action_statistics.lower() == "easy":
                #Print easy statistics
            elif action_statistics.lower() == "medium":
                #Print medium statistics
            elif action_statistics.lower() == "hard":
                #Print hard statistics
            elif action_statistics.lower() == "elite":
                #Print elite statistics
            elif action_statistics.lower() == "master":
                #Print master statistics
            elif action_statistics.lower() == "all":
                #Print all statistics
            else:    #Invalid input
                print "Null"
        else:    #Invalid input
            print "Null."

    raw_input()    #Press enter to quit

if __name__ == "__main__":
    main()
