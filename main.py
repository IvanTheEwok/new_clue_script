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
            tiers = ["easy", "medium", "hard", "elite", "master"]
            for tier in tiers:
                if action_statistics.lower() == tier:
                    print "{tier} statistics:".format(tier=tier)
                    func.statistics_tier(tier)
        else:    #Invalid input
            print "Null."

    raw_input()    #Press enter to quit

if __name__ == "__main__":
    main()
