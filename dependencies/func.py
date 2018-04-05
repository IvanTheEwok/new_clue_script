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
                WHERE tier=tier'''
    results = cursor.execute(sql)
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
