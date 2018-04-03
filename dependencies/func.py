import clue
import sqlite3

def write_clue():
    conn = sqlite3.connect("dependencies\clues.db")
    cursor = conn.cursor()
    print "Let's import some clues!"

    while True:
        #name = raw_input("Student's name: ")
        #username = raw_input("Student's username: ")
        #id_num = raw_input("Student's id number: ")

        new_clue = clue.Clue()

        sql = '''insert into clues (tier, value, stages) values (:tier, :value, :stages)'''
        cursor.execute(sql, {'tier':new_clue.tier, 'value':new_clue.value, 'stages':new_clue.stages})
        conn.commit()

        cont = raw_input("Another clue?" )
        if cont[0].lower() == "n":
            break
    cursor.close()
