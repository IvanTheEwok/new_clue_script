import clue    #contains the Clue class
import sqlite3

def write_clue():
    '''Let's the user input new clues into the database'''

    conn = sqlite3.connect("dependencies\clues.db")
    cursor = conn.cursor()
    print "Let's import some clues!"

    while True:
        new_clue = clue.Clue()

        sql = '''insert into clues (tier, value, stages) values (:tier, :value, :stages)'''
        cursor.execute(sql, {'tier':new_clue.tier, 'value':new_clue.value, 'stages':new_clue.stages})
        conn.commit()

        #Asks the user if they want to add another clue to the database.
        count = 0    #This will help us check if the user said yes or no.
        while True:
            cont = raw_input("Another clue? [y/n]: " )
            if cont[0].lower() == "n":
                count += 1    #If count == 1 outside this loop, the big loop in this function will break.
                break
            elif cont[0].lower() == "y":    #Continue the loop.
                break
            elif cont[0].lower() != "y" or "n":    #Invalid inputs.
                print "Null."
        if count == 1:    #Since the user input == n, the loop will break.
            break

    cursor.close()

def read_tier(tier):
    '''Reads all the clues of a specific tier in the database'''

    conn = sqlite3.connect("dependencies\clues.db")
    cursor = conn.cursor()

    sql = '''SELECT *
                FROM clues
                WHERE tier=?'''
    results = cursor.execute(sql, (tier,))
    all_clues = results.fetchall()
    cursor.close()
    return all_clues    #A list of all the clues of a specific tier.

def read_all():
    '''Reads all the clues in the database'''

    conn = sqlite3.connect("dependencies\clues.db")
    cursor = conn.cursor()

    sql = '''SELECT *
                FROM clues'''
    results = cursor.execute(sql)
    all_clues = results.fetchall()
    cursor.close()
    return all_clues    #A list of all the clues.

def completed_tier(tier):
    '''Counts all the completed clues in the tier.'''

    all_clues = read_tier(tier)    #Returns a list of all the clues in a specific tier.
    count = 0
    for clue in all_clues:
        count += 1
    return count

def completed_all():
    '''Counts all the completed clues'''

    all_clues = read_all()    #Returns a list of all the clues.
    count = 0
    for clue in all_clues:
        count += 1
    return count

def min_value_tier(tier):
    '''Returns the lowest reward value of a clue in a specific tier'''

    all_clues = read_tier(tier)
    min_value = 999999999    #A random number to use as a starting point.
    for clue in all_clues:
        if clue[1] < min_value:
            min_value = clue[1]
    return min_value

def min_value_all():
    '''Returns the lowest reward value of all clues'''

    all_clues = read_all()
    min_value = 999999999    #A random number to use as a starting point.
    for clue in all_clues:
        if clue[1] < min_value:    #The index 1 contains the value of the clue
            min_value = clue[1]
    return min_value

def max_value_tier(tuer):
    '''Returns the highest reward value of a specific tier'''

    all_clues = read_tier(tier)
    max_value = 0
    for clue in all_clues:
        if clue[1] > max_value:    #The index 1 contains the value of the clue
            max_value = clue[1]
    return max_value

def max_value_all():
    '''Returns the highest reward value of all clues'''

    all_clues = read_all()
    max_value = 0
    for clue in all_clues:
        if clue[1] > max_value:    #The index 1 contains the value of the clue
            max_value = clue[1]
    return max_value

def average_value_tier(tier):
    '''Returns the average reward value of a specific tier'''

    all_clues = read_tier(tier)
    total_value = 0
    count = 0
    for clue in all_clues:
        total_value += clue[1]    #The index 1 contains the value of the clue
        count += 1
    average_value = total_value / count
    return average_value

def average_value_all():
    '''Returns the average reward value of all clues'''

    all_clues = read_tier(tier)
    total_value = 0
    count = 0
    for clue in all_clues:
        total_value += clue[1]
        count += 1
    average_value = total_value / count
    return average_value


def statistics_tier(tier):
    '''Prints the statistics of a specific tier'''

    print "Completed: {}".format(completed_tier(tier))
    print "Min. value: {}".format(min_value_tier(tier))
    print "Max. value: {}".format(max_value_tier(tier))
    print "Average value: {}".format(average_value_tier(tier))

def statistics_all():
    '''Prints the statistics of all clues'''

    print "Completed: {}".format(completed_all())
    print "Min. value: {}".format(min_value_all())
    print "Max. value: {}".format(max_value_all())
    print "Average value: {}".format(average_value_all(tier))
